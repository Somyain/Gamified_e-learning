from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ElearnEnrollmentLine(models.Model):
    _name = "elearn.enrollment.line"
    _inherit = "elearn.enrollment.base"
    _description = "Enrollment Course Line"

    state = fields.Selection(related='enrollment_id.state')

    enrollment_id = fields.Many2one('elearn.enrollment',required=True)

    user_id = fields.Many2one( related='enrollment_id.user_id')

    course_id = fields.Many2one('elearn.course',required=True)

    lesson_ids = fields.One2many('elearn.lesson',compute='_compute_lesson_ids',string="Lessons",store=False)
    
    email = fields.Char(related='enrollment_id.email')

    enroll_date = fields.Datetime(related='enrollment_id.enroll_date')

    @api.depends('course_id')
    def _compute_lesson_ids(self):
        for record in self:
            if record.course_id:
                record.lesson_ids = record.course_id.lesson_ids
            else:
                record.lesson_ids = False

    # _sql_constraints = [
    #     (
    #         'unique_course_per_enrollment',
    #         'unique(enrollment_id, course_id)',
    #         'This course is already added for this student.'
    #     )
    # ]