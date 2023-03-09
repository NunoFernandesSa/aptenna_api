from django.db import models


class Technologie(models.Model):
    name = models.CharField(max_length=60, help_text='Ce champ est obligatoire.')
    image = models.ImageField(upload_to='technologies/images', default='', help_text='Ce champ est obligatoire.')
    description = models.TextField(blank=True, null=True, help_text='La description de la technologie est optionelle.')
    created_at = models.DateField('Date de création', auto_now=True)
    modified_at = models.DateField('Mise à jour', auto_now=True)

    def __str__(self):
        return self.name
