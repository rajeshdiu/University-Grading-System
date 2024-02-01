# myApp/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.name

class SubjectModel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    credit_hours = models.IntegerField(null=True)
    marks_obtained = models.FloatField(null=True)
    weighted_grade_point = models.FloatField(default=0.0,null=True)
    
    def __str__(self) -> str:
        return self.name
    
