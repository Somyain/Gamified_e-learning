from odoo import models, fields
from odoo.exceptions import ValidationError

class LessonCompleteWizard(models.TransientModel):
    _name = 'elearn.lesson.complete.wizard'
    _description = 'Complete Lesson Wizard'

    lesson_id = fields.Many2one('elearn.lesson',string="Lesson",required=True)

    user_id = fields.Many2one('res.partner',string="Student",required=True,default=lambda self: self.env.user)

    confirm = fields.Boolean(string="I confirm I have completed this lesson")

    def action_confirm(self):
        self.ensure_one()

        if not self.confirm:
            raise ValidationError("Please confirm lesson completion.")

        Progress = self.env['elearn.lesson.progress']
        existing = Progress.search([
            ('user_id', '=', self.user_id.id),
            ('lesson_id', '=', self.lesson_id.id)
        ], limit=1)

        if existing:
            raise ValidationError("You have already completed this lesson.")
        Progress.create({
            'user_id': self.user_id.id,
            'lesson_id': self.lesson_id.id,
            'completed': True,
        })
        return {'type': 'ir.actions.act_window_close'}