from odoo import models, fields, api


class TacGia(models.Model):
    _name = 'model.tacgia'
    _rec_name = 'ho_ten'

    anh_dai_dien = fields.Binary(string='Ảnh đại diện')
    anh_ca_nhan = fields.Binary(string='Ảnh')
    ho_ten = fields.Char(string='Họ tên:')
    ngay_sinh = fields.Char(string='Ngày sinh')
    tac_pham = fields.Many2many(comodel_name='model.sach')
    mo_ta = fields.Text(string='Mô tả')
    tacpham_count = fields.Integer(compute='dem_so_tacpham', string='Số lượng tác phẩm', store=True)

    @api.model
    def create(self, vals):
        vals['ho_ten'] = vals['ho_ten'].title()
        rec = super(TacGia, self).create(vals)
        return rec
    
    def write(self, vals):
        result = super(TacGia, self).write(vals)
        return result
    
    def unlink(self):
        return super(TacGia, self).unlink()
    
    @api.depends('tac_pham')
    def dem_so_tacpham(self):
        for rec in self:
            rec.tacpham_count = len(rec.tac_pham)







