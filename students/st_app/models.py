from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birth_date = models.CharField(max_length=15, blank=False)
