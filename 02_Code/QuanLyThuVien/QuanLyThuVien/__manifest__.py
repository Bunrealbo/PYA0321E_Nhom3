# -*- coding: utf-8 -*-
{
    'name': 'Đồ án quản lý thư viện (ITPLUS COURSE) ',
    'version': '1.0',
    'summary': 'Ứng dụng quản lý thư viện',
    'sequence': 0,
    'author': 'Phuong2711 & VTD',
    'description': """
        Đồ án xây dựng ứng dụng quản lý thư viện
    """,
    'category': 'Quản lý',
    'website': '',
    'depends': ['mail',
                ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/sach_view.xml',
        'views/theloai_view.xml',
        'views/kho_sach_view.xml',
        'views/phieu_muon_view.xml',
        'views/tac_gia_view.xml',
        'views/template.xml',
        'data/auto_change_state.xml',
        'reports/report.xml',


    ],
    'installable': True,
    'application': True,
}