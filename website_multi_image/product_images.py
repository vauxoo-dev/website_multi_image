# coding: utf-8
from openerp import models, fields, api


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    image_id = fields.Many2one('product.template', string='Images')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('ir.attachment', 'image_id',
                             string='Images')

    @api.one
    def action_copy_image_to_images(self):
        if not self.image:
            return
        image = None
        for r in self.images:
            if r.from_main_image:
                image = r
                break

        if image:
            image.image = self.image
        else:
            vals = {'image': self.image,
                    'name': self.name,
                    'product_tmpl_id': self.id,
                    'from_main_image': True, }
            self.env['ir.attachment'].create(vals)
