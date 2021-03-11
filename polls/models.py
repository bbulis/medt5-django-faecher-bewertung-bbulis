from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    answer_count = models.IntegerField(default=0)

class Answer(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)