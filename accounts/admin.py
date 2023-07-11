from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import TeacherCreateForm, TeacherChangeForm
from .models import Teacher


# Register your models here.

class TeacherAdmin(UserAdmin):
    add_form = TeacherCreateForm
    form = TeacherChangeForm
    model = Teacher


admin.site.register(Teacher)
