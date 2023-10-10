from django.urls import path

from st_app.views import (
    index,
    generate_student,
    generate_students,
    students,
    teacher_form,
    teachers,
    group_form,
    groups,
    group_edit,
    teacher_edit,
    group_delete,
    teacher_delete,
    student_form,
    student_edit,
    student_delete,

)

urlpatterns = [
    path("", index, name="home"),
    path("generate-student/", generate_student, name="generate_student"),
    path("students/", students, name="students"),
    path("generate-students/", generate_students, name="generate_students"),
    path("teacher/", teacher_form, name="teacher"),
    path("teachers/", teachers, name="teachers"),
    path("group/", group_form, name="group"),
    path("groups/", groups, name="groups"),
    path("group/<int:pk>/", group_edit, name="group_edit"),
    path("teacher/<int:pk>/", teacher_edit, name="teacher_edit"),
    path('teacher/<int:pk>/delete/', teacher_delete, name='teacher_delete'),
    path('group/<int:pk>/delete/', group_delete, name='group_delete'),
    path("student/", student_form, name="student"),
    path("student/<int:pk>/", student_edit, name="student_edit"),
    path('student/<int:pk>/delete/', student_delete, name='student_delete'),
]
