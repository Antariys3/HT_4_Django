from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birth_date = models.CharField(max_length=15, blank=False)


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birth_date = models.CharField(max_length=15, blank=False)
    subject = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Group(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    curator = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="curated_groups"
    )

    def __str__(self):
        return self.name
