from django.db import models
from django.urls import reverse

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name


class Science(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("sciences")

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Particle(models.Model):
    science = models.ForeignKey(to=Science, on_delete=models.CASCADE)
    majors = models.ManyToManyField(to=Major, related_name='particle_majors')
    student_count = models.PositiveSmallIntegerField(null=False)
    flow = models.PositiveSmallIntegerField(null=False)
    group = models.PositiveSmallIntegerField(null=False)
    course = models.PositiveSmallIntegerField(null=False, default=1)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(null=False, default=2)
    lecture = models.PositiveSmallIntegerField(null=False, default=30)
    practice = models.PositiveSmallIntegerField(null=False, default=30)
    laboratory = models.PositiveSmallIntegerField(null=False, default=0)
    seminar = models.PositiveSmallIntegerField(null=False, default=0)
    coursework = models.PositiveSmallIntegerField(null=False, default=0)

    def __str__(self):
        return str(self.science)

    def get_absolute_url(self):
        return reverse("particles")

class Particle_Teacher(models.Model):
    teacher = models.ForeignKey(to='accounts.Teacher', on_delete=models.CASCADE)
    particle = models.ForeignKey(to=Particle, on_delete=models.CASCADE, related_name='teachers')
    student_count = models.PositiveSmallIntegerField(null=False)
    flow = models.PositiveSmallIntegerField(null=False)
    group = models.PositiveSmallIntegerField(null=False)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(null = False)
    lecture = models.PositiveSmallIntegerField(null=False, default=0)
    practice = models.PositiveSmallIntegerField(null=False, default=0)
    laboratory = models.PositiveSmallIntegerField(null=False, default=0)
    seminar = models.PositiveSmallIntegerField(null=False, default=0)
    coursework = models.PositiveSmallIntegerField(null=False, default=0)
    raiting = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return self.teacher
    
    def get_absolute_url(self):
        return reverse('particle_teachers', kwargs={"pk": self.particle_id})
        # return reverse("particles", kwargs={"pk": self.pk})
    