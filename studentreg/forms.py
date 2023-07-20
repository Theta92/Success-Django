from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Student

# Form for new user registration
class RegisterForm(UserCreationForm):
    """Form definition for user/student registration."""

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "inputField",
                "id": "Username",
            }
        ),
    )

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "inputField",
                "id": "First Name",
            }
        ),
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "inputField",
                "id": "Last Name",
            }
        ),
    )
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "inputField",
                "id": "Email",
            }
        ),
    )

    password1 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "inputField",
                "id": "Password",
            }
        ),
    )

    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "inputField",
                "id": "Password2",
            }
        ),
    )

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "inputField",
                "id": "Username",
            }
        ),
    )

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "inputField",
                "id": "First Name",
            }
        ),
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "inputField",
                "id": "Last Name",
            }
        ),
    )
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "inputField",
                "id": "Email",
            }
        ),
    )

    password1 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "inputField",
                "id": "Password",
            }
        ),
    )

    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "inputField",
                "id": "Password2",
            }
        ),
    )

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
        widget=forms.Select(
            attrs={
                "placeholder": "courses",
                "class": "inputField",
                "id": "Courses",
            }
        ),
    )

    gender = forms.ChoiceField(
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ),
        widget=forms.Select(
            attrs={
                "id": "gender",
                "class": "inputField",
                "placeholder": "gender",
            }
        ),
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

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={
                    "id": "date_of_birth",
                    "placeholder": "DD-MM-YYYY",
                    "type": "date",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "id": "address",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "id": "city",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "id": "country",
                }
            ),
            "photo": forms.FileInput(
                attrs={
                    "id": "photo",
                }
            ),
        }
