from django.contrib import admin
from .models import JobType



class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','exceution_time']
    search_fields = ['name']


admin.site.register(JobType,JobTypeAdmin)
