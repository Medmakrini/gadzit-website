from django.contrib import admin

from .models import Formation

# Register your models here.

class FormationAdmin(admin.ModelAdmin):
    list_display=('email','first_name','last_name','choices')


admin.site.register(Formation,FormationAdmin)