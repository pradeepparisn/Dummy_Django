from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class Applicant(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    paddress=models.CharField(max_length=122)
    dob=models.DateField()
    branch=models.CharField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.name
    