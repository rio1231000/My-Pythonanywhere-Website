from django.contrib import admin
from .models import Education, Skill, WorkExperience, Achievement

# Register your models here.
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Achievement)