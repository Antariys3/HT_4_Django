from django.db import models
from django.urls import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birth_date = models.CharField(max_length=15, blank=False)
    group = models.ForeignKey(
        "Group", on_delete=models.CASCADE, related_name="students", null=True
    )
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse("student_delete", args=[str(self.id)])


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birth_date = models.CharField(max_length=15, blank=False)
    subject = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse("teacher_delete", args=[str(self.id)])


class Group(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    curator = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="curated_groups"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("group_delete", args=[str(self.id)])
