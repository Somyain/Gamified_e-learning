from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ElearnEnrollment(models.Model):
    _name = "elearn.enrollment"
    _description = "Course Enrollment"
    
    _rec_name = 'users_id'
    users_id = fields.Many2one('res.partner',string="Student",required=True)
    course_id =fields.Many2one('elearn.course',string='Course',required=True)
    state = fields.Selection(
        [('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ],default='enrolled',string="Status")
    enroll_date=fields.Datetime(string="Enrollment Date",)

    student_image = fields.Binary(string="Student Image")

    @api.constrains('users_id','course_id')
    def _check_duplicate_enrollment(self):
        for record in self:
            if not record.users_id or not record.course_id:
                continue
            domain = [
                ('users_id', '=', record.users_id.id),
                ('course_id', '=', record.course_id.id),
                ('id', '!=', record.id),
            ]
            if self.search_count(domain):
                raise ValidationError(f"Student {record.users_id.name} is already enrolled in the course {record.course_id.name}.")