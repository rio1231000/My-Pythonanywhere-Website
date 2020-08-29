from django.db import models
from django.utils import timezone


class Education(models.Model):
    program_title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    program_desc = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.program_title

    def start_date_without_time(self):
        return self.start_date.strftime('%B %d %Y')

    def finish_date_without_time(self):
        return self.finish_date.strftime('%B %d %Y')

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    job_desc = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.job_title

    def start_date_without_time(self):
        return self.start_date.strftime('%B %d %Y')

    def finish_date_without_time(self):
        return self.finish_date.strftime('%B %d %Y')

class Skill(models.Model):
    skill_title = models.CharField(max_length=200)
    skill_area = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_title

class Achievement(models.Model):
    achievement_title = models.CharField(max_length=200)
    achievement_desc = models.TextField()
    achieve_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.achievement_title

    def achieve_date_without_time(self, date_time):
        return self.achieve_date.strftime('%B %d %Y')