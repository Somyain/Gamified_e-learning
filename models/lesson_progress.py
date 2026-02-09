from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ElearnLessonProgress(models.Model):
    _name = "elearn.lesson.progress"
    _description = "lesson Progress"
    
    _rec_name = "lesson_id"
    user_id = fields.Many2one('res.users',string="Student",required=True)
    lesson_id = fields.Many2one('elearn.lesson',string='Lesson',required=True)

    completed = fields.Boolean(string="Completed",default=False)
    completed_on = fields.Datetime(string="Completed On")

    def _check_completed_and_add_xp(self):
        for record in self:
            if not record.completed:
                continue
            if record.completed_on:
                raise ValidationError(
                    "This lesson is already marked as completed."
                )
            record.completed_on = fields.Datetime.now()
            xp = record.lesson_id.xp_reward
            user = record.user_id
            user.xp += xp