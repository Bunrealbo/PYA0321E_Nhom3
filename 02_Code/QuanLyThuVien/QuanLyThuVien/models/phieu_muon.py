from odoo import models, fields, api
from odoo import _
from odoo.exceptions import ValidationError
import datetime
import re


class PhieuMuon(models.Model):
    _name = 'model.phieumuon'
    _rec_name = 'ma_phieu_muon'

    ma_phieu_muon = fields.Char(string='Mã phiếu mượn', copy=False,
                                default= lambda self: _('Tạo phiếu mượn'))
    ten_kh = fields.Char(string='Tên khách hàng:')
    sdt = fields.Char(string='Số điện thoại:')
    dia_chi = fields.Text(string='Địa chỉ:')
    danhsach_sach = fields.Many2many(comodel_name='model.sach')
    ngay_muon = fields.Date(string='Ngày mượn sách:', default=datetime.datetime.today(), store=True)
    ngay_tra = fields.Date(string='Ngày trả sách:')
    so_ngay_muon = fields.Integer(string='Số ngày mượn', compute='tinh_ngay_muon')
    tong_tien = fields.Integer(compute='tinh_tong_tien')
    tien_phat = fields.Integer(compute='tinh_tien_phat')
    trang_thai = fields.Selection(selection=[('0', 'Chờ xét duyệt'), ('1', 'Đang mượn'),
                                             ('2', 'Đã quá hạn'),('3', 'Đã từ chối'),('4', 'Đã trả sách')],
                                  default='0')

    @api.model
    def create(self, vals):
        vals['ten_kh'] = vals['ten_kh'].title()
        vals['dia_chi'] = vals['dia_chi'].title()
        if vals.get('ma_phieu_muon', 'Tạo phiếu mượn') == 'Tạo phiếu mượn':
            vals['ma_phieu_muon'] = self.env['ir.sequence'].next_by_code('model.phieumuon.sequence') or 'Tạo phiếu mượn'
        result = super(PhieuMuon, self).create(vals)
        return result

    def check_trang_thai(self):
        today = fields.Date.today()
        all_pm = self.env['model.phieumuon'].search([])
        for rec in all_pm:
            if rec.trang_thai == '1' and rec.ngay_tra < today:
                rec.trang_thai = '2'

    @api.depends('ngay_muon', 'ngay_tra')
    def tinh_ngay_muon(self):
        try:
            self.so_ngay_muon = abs((self.ngay_tra-self.ngay_muon).days)
        except:
            self.so_ngay_muon = 0

    @api.depends('ngay_muon', 'ngay_tra', 'danhsach_sach')
    def tinh_tong_tien(self):
        try:
            self.tong_tien = abs((self.ngay_tra-self.ngay_muon).days) * len(self.danhsach_sach) * 5000
        except:
            self.tong_tien = 0

    @api.depends('ngay_tra', 'danhsach_sach')
    def tinh_tien_phat(self):
        today_date = datetime.date.today()
        for rec in self:
            try:
                ngay_tra = fields.Date.to_date(rec.ngay_tra)
                tien_phat = (today_date-ngay_tra).days * len(rec.danhsach_sach) * 10000
            except:
                tien_phat = 0
            if tien_phat <= 0:
                self.tien_phat = 0
            else:
                self.tien_phat = tien_phat

    @api.constrains('sdt')
    def validate_sdt(self):
        if not re.match(r"^0+[0-9]{9}$", self.sdt):
            raise ValidationError('Vui lòng nhập sdt hợp lệ!!!')

    @api.constrains('danhsach_sach')
    def validate_list_book(self):
        if len(self.danhsach_sach) == 0:
            raise ValidationError('Vui lòng chọn ít nhất 1 sách trong phiếu mượn!!!')

    @api.constrains('ngay_muon', 'ngay_tra')
    def validate_ngay_tra(self):
        if self.ngay_tra <= self.ngay_muon:
            raise ValidationError('Ngày trả sách phải sau ngày mượn sách')

    def chap_nhan(self):
        self.trang_thai = '1'

    def tu_choi(self):
        self.trang_thai = '3'

    def da_tra(self):
        self.trang_thai = '4'






