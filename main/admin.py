from django.contrib import admin
from .models import (
    Science, 
    Degree, 
    Position, 
    Language, 
    Major, 
    Gender,
    )

# Register your models here.

admin.site.register(Science)
admin.site.register(Degree)
admin.site.register(Position)
admin.site.register(Language)
admin.site.register(Major)
admin.site.register(Gender)
