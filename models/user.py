from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    is_student = fields.Boolean(string="Is a Student",default=True)

    enrollment_ids = fields.One2many('elearn.enrollment','users_id',string="Enrollment Id")

    xp = fields.Integer(string="XP",default=0)

    level = fields.Integer(string="Level",default=1)