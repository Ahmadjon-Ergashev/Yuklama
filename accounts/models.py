from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.urls import reverse
from main.models import Position, Degree, Gender, Science
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        self.phone = phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

class Teacher(AbstractUser):
    username = None
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE, null=True)
    degree = models.ForeignKey(to=Degree, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=13, null=False, blank=True, unique=True)
    gender = models.ForeignKey(to=Gender, on_delete=models.CASCADE, null=True)
    birth = models.DateField(max_length=10, null=True)
    sciences = models.ManyToManyField(Science, related_name='teacher_sciences', blank=True)
    main_stage = models.PositiveSmallIntegerField(null=True, default=1)
    addition_stage = models.PositiveSmallIntegerField(null=True, default=0)
    per_hour = models.PositiveSmallIntegerField(null=True, default=0)
    

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
       
    object = UserManager()

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse("teachers")
