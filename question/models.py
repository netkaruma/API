from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=300)
    crated_at = models.DateField(auto_now_add=True)
    