from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from faker import Faker

from st_app.forms import TeacherForm, GroupForm, StudentForm
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
    list_students = Student.objects.all().order_by("-id")
    return render(request, "students.html", context={"students": list_students})


# ДЗ 6. Django Forms
def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teachers_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("teachers")

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
        form.save()
        return redirect("groups")

    return render(request, "groups_form.html", {"form": form})


def groups(request):
    list_groups = Group.objects.all().order_by("-id")
    return render(request, "groups.html", context={"groups": list_groups})


# ДЗ 7. reverse, urls
def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupForm(instance=group)
        return render(request, "group_edit.html", {"form": form})
    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        form.save()
        return redirect("groups")
    return render(request, "group_edit.html", {"form": form})


def teacher_edit(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form})
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect("teachers")
    return render(request, "teacher_edit.html", {"form": form})


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        group.delete()
        return redirect("groups")
    return render(request, "group_confirm_delete.html", {"object": group})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect("teachers")
    return render(request, "teacher_confirm_delete.html", {"object": teacher})


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_form.html", {"form": form})
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("students")

    return render(request, "student_form.html", {"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_edit.html", {"form": form})
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("students")
    return render(request, "student_edit.html", {"form": form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("students")
    return render(request, "student_confirm_delete.html", {"object": student})
