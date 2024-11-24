from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    sex = models.CharField(max_length=10, 
                        choices=[('m','Мужчина'),('w', 'Женщина')])
    active = models.BooleanField()
    startDate = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
