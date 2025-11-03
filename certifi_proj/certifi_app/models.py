from django.db import models

class Certificate(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    completion_date = models.DateField()
    student_email = models.EmailField()
    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
