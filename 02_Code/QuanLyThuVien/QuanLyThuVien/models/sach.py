from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Sach(models.Model):
    _name = 'model.sach'
    _rec_name = 'ten_sach'

    ten_sach = fields.Char(string='Tên sách')
    tac_gia = fields.Many2many(comodel_name='model.tacgia', string='Tác giả')
    anh = fields.Binary(string='Ảnh')
    so_trang = fields.Integer(string='Số trang')
    the_loai = fields.Many2many(comodel_name='model.theloai', inverse_name='ten_sach', string='Thể loại')
    mo_ta = fields.Text(string='Mô tả')
    anh_sach = fields.Binary(string='Ảnh sách')

    @api.model
    def create(self, vals):
        vals['ten_sach'] = vals['ten_sach'].title()
        record = super(Sach, self).create(vals)
        return record
    
    def write(self, vals):
        result = super(Sach, self).write(vals)
        return result
    
    def unlink(self):
        return super(Sach, self).unlink()

    @api.constrains('so_trang')
    def validate_sotrang(self):
        if not self.so_trang or self.so_trang <= 0:
            raise ValidationError('Số trang phải lớn hơn 0!')



