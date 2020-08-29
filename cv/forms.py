from django import forms

from .models import WorkExperience

class WorkExperienceForm(forms.ModelForm):
	

    class Meta:
        model = WorkExperience
        fields = ('job_title', 'company','job_desc','start_date','finish_date')