{
    'name' : 'Gamified E-Learning',
    'version' : '1.0.0',
    'summary' : 'Custom gamified e-learning module',
    'category' : 'Education',
    'description' : """
                    Gamify learning is the mordern way of learning and applying your knowledge
    """,
    'author' : 'Somya',
    'depends' : ['base'],
    'data' : [
        'security/ir.model.access.csv',
        
        'views/course_views.xml',
        'views/lesson_views.xml',
        'views/enrollment_views.xml',
        'views/elearn_menu.xml',
        'views/user_views.xml',
    ],
    'installation':True,
    'appliation' :True,
    'auto-install':False,
}