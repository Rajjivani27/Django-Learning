from django.db import models

class Recepie(models.Model):
    recepie_name = models.CharField(max_length=100)
    recepie_description = models.TextField()
    recepie_image = models.ImageField(upload_to="receipe")

    def __str__(self):
        return self.recepie_name