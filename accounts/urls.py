from django.urls import path
from .views import (
    TeacherView, 
    TeacherEditView, 
    TeacherCreateView, 
    TeacherDeActivateView,
    DeactivatedTeachersView,
)

urlpatterns = [
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('teachers/create/', TeacherCreateView, name='teacher_create'),
    path('teachers/<int:pk>/edit/', TeacherEditView.as_view(), name='teacher_edit'),
    path('teachers/<int:pk>/archive/', TeacherDeActivateView.as_view(), name='teacher_deactivate'),
    path('archive/teachers/', DeactivatedTeachersView.as_view(), name='deactivated_teachers')
]
