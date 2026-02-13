from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ElearnEnrollmentBase(models.AbstractModel):
    _name = "elearn.enrollment.base"
    _description = "Shared Enrollment Fields"

    user_id = fields.Many2one('res.partner',string="Student")

    state = fields.Selection(
        [
            ('enrolled', 'Enrolled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='enrolled',string="Status")

    email = fields.Char(string="Email")

class ElearnEnrollment(models.Model):
    _name = "elearn.enrollment"
    _inherit = "elearn.enrollment.base"
    _description = "Course Enrollment"

    _rec_name = 'user_id'

    enroll_date = fields.Datetime(string="Enrollment Date")

    student_image = fields.Binary(string="Student Image")

    enrollment_line_ids = fields.One2many('elearn.enrollment.line','enrollment_id',string="Enrolled Courses")

    _unique_email = models.Constraint('UNIQUE(email,course_id)','This email address is already registered in this course!' )

    @api.constrains('enrollment_line_ids')
    def _check_duplicate_courses(self):
        for rec in self:
            courses = rec.enrollment_line_ids.mapped('course_id')
            if len(courses) != len(set(courses.ids)):
                raise ValidationError("Duplicate courses are not allowed.")