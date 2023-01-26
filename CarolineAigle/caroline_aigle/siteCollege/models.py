from django.db import models

class Article(models.Model):
    titre = models.fields.CharField(max_length=100)
    #TODO: ajouter choix type et image
    type = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
