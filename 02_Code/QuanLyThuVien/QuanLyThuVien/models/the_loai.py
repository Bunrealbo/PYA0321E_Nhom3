from odoo import models, fields, api


class TheLoai(models.Model):
    _name = 'model.theloai'
    _rec_name = 'ten_theloai'

    ten_theloai = fields.Char(string='Tên thể loại')
    ten_sach = fields.Many2many(comodel_name='model.sach', string='Tên sách')