from django.db import models
class CourseModel(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.TextField(max_length=50,unique=True)
    fee=models.FloatField()

class CommonModel(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.TextField(max_length=30)
    contact=models.IntegerField(unique=True)
    subject=models.CharField(max_length=30)

    class Meta:
        abstract=True

class FacultyModel(CommonModel):
    subject =models.ManyToManyField(CourseModel)
    salary=models.FloatField()

class StudentModel(CommonModel):
    subject = models.ManyToManyField(CourseModel)
    fee=models.FloatField()