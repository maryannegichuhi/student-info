from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    admissionnumber = models.CharField(max_length=200)

    class Meta:
        db_table = "student"


