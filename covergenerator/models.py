from django.db import models

MISSIONS_CHOICES = [
    ('standard', 'Standard'),
    ('ed-tech', 'Ed-Tech'),
    ('ecology', 'Ecology'),
    ('energy', 'Energy'),
    ('enabling_connections', 'Connexion'),
    ('géographies', 'Géographies'),
    ('aménagement_du_territoire', 'Aménagement du territoire'),
    ('histoire', 'Histoire'),
    ('politique', 'Politique'),
    ('education', 'Education'),
    ('sécurité', 'Sécurité'),
    ('fonction_publique', 'Fonction publique'),
    ('animaux', 'Animaux'),
    ('féminisme', 'Féminisme'),
    ('sexualité', 'Sexualité'),
    ('social_justice', 'Social-justice'),
    ('arts', 'Arts'),
    ('sport', 'Sport'),
    ('esn', 'ESN'),
    ('justice', 'Justice'),
    ('immobilier', 'Immobilier'),
    ('cybersecurite', 'Cybersecurité'),
]

STATUS_CHOICE = [
    ('pending', 'Pending'),
    ('rh_interview', 'RH interview'),
    ('tech_iterview', 'Tech interview'),
    ('final_interview', 'Final interview'),
    ('declined', 'Declined'),
    ('hired', 'Hired'),
]

class Application(models.Model):

    company_name = models.CharField(max_length=255)
    job_offer_link = job_offer_link = models.URLField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    mission = models.CharField(max_length=50, choices=MISSIONS_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='pending')
    python = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    html_css = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    typescript = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    next = models.BooleanField(default=False)
    tailwind = models.BooleanField(default=False)
    node = models.BooleanField(default=False)
    vuejs = models.BooleanField(default=False)
    bdd = models.BooleanField(default=False)
    devops = models.BooleanField(default=False)
    java = models.BooleanField(default=False)
    angular = models.BooleanField(default=False)
    php = models.BooleanField(default=False)
    ruby = models.BooleanField(default=False)
    go = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.company_name} - {self.mission}"