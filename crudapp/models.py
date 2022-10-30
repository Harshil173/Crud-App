from unittest.util import _MAX_LENGTH
from django.db import models

DEP_LIST = (
    ('CE','CE'),
    ('IT','IT'),
)
class sinfo(models.Model):
    Name = models.CharField(max_length=50)
    Erno = models.IntegerField()
    Dept = models.CharField(max_length=10,choices = DEP_LIST)
    College = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
