from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db.models import Sum, Count
from django.views.generic import ListView, UpdateView, CreateView, TemplateView, DeleteView
from .models import Science,  Particle, Particle_Teacher
from accounts.models import Teacher
from .forms import (
    ScienceCreateForm,
    ParticleForm,
    ParticleCreateForm,
    ParticleChangeForm,
    ParticleTeacherCreateForm,
)


# home
class HomeView(TemplateView):
    template_name = 'home.html'


# Sciences
class ScienceView(ListView):
    model = Science
    template_name = 'sciences.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Science.objects.filter(is_active = True)
        return context


class ScienceEditView(UpdateView):
    model = Science
    template_name = 'science_edit.html'
    fields = [
        'name',
    ]


class ScienceCreateView(CreateView):
    model = Science
    template_name = 'science_create.html'
    form_class = ScienceCreateForm


class DeactivatedSciencesView(ListView):
    model = Science
    template_name = 'archive_sciences.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Science.objects.filter(is_active = False)
        return context


class ScienceDeActivateView(UpdateView):
    model = Science
    fields = ()
    template_name = 'science_deactivate.html'

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


#Particles
class ParticleView(ListView):
    model = Particle
    template_name = 'particle.html'
    is_complete = {}
    particle_list = {}
    form_class = ParticleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        list_id = []
        self.is_complete = {}
        self.particle_list = {}
        for obj in Particle.objects.all():
            list_id.append(obj.pk)
            self.is_complete[obj.pk] = None
            self.particle_list[obj.pk] = [
                obj.lecture, obj.practice, obj.laboratory, obj.seminar, obj.coursework]
        for i in list_id:
            temp = Particle_Teacher.objects.filter(particle_id=i).values('particle_id').annotate(Sum('lecture')).annotate(
                Sum('practice')).annotate(Sum('laboratory')).annotate(Sum('seminar')).annotate(Sum('coursework'))
            obj = Particle.objects.get(pk=i)
            if (len(temp)):
                self.is_complete[i] = (temp[0]['lecture__sum']) == obj.lecture and (temp[0]['practice__sum']) == obj.practice and \
                    (temp[0]['laboratory__sum']) == obj.laboratory and (temp[0]['seminar__sum']) == obj.seminar and \
                    (temp[0]['coursework__sum']) == obj.coursework
                self.particle_list[i][0] -= temp[0]['lecture__sum']
                self.particle_list[i][1] -= temp[0]['practice__sum']
                self.particle_list[i][2] -= temp[0]['laboratory__sum']
                self.particle_list[i][3] -= temp[0]['seminar__sum']
                self.particle_list[i][4] -= temp[0]['coursework__sum']

        context['is_complete'] = self.is_complete
        context['particle_list'] = self.particle_list
        return context


class ParticleCreateView(CreateView):
    model = Particle
    template_name = 'particle_create.html'
    form_class = ParticleCreateForm


class ParticleChangeView(UpdateView):
    model = Particle
    template_name = 'particle_edit.html'
    form_class = ParticleChangeForm


class ParticleDeleteView(DeleteView):
    model = Particle
    template_name = 'particle_delete.html'

    def get_success_url(self):
        return reverse_lazy('particles')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Particle.objects.get(pk=self.kwargs['pk'])
        return context


#ParticleTeachers
class ParticleTeachersView(ListView):
    model = Particle_Teacher
    template_name = 'particle_teachers.html'
    is_complete = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Particle_Teacher.objects.filter(
            particle_id=self.kwargs['pk'])
        context['particle'] = Particle.objects.get(id=self.kwargs['pk'])
        temp = context['object_list'].values('particle_id').annotate(Sum('lecture')).annotate(Sum(
            'practice')).annotate(Sum('laboratory')).annotate(Sum('seminar')).annotate(Sum('coursework'))
        obj = context['particle']
        if (len(temp)):
            self.is_complete = (temp[0]['lecture__sum']) == obj.lecture and (temp[0]['practice__sum']) == obj.practice and \
                (temp[0]['laboratory__sum']) == obj.laboratory and (temp[0]['seminar__sum']) == obj.seminar and \
                (temp[0]['coursework__sum']) == obj.coursework
        context['is_complete'] = self.is_complete
        return context


class ParticleTeacherCreateView(CreateView):
    model = Particle_Teacher
    template_name = 'particle_teacher_create.html'
    form_class = ParticleTeacherCreateForm

    
    def get_context_data(self, **kwargs):
        default_values = Particle.objects.get(pk=self.kwargs['pk'])
        temp = Particle_Teacher.objects.filter(particle_id=self.kwargs['pk']).values('particle_id').annotate(Sum('lecture')).annotate(
                Sum('practice')).annotate(Sum('laboratory')).annotate(Sum('seminar')).annotate(Sum('coursework'))[0]
        default_values.lecture -= temp['lecture__sum']
        default_values.practice -= temp['practice__sum']
        default_values.laboratory -= temp['laboratory__sum']
        default_values.seminar -= temp['seminar__sum']
        default_values.coursework -= temp['coursework__sum']

        context = super().get_context_data(**kwargs)
        context['default_values'] = default_values
        context['recommended_teachers'] = Teacher.object.filter(is_active = 1, sciences = self.kwargs['pk'])
        context['other_teachers'] = Teacher.object.filter(is_active = 1).exclude(sciences = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.particle_id = self.kwargs['pk']
        return super().form_valid(form)


class ParticleTeacherDeleteView(DeleteView):
    model = Particle_Teacher
    template_name = 'particle_teacher_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Particle_Teacher.objects.get(pk=self.kwargs['pk'])
        context['title'] = "Ushbu ma'lumotli yuklama taqsimoti o'chirilsinmi?"
        return context

    def get_success_url(self):
        if len(Particle_Teacher.objects.filter(particle_id=self.kwargs['id'])) > 1:
            return reverse_lazy('particle_teachers', kwargs={'pk': self.kwargs['id']})
        else:
            return reverse_lazy('particles')


#SelfParticles
class SelfParticleView(ListView):
    template_name = 'self_particles.html'
    model = Particle_Teacher

    def get_userId(self, **kwargs):
        return self.request.user.pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Particle_Teacher.objects.filter(
            teacher_id=self.get_userId())
        return context


class SelfParticleDeleteView(DeleteView):
    model = Particle_Teacher
    template_name = 'particle_teacher_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Particle_Teacher.objects.get(pk=self.kwargs['pk'])
        context['title'] = "Ushbu ma'lumotli yuklama taqsimoti o'chirilsinmi?"
        return context

    def get_success_url(self):
        return reverse_lazy('self_particles')


#Archive
class ArchiveView(TemplateView):
    template_name = 'archive.html'


#Setting
class SettingsView(TemplateView):
    template_name = 'settings.html'