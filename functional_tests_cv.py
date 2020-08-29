from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Chrome("./chromedriver")

    def tearDown(self):  
        self.browser.quit()

    def check_for_table_not_empty(self, id):
        table = self.browser.find_element_by_id(id)
        rows = table.find_elements_by_tag_name('tr')
        self.assertIsNotNone(rows)       

    def test_can_start_a_cv_and_retrieve_it_later(self):
        # check out the cv page
        self.browser.get('http://localhost:8000/cv')

        # notices the page title and header mention cv
        self.assertIn('Rio\'s cv', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('LingKi Chan', header_text)


        # check cv page is not empty
        self.check_for_table_not_empty('id_education_table')
        self.check_for_table_not_empty('id_workExperience_table')
        self.check_for_table_not_empty('id_skill_table')
        self.check_for_table_not_empty('id_achievement_table')

        # try to login
        inputbox = self.browser.find_element_by_id('login') 
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)
        inputbox = self.browser.find_element_by_id('id_username') 
        inputbox.send_keys('rio') 
        inputbox = self.browser.find_element_by_id('id_password') 
        inputbox.send_keys('rio') 
        inputbox = self.browser.find_element_by_id('submit') 
        inputbox.send_keys(Keys.ENTER) 
        time.sleep(1)

        # go back to cv after login
        self.browser.get('http://localhost:8000/cv')

        # try to add new work experience
        inputbox = self.browser.find_element_by_id('add_workExperience') 
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)

        # add new work experience
        inputbox = self.browser.find_element_by_id('id_job_title') 
        inputbox.send_keys('rubbish')
        inputbox = self.browser.find_element_by_id('id_company') 
        inputbox.send_keys('aunt\'s home')
        inputbox = self.browser.find_element_by_id('id_job_desc') 
        inputbox.send_keys('doing nothing, eat , and play games')
        inputbox = self.browser.find_element_by_id('id_start_date') 
        # clear default input to prevent error
        inputbox.clear()
        inputbox.send_keys('2020-08-29 02:06:07')
        inputbox = self.browser.find_element_by_id('id_finish_date') 
        inputbox.send_keys('2020-09-27 00:00:00')
        inputbox = self.browser.find_element_by_id('submit') 
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #The page updates again, and now shows new work experience on the cv
        table = self.browser.find_element_by_id('id_workExperience_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('@aunt\'s home', [row.text for row in rows])

        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there


if __name__ == '__main__':  
    unittest.main(warnings='ignore')