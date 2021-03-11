from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    answer_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        ret = {'subject_name': self.subject_name, 'answer_count': self.answer_count}
        return ret

class Answer(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)

    def __str__(self) -> str:
        ret = {'subject_name': self.subject, 'answer_text': self.answer_text}
        return ret