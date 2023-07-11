from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from .forms import TeacherCreateForm, TeacherChangeForm
from .models import Teacher


# Create your views here.

class TeacherView(ListView):
    model = Teacher
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Teacher.objects.filter(is_active = True)
        return context

class DeactivatedTeachersView(ListView):
    model = Teacher
    template_name = 'archive_teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Teacher.objects.filter(is_active = False)
        return context


class TeacherEditView(UpdateView):
    model = Teacher
    form_class = TeacherChangeForm
    template_name = 'teacher_edit.html'


# class TeacherCreateView(CreateView):
#     model = Teacher
#     template_name = 'teacher_create.html'
#     form_class = TeacherCreateForm

def TeacherCreateView(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST or None)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.save()
            form.save_m2m() # save m2m after meal has id
            return redirect('teachers')
    else:
        form = TeacherCreateForm()
    return render(request, 'teacher_create.html', context={'form': form})
    

class TeacherDeActivateView(UpdateView):
    model = Teacher
    fields = ()
    template_name = 'teacher_deactivate.html'

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)