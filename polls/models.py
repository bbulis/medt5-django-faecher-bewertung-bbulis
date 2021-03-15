from django.db import models

# Create your models here.
class Subject(models.Model):
    """
    class is data model for database connection
    """
    subject_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.subject_name

class Answer(models.Model):
    """
    class is for data modeling 
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.answer_text