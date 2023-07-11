from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django import forms
from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField
from django.utils.translation import gettext_lazy as _
from .models import Teacher
from main.models import Science
    

class TeacherCreateForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Parol"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=None,
    )
    password2 = forms.CharField(
        label=_("Parol qayta"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=None,
    )
    class Meta:
        model = Teacher
        fields = ('last_name', 'first_name', 'position', 'degree', 'main_stage', 'addition_stage', 'per_hour', 'phone', 'gender',
                  'birth', 'sciences')
        labels = {
            'first_name': _('Ismi'),
            'last_name': _('Familiyasi'),
            'position': _('Lavozimi'),
            'degree': _('Ilmiy daraja'),
            'main_stage': _('Asosiy shtat'),
            'addition_stage': _('O\'rindosh shtat'),
            'per_hour': _('Soatbay'),
            'phone': _('Telefon'),
            'gender': _('Jins'),
            'birth': _('Tug\'ilgan sana'),
            'sciences': _('Fanlar'),
        }
    sciences = ModelMultipleChoiceField(
        label='Fanlar',
        queryset=Science.objects.all(),
        widget=CheckboxSelectMultiple,
    )
    def __init__(self, *args, **kwargs):
        super(TeacherCreateForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = None
        self.fields['degree'].empty_label = None
        self.fields['gender'].empty_label = None


class TeacherChangeForm(UserChangeForm):
    class Meta:
        model = Teacher
        fields = ('last_name', 'first_name', 'position', 'degree', 'main_stage', 'addition_stage', 'per_hour', 'phone', 'gender',
                  'birth', 'sciences')
        labels = {
            'first_name': _('Ismi'),
            'last_name': _('Familiyasi'),
            'position': _('Lavozimi'),
            'degree': _('Ilmiy daraja'),
            'main_stage': _('Asosiy shtat'),
            'addition_stage': _('O\'rindosh shtat'),
            'per_hour': _('Soatbay'),
            'phone': _('Telefon'),
            'gender': _('Jins'),
            'birth': _('Tug\'ilgan sana'),
            'sciences': _('Fanlar'),
        }
    sciences = ModelMultipleChoiceField(
        label='Fanlar',
        queryset=Science.objects.all(),
        required = False,
        widget=CheckboxSelectMultiple,
    )
    password = None
    def __init__(self, *args, **kwargs):
        super(TeacherChangeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = None
        self.fields['degree'].empty_label = None
        self.fields['gender'].empty_label = None
