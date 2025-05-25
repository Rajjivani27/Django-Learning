from django.db import models
from django.contrib.auth.models import User

class Recepie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    recepie_name = models.CharField(max_length=100)
    recepie_description = models.TextField()
    recepie_image = models.ImageField(upload_to="receipe")

    def __str__(self):
        return self.recepie_name