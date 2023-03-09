from django.db import models


class Service(models.Model):
    """

    """
    name = models.CharField(max_length=100, help_text='Ce champ est obligatoire')
    description = models.TextField(help_text='Ce champ est obligatoire')
    slug = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='services/images', default='', help_text='Ce champ est obligatoire')
    created_at = models.DateField('Date de création', auto_now=True)
    modified_at = models.DateField('Mise à jour', auto_now=True)
