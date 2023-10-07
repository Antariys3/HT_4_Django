from django.shortcuts import render, redirect
from faker import Faker

from st_app.forms import TeacherForm, GroupForm
from st_app.models import Student, Teacher, Group

fake = Faker("ru-RU")


# ДЗ 4. Django
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


# ДЗ 5. Black, GitHub Actions, Django commands
def teachers_list(request):
    list_teachers = Teacher.objects.all().order_by("-id")
    return render(request, "teachers_list.html", context={"teachers": list_teachers})


# ДЗ 6. Django Forms
def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teachers_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        teacher = Teacher.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            birth_date=request.POST["birth_date"],
            subject=request.POST["subject"],
        )
        return redirect(teachers)

    return render(request, "teachers_form.html", {"form": form})


def teachers(request):
    list_teachers = Teacher.objects.all().order_by("-id")
    return render(request, "teachers.html", context={"teachers": list_teachers})


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "groups_form.html", {"form": form})
    form = GroupForm(request.POST)
    if form.is_valid():
        group = Group.objects.create(
            name=request.POST["name"],
            curator_id=request.POST["curator"],
        )
        return redirect(groups)

    return render(request, "groups_form.html", {"form": form})


def groups(request):
    list_groups = Group.objects.all().order_by("-id")
    return render(request, "groups.html", context={"groups": list_groups})
