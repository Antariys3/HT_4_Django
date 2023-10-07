from datetime import date, timedelta

from django import forms
from django.core.exceptions import ValidationError

from .management.commands.generate_teachers import ext_word_list
from .models import Teacher


class TeacherForm(forms.Form):
    first_name = forms.CharField(
        label="Имя преподавателя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        label="Фамилия преподавателя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    subject = forms.ChoiceField(
        label="Предмет",
        choices=[(subject, subject) for subject in ext_word_list],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]

        if not str(first_name).isalpha():
            raise ValidationError("Имя не должно содержать цифры или символы.")
        elif len(first_name) > 20:
            raise ValidationError("Имя не должно быть больше 20 символов.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]

        if not str(last_name).isalpha():
            raise ValidationError("Фамилия не должна содержать цифры или символы.")
        elif len(last_name) > 20:
            raise ValidationError("Фамилия не должна быть больше 20 символов.")
        return last_name

    def clean_birth_date(self):
        birth_date = self.cleaned_data["birth_date"]
        today = date.today()
        min_age = timedelta(days=365 * 18)
        max_age = timedelta(days=365 * 65)
        if not min_age <= (today - birth_date) <= max_age:
            raise ValidationError("Учитель должен быть в возрасте от 18 до 65 лет.")
        return birth_date


class GroupForm(forms.Form):
    name = forms.CharField(
        label="Название группы",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    curator = forms.ModelChoiceField(
        label="Куратор",
        queryset=Teacher.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean_name(self):
        name = self.cleaned_data["name"]

        if len(name) > 10:
            raise forms.ValidationError(
                "Название группы не должно быть больше 10 символов."
            )
        return name

    def clean_curator(self):
        curator = self.cleaned_data["curator"]

        if len(str(curator)) > 50:
            raise forms.ValidationError(
                "Имя куратора не должно быть больше 50 символов."
            )
        return curator
