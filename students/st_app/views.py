from django.shortcuts import render
from faker import Faker

from st_app.models import Student
from st_app.models import Teacher

fake = Faker("ru-RU")


def index(request):
    return render(request, "index.html")


def generate_student(request):
    # id, first_name, last_name, birth_date
    Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date(pattern="%d-%m-%Y"),
    )
    return render(request, "generate_student.html")


def generate_students(request):
    count = int(request.GET.get("count", 10))
    if count <= 0:
        return render(
            request,
            "error.html",
            {"message": "Query параметр должен быть положительным числом"},
        )
    else:
        count = min(count, 100)
        for i in range(count):
            Student.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date(pattern="%d-%m-%Y"),
            )
        return render(request, "generate_students.html", {"count": count})


def students(request):
    list_students = Student.objects.all()
    return render(request, "students.html", context={"students": list_students})


def teachers(request):
    list_teachers = Teacher.objects.all()
    return render(request, "teachers.html", context={"teachers": list_teachers})
