from django.db import models


class Team(models.Model):
    image = models.ImageField(upload_to='team/images', default='', help_text='Ce champ est obligatoire')
    fname = models.CharField(max_length=60, help_text='Ce champ est obligatoire')
    lname = models.CharField(max_length=60, help_text='Ce champ est obligatoire')
    job = models.ManyToManyField('jobs.Job', related_name='jobs_team', help_text='Ce champ est obligatoire')
    skills = models.ManyToManyField('skills.Skill', related_name='skills_team', help_text='Ce champ est obligatoire')
    description = models.TextField(help_text='Ce champ est obligatoire')
    linkedin = models.CharField(max_length=250, null=True, help_text='Ce champ est obligatoire')
    malt = models.CharField(max_length=250, null=True, help_text='Ce champ est obligatoire')
    slug = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateField('Date de création', auto_now=True)
    modified_at = models.DateField('Mise à jour', auto_now=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
