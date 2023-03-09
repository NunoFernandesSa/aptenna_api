from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=250, help_text='Ce champ est obligatoire')
    created_at = models.DateField('Date de création', auto_now=True)
    modified_at = models.DateField('Mise à jour', auto_now=True)

    def __str__(self):
        return self.name

