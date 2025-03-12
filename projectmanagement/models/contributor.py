from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from projectmanagement.models.address import Address

class ContributorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a regular user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a superuser with admin privileges."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Contributor(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    # Required fields for authentication
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ContributorManager()

    USERNAME_FIELD = 'email'  # Authentication will be done using email
    REQUIRED_FIELDS = ['fullName']

    def __str__(self):
        return f"{self.fullName} {self.email}"
