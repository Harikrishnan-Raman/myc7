from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.


class User(AbstractUser):
    role = models.CharField('ROLE', max_length=63)
    username = models.CharField('USERNAME', unique=True, max_length=15)
    universityID = models.CharField('Univ ID', max_length=15)


class projectDatabase(models.Model):
    courseInstructor = models.CharField(max_length=240)
    courseName = models.CharField(max_length=240)
    courseDescription = models.CharField(max_length=1024)
    courseStartDate = models.DateField(default=timezone.now)
    courseEndDate = models.DateField(default=timezone.now)
    assignmentQuantity = models.IntegerField(max_length=20)




class assignmentDatabase(models.Model):
    projCode = models.CharField(max_length=20)
    assignmentName = models.CharField(max_length=240)
    assignmentDescription = models.CharField(max_length=1024)
    assignmentStartDate = models.DateField()
    assignmentDueDate = models.DateField()
    assignmentRequiresGit = models.BooleanField()
    assignmentMarksTotal = models.IntegerField()

class evaluationDatabase(models.Model):
    splitUpComponent = models.CharField(max_length=240)
    alottedMarks = models.IntegerField()
    evaludation_data = models.ForeignKey(assignmentDatabase, on_delete=models.CASCADE, related_name='evaluation')

    def __str__(self):
        return '%d: %s' % (self.alottedMarks, self.splitUpComponent)






class marksDatabase(models.Model):
    assignmentCode = models.CharField(max_length=20)
    groupID = models.IntegerField()
    comment = models.CharField(max_length=240)

class marksSplitDatabase(models.Model):
    obtainedMarks = models.IntegerField()
    alottedMarks = models.IntegerField()
    eval_data = models.ForeignKey(marksDatabase, on_delete=models.CASCADE, related_name='eval')

    def __str__(self):
        return '%d: %d' % (self.alottedMarks, self.obtainedMarks)

