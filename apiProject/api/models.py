from django.db import models

class studentModel(models.Model):
    username = models.CharField(max_length=100, null=True)
    studentRoll = models.IntegerField(null=True)
    Name = models.CharField(max_length=100, null=True)
    Age = models.IntegerField(null=True)
    DateofBirth = models.DateField(null=True)
    
    def __str__(self):
        return self.Name