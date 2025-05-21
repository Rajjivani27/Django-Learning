from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=30)
    medaltype = [
        ('GL','Gold'),
        ('SL','Silver'),
        ('BR','Bronze')
    ]

    Medaltype = models.TextField(choices=medaltype)