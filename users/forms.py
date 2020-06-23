from django_registration.forms import RegistrationForm  # pip install django_registration
from users.models import CustomUser


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
