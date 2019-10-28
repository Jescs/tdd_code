from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')
        # 她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)
        # 页面再次更新，她的清单中显示了这两个待办事项
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('finish the test!')
    #
    # def test_uses_home_template(self):
    #     response = self.browser.get('/')
    #     self.assertTupleEqual(response, 'home.html')
    #
    # def test_can_save_a_POST_request(self):
    #     response = self.browser.post('/', data={'item_text':'A new list item'})
    #     self.assertIn('A new list item', response.content.decode())
    #     self.assertTupleEqual(response, 'home.html')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
