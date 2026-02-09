from odoo import models , fields

class ElearnLesson(models.Model):
    _name = 'elearn.lesson'
    _description = 'E-Learning Lesson'

    name = fields.Char(string="Lesson Title", required=True)
    course_id = fields.Many2one('elearn.course', string="Course", required=True)
    content = fields.Html(string="Lesson Content")

    xp_reward = fields.Integer(string="XP Reward", default=10)