from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import pytz
from django.utils import timezone
from datetime import datetime

from cv.views import cv, addWorkExperience
from .forms import WorkExperienceForm

from django.template.loader import render_to_string

from cv.models import Education, Skill, WorkExperience, Achievement

from django.contrib.auth.models import User

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/cv/')  
        self.assertEqual(found.func, cv)
        
    def test_uses_home_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv_home.html')

class Add_workExperience_test(TestCase):
    
    def test_root_url_resolves_to_add_we_view(self):
        found = resolve('/addWE/')  
        self.assertEqual(found.func, addWorkExperience)
        
    def test_uses_add_we_template(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/addWE/')
        #self.assertRedirects(response, 'add_workExperience.html')
        self.assertTemplateUsed(response, 'add_workExperience.html')

    def test_can_save_a_POST_request(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')
        self.client.post('/addWE/', data={'job_title': 'rubbish',
                                          'company':'aunt\'s home',
                                          'job_desc':'doing nothing, eat , and play games',
                                          'start_date':'2020-08-29 02:06:07',
                                          'finish_date':'2020-09-27 00:00:00'})

        self.assertEqual(WorkExperience.objects.count(), 1)
        new_WorkExperience = WorkExperience.objects.first()
        self.assertEqual(new_WorkExperience.company, 'aunt\'s home')

    def test_redirects_after_POST(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/addWE/', data={'job_title': 'rubbish',
                                          'company':'aunt\'s home',
                                          'job_desc':'doing nothing, eat , and play games',
                                          'start_date':'2020-08-29 02:06:07',
                                          'finish_date':'2020-09-27 00:00:00'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')


class CvModelTest(TestCase):

    def test_saving_and_retrieving_data(self):
        hk_tz = pytz.timezone("Asia/Hong_Kong")
        uni = Education()
        uni.program_title = 'computer science'
        uni.organization = 'uob'
        uni.program_desc = 'study computer related stuff'
        uni.start_date = hk_tz.localize(datetime(2019,9,30))
        uni.finish_date = hk_tz.localize(datetime(2020,7,30))
        uni.save()

        secondary_school = Education()
        secondary_school.program_title = 'HKDSE'
        secondary_school.organization = 'pooitun'
        secondary_school.program_desc = 'study different foundation subjects'
        secondary_school.start_date = hk_tz.localize(datetime(2011,9,30))
        secondary_school.finish_date = hk_tz.localize(datetime(2017,7,30))
        secondary_school.save()

        saved_education = Education.objects.all()
        self.assertEqual(saved_education.count(), 2)

        first_saved_education = saved_education[0]
        second_saved_education = saved_education[1]
        self.assertEqual(first_saved_education.organization, 'uob')
        self.assertEqual(second_saved_education.organization, 'pooitun')


        python = Skill()
        python.skill_title = 'python'
        python.skill_area = 'programming'
        python.save()

        sql = Skill()
        sql.skill_title = 'sql'
        sql.skill_area = 'database mangement'
        sql.save()

        saved_skill = Skill.objects.all()
        self.assertEqual(saved_skill.count(), 2)

        first_saved_skill = saved_skill[0]
        second_saved_skill = saved_skill[1]
        self.assertEqual(first_saved_skill.skill_title, 'python')
        self.assertEqual(second_saved_skill.skill_title, 'sql')

        qbs = WorkExperience()
        qbs.job_title = 'DataScienceIntern'
        qbs.company = 'qbs'
        qbs.job_desc = 'car plate regconition project'
        qbs.start_date = hk_tz.localize(datetime(2018,8,1))
        qbs.finish_date = hk_tz.localize(datetime(2018,8,30))
        qbs.save()

        saved_job = WorkExperience.objects.all()
        self.assertEqual(saved_job.count(), 1)

        first_saved_job = saved_job[0]
        self.assertEqual(first_saved_job.company, 'qbs')

        ashf = Achievement()
        ashf.achievement_title = 'ashf'
        ashf.achievement_desc = 'scholar'
        ashf.achieve_date = hk_tz.localize(datetime(2019,5,17))
        ashf.save()

        saved_achievement = Achievement.objects.all()
        self.assertEqual(saved_achievement.count(), 1)

        first_saved_achievement = saved_achievement[0]
        self.assertEqual(first_saved_achievement.achievement_title, 'ashf')
        self.assertEqual(first_saved_achievement.achievement_desc, 'scholar')
        self.assertEqual(first_saved_achievement.achieve_date, hk_tz.localize(datetime(2019,5,17)))


