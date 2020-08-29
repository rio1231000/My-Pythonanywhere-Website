from django.shortcuts import render, redirect
from cv.models import Education, Skill, WorkExperience, Achievement
from django.contrib.auth.decorators import login_required
from .forms import WorkExperienceForm

# Create your views here.

def cv(request):
	educations = Education.objects.all()
	workExperiences = WorkExperience.objects.all()
	skills = Skill.objects.all()
	achievements = Achievement.objects.all()
	return render(request, 'cv_home.html', {'educations': educations,
											'workExperiences': workExperiences,
											'skills': skills,
											'achievements': achievements})

@login_required
def addWorkExperience(request):
	if request.method == "POST":
		form = WorkExperienceForm(request.POST)
		if form.is_valid():
			new_workExperience = form.save(commit=False)
			new_workExperience.save()
			return redirect('/cv/')
		else:
			status = "Invalid input !!!"
	else:
		form = WorkExperienceForm()
		status=''
	return render(request, 'add_workExperience.html', {'form': form,
													   'status': status})