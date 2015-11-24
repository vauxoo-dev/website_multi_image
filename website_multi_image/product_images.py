# coding: utf-8
from openerp import models, fields


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    _order = 'name asc'

    product_tmpl_id = fields.Many2one('product.template', string='Images')
    sequence = fields.Integer(
        'Sequence',
        help="Dragging and dropping an image at te beggining of the list of"
             "images will make the picture on top the default image to be"
             "shown if there is no main image in the product form.")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('ir.attachment', 'product_tmpl_id',
                             string='Images')
