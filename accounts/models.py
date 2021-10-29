from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class AccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, date_of_birth, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_staff') is not True:
            return ValueError(_("Superuser must be assigned to is_staff=True."))

        if other_fields.get('is_superuser') is not True:
            return ValueError(_("is superuser must be assigned to is_superuser=True."))

        return self.create_user(email, password, date_of_birth, **other_fields)

    def create_user(self, email, first_name, last_name, password, date_of_birth, **other_fields):
        # How can i set user type flag ?

        if not email:
            return ValueError(_("You must provide an email address."))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, date_of_birth=date_of_birth, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    is_factory_manager = models.BooleanField(default=False)
    is_dealer_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    first_name = models.CharField(
        _("Your first name"), blank=False, max_length=30)
    last_name = models.CharField(
        _("Your last name"), blank=False, max_length=30)
    date_of_birth = models.DateField(blank=False)
    email = models.EmailField(_("email address"), unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name']
    objects = AccountManager()

    def __str__(self):
        return self.first_name + self.last_name
