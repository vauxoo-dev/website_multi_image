from openerp import models, fields, api


class product_image(models.Model):
    _name = 'product.image'

    name = fields.Char('Name')
    description = fields.Text('Description')
    image_alt = fields.Text('Image Label')
    image = fields.Binary('Image')
    image_small = fields.Binary('Small Image')
    product_tmpl_id = fields.Many2one('product.template', 'Product')


class product_product(models.Model):
    _inherit = 'product.product'

    images = fields.One2many('product.image', related='product_tmpl_id.images',
                             string='Images', store=False)


class product_template(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('product.image', 'product_tmpl_id',
                             string='Images')
