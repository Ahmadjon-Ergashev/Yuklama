from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, CheckboxSelectMultiple, ModelMultipleChoiceField, DateField, DateInput
from .models import Science, Particle, Major, Particle_Teacher
from accounts.models import Teacher


class ScienceCreateForm(ModelForm):
    class Meta:
        model = Science
        fields = ('name',)
        labels = {
            'name': _('Nomi'),
        }

class ParticleForm(ModelForm):
    class Meta:
        model = Particle
        fields = ('science', 'majors', 'flow', 'group', 'student_count', 'language', 'course', 'semester', 'lecture', 'practice', 'laboratory', 'seminar', 'coursework')
        labels = {
            'science': _('Fan'),
            'majors': _('Yo\'nalish'),
            'flow': _('Potok'),
            'group': _('Guruhlar'),
            'student_count': _('Talaba soni'),
            'language': _('Til'),
            'course': _('Kurs'),
            'semester': _('Semestr'),
            'lecture': _('Ma\'ruza'),
            'practice': _('Amaliyot'),
            'laboratory': _('Laboratoriya'),
            'seminar': _('Seminar'),
            'coursework': _('Kurs ishi'),
        }

class ParticleCreateForm(ModelForm):
    class Meta:
        model = Particle
        fields = ('science', 'majors', 'student_count', 'flow', 'group', 'language', 'course', 'semester', 'lecture', 'practice', 'laboratory', 'seminar', 'coursework')
        labels = {
            'science': _('Fan'),
            'majors': _('Yo\'nalish'),
            'flow': _('Potok'),
            'group': _('Guruhlar'),
            'student_count': _('Talaba soni'),
            'language': _('Til'),
            'course': _('Kurs'),
            'semester': _('Semestr'),
            'lecture': _('Ma\'ruza'),
            'practice': _('Amaliyot'),
            'laboratory': _('Laboratoriya'),
            'seminar': _('Seminar'),
            'coursework': _('Kurs ishi'),
        }
    majors = ModelMultipleChoiceField(
        label='Yo\'nalishlar',
        queryset=Major.objects.all(),
        widget=CheckboxSelectMultiple
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['science'].empty_label = None
        self.fields['language'].empty_label = None


class ParticleChangeForm(ModelForm):
    class Meta:
        model = Particle
        fields = ('science', 'majors', 'student_count', 'flow', 'group',  'language', 'course', 'semester', 'lecture', 'practice', 'laboratory', 'seminar', 'coursework')
        labels = {
            'science': _('Fan'),
            'majors': _('Yo\'nalish'),
            'flow': _('Potok'),
            'group': _('Guruhlar'),
            'student_count': _('Talaba soni'),
            'language': _('Til'),
            'course': _('Kurs'),
            'semester': _('Semestr'),
            'lecture': _('Ma\'ruza'),
            'practice': _('Amaliyot'),
            'laboratory': _('Laboratoriya'),
            'seminar': _('Seminar'),
            'coursework': _('Kurs ishi'),
        }
    majors = ModelMultipleChoiceField(
        label='Yo\'nalishlar',
        queryset=Major.objects.all(),
        widget=CheckboxSelectMultiple
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['science'].empty_label = None
        self.fields['language'].empty_label = None

class ParticleTeacherCreateForm(ModelForm):
    class Meta:
        model = Particle_Teacher
        fields = ('teacher', 'student_count', 'flow', 'group', 'language', 'semester', 'lecture', 'practice', 'laboratory', 'seminar', 'coursework', 'raiting')
        labels = {
            'teacher': _('O\'qituvchi'),
            'student_count': _('Talabalar soni'),
            'flow': _('Potok'),
            'group': _('Guruhlar'),
            'language': _('Til'),
            'semester': _('Semestr'),
            'lecture': _('Ma\'ruza'),
            'practice': _('Amaliyot'),
            'laboratory': _('Laboratoriya'),
            'seminar': _('Seminar'),
            'coursework': _('Kurs ishi'),
            'raiting': _('Reyting'),
        }
    # majors = ModelMultipleChoiceField(
    #     label='Yo\'nalishlar',
    #     queryset=Major.objects.all(),
    #     widget=CheckboxSelectMultiple
    # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['teacher'].queryset = Teacher.objects.filter(sciences = 1, is_active = 1)

        self.fields['teacher'].empty_label = None
        self.fields['language'].empty_label = None