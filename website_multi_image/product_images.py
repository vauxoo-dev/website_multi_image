from openerp import models, fields, api


# class product_image(models.Model):
#     _name = 'product.image'
#     _order = 'sequence, id DESC'

#     name = fields.Char('Name')
#     description = fields.Text('Description')
#     sequence = fields.Integer('Sequence')
#     image_alt = fields.Text('Image Label')
#     image = fields.Binary('Image')
#     image_small = fields.Binary('Small Image')
#     product_tmpl_id = fields.Many2one('product.template', 'Product', select=True)
#     from_main_image = fields.Boolean('From Main Image', default=False)


class ir_attachment(models.Model):
    _inherit = 'ir.attachment'

    image_id = fields.Many2one('product.template', string='Images')


class product_template(models.Model):
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
