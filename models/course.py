from odoo import models, fields ,api 

class ElearnCourse(models.Model):
    _name = 'elearn.course'
    _description  = 'E-Learning Course'

    name = fields.Char(string="Course Name",required=True)
    description = fields.Text(string="Description")

    lesson_ids = fields.One2many('elearn.lesson','course_id',string="Lessons")
    lesson_count = fields.Integer('Lesson Count',compute='_compute_lesson_count')

    enrollment_ids = fields.One2many('elearn.enrollment','course_id',string="Enrollments")

    enrollment_count = fields.Integer(string="Enrollment Count",compute='_compute_enrollment_count')

    @api.depends('lesson_ids')
    def _compute_lesson_count(self):
        for record in self:
            record.lesson_count = len(record.lesson_ids)

    def action_open_lessons(self):
        self.ensure_one()
        return {
            'type':'ir.actions.act_window',
            'name':'Lessons',
            'res_model':'elearn.lesson',
            'view_mode': 'list,form',
            'domain': [('course_id', '=', self.id)],
            'context': {
                'default_course_id': self.id
            }
        }

    @api.depends('enrollment_ids')
    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = len(record.enrollment_ids)

    def action_open_enrollments(self):
        self.ensure_one()
        return{
            'type': 'ir.actions.act_window',
            'name': 'Enrollments',
            'res_model': 'elearn.enrollment',
            'view_mode': 'list,form',
            'domain': [('course_id', '=', self.id)],
            'context': {
                'default_course_id': self.id
            }
        }