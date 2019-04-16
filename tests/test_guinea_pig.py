import pytest
import time


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_link(self, driver, record_xml_attribute):
        record_xml_attribute("classname", "custom_classname")
        record_xml_attribute("name", "custom_name")
        """
        Verify page title change when link clicked
        :return: None
        """
        driver.get('https://saucelabs-sample-test-frameworks.github.io/training-test-page')


        start = time.time()
        end = time.time()
        while end - start < 1500:
            driver.find_element_by_id("i_am_a_link").click()
            end = time.time()

        title = "I am another page title - Sauce Labs"
        assert title == driver.title


    def test_comment(self, driver):
        """
        Verify comment submission
        :return: None
        """
        driver.get('https://saucelabs-sample-test-frameworks.github.io/training-test-page')
        sample_text = "hede@hodo.com"
        email_text_field = driver.find_element_by_id("comments")
        email_text_field.send_keys(sample_text)

        start = time.time()
        end = time.time()
        while end - start < 1500:
            driver.find_element_by_id("submit").click()
            end = time.time()
        

        text = driver.find_element_by_id("your_comments").text
        assert sample_text in text
