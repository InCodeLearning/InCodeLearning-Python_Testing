import unittest
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ePO_login(unittest.TestCase):

    """
    This sample exercise the explicit wait function
    The ExpectedConditions are listed below:
    prerequsite: my_email and password must be registered at manage.mcafee.com

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable - it is Displayed and Enabled.
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
    """

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://manage.mcafee.com")
        assert "Log On" in driver.title
        elem = driver.find_element_by_id('logOnEmailAddress')
        elem.clear()
        elem.send_keys('my@email.com')
        elem = driver.find_element_by_id('logOnPassword')
        elem.clear()
        elem.send_keys('password')
        elem = driver.find_element_by_id('logOnButton')
        elem.click()
        # time.sleep(10) # implicit wait
        # explicit wait EC.presence_of_element
        try:
            element = WebDriverWait(driver, 20).until(
               EC.presence_of_element_located((By.ID, "mfaTitle"))
            )
        except IOError as e:
            print("I/O errors({0}): {1}".format(e.errorno, e.strerror))
        except ValueError:
            print("Value Error")
        except:
            print("Unexpected error (can't find the control)")
        finally:
            pass

        elem = driver.find_element_by_xpath("//*[text()='Dashboards']")
        elem.click()
        # explicit wait EC.text_to_be_present
        try:
            element = WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element_value
                ((By.ID, "mfaTitle"), 'Dashboards')
            )
        except IOError as e:
            print("I/O errors({0}): {1}".format(e.errorno, e.strerror))
        except ValueError:
            print("Value Error")
        except:
            print("Unexpected error (can't find the control)")
        finally:
            pass

        elem = driver.find_element_by_xpath("//*[text()='Getting Started']")
        elem.click()
        elem = driver.find_element_by_xpath("//*[text()='Systems']")
        elem.click()
        elem = driver.find_element_by_xpath("//*[text()='Queries & Reports']")
        elem.click()

        assert "ePolicy" in driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()

__author__ = 'mpsauto'
