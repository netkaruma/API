from django.db import models
# Create your models here.

class Answer(models.Model):
    question_id = models.ForeignKey("question.Question", on_delete=models.CASCADE)
    user_id = models.UUIDField()
    text = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=False, auto_now_add=True)