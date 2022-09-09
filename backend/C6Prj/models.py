from django.db import models
from django.utils import timezone
import datetime




class projectDatabase(models.Model):
    courseInstructor = models.CharField(max_length=240)
    courseName = models.CharField(max_length=240)
    courseDescription = models.CharField(max_length=1024)
    courseCode = models.CharField(max_length=20, default=0)
    courseStartDate = models.DateField(default=timezone.now)
    courseEndDate = models.DateField(default=timezone.now)
    assignmentQuantity = models.IntegerField(max_length=20)


class assignmentDatabase(models.Model):
    projCode = models.CharField(max_length=20)
    assignmentName = models.CharField(max_length=240)
    assignmentDescription = models.CharField(max_length=1024)
    assignmentDueDate = models.DateField()
    assignmentRequiresGit = models.BooleanField()
    assignmentCode = models.CharField(max_length=20)
    assignmentDocument = models.URLField()
    assignmentMarksTotal = models.IntegerField()
    assignmentMarksSplit1 = models.IntegerField()
    assignmentMarksSplit2 = models.IntegerField()
    assignmentMarksSplit3 = models.IntegerField()
    assignmentMarksSplit4 = models.IntegerField()


class studentDatabase(models.Model):
    studentName = models.CharField(max_length=30)
    universityID = models.IntegerField()
    studentGroupNum = models.IntegerField()


class instructorDatabase(models.Model):
    projCode = models.CharField(max_length=20)
    projInstructor = models.CharField(max_length=30)
    universityID = models.IntegerField()


class submissionDatabase(models.Model):
    submissionDocument = models.URLField()
    submissionGitURL = models.URLField()
    studentGroupNum = models.IntegerField()



class evaluationDatabase(models.Model):
    assignmentCode = models.CharField(max_length=15)
    studentGroupNum = models.IntegerField()
    studentMarksSplit1 = models.IntegerField()
    studentMarksSplit2 = models.IntegerField()
    studentMarksSplit3 = models.IntegerField()
    studentMarksSplit4 = models.IntegerField()
    studentMarksTotal = models.IntegerField()
