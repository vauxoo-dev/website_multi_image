# coding: utf-8
from openerp import models, fields, api


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    image_id = fields.Many2one('product.template', string='Images')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('ir.attachment', 'image_id',
                             string='Images')
