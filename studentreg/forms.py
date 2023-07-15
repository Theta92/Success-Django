from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Student


class RegisterForm(UserCreationForm):
    """Form definition for user and student registration."""

    class Meta:
        """Meta definition for Registerform."""

        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class StudentCreationForm(forms.ModelForm):
    """Form definition for Student."""

    course = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select Course",
        # widget=forms.Select(
        #     attrs={
        #         "class": FORM_CLASS_NAME,
        #         "id": "course",
        #     }
        # ),
    )

    gender = forms.ChoiceField(
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        )
    )

    class Meta:
        """Meta definition for Studentform."""

        model = Student
        fields = ("course", "gender")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class StudentProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        )
    )

    class Meta:
        """Meta definition for Studentform."""

        model = Student
        fields = (
            "date_of_birth",
            "gender",
            "address",
            "city",
            "country",
            "gender",
            "photo",
        )
