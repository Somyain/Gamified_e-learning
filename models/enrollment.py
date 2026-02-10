from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ElearnEnrollment(models.Model):
    _name = "elearn.enrollment"
    _description = "Course Enrollment"
    
    _rec_name = 'user_id'
    user_id = fields.Many2one('res.partner',string="Student",required=True)
    course_id =fields.Many2one('elearn.course',string='Course',required=True)
    state = fields.Selection(
        [('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ],default='enrolled',string="Status")
    enroll_date=fields.Datetime(string="Enrollment Date",)

    student_image = fields.Binary(string="Student Image")

    lesson_ids = fields.One2many('elearn.lesson',related='course_id.lesson_ids',string="Lessons",compute='_compute_course_lessons',store=False)

     #_constraint_name = models.Constraint(sql_definition, error_message)
    email = fields.Char(string='Email')
    
    _unique_email = models.Constraint('UNIQUE(email,course_id)', 'This email address is already registered in this course!')

    @api.depends('course_id')
    def _compute_course_lessons(self):
        for record in self:
            record.lesson_ids = record.course_id.lesson_ids if record.course_id else False

    @api.constrains('user_id','course_id')
    def _check_duplicate_enrollment(self):
        for record in self:
            if not record.user_id or not record.course_id:
                continue
            domain = [
                ('user_id', '=', record.user_id.id),
                ('course_id', '=', record.course_id.id),
                ('id', '!=', record.id),
            ]
            if self.search_count(domain):
                raise ValidationError(f"Student {record.user_id.name} is already enrolled in the course {record.course_id.name}.")
    