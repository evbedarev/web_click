# coding: utf8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.chrome.options import Options
import datetime
import subprocess
import pgup
import user_agent
import change_res

class find_and_click():
	elm_ya=[]
	b=[]
	# print_text = ""
	def __init__(self,text_find,num_link,driver):

		self.elm_ya = driver.find_elements_by_class_name("geolink")

		self.elm_ya[0].click()
		time.sleep(random.random()+random.random()+random.random())

		self.elm_ya = driver.find_elements_by_class_name("checkbox__control")

		self.elm_ya[0].click()
		time.sleep(random.random()+random.random()+random.random())

		self.elm_ya = driver.find_elements_by_class_name("input__control")
		self.print_t(u"Санкт-Петербург",0)

		time.sleep(random.random()+random.random()+random.random())
		self.elm_ya[0].send_keys(Keys.RETURN)
		time.sleep(random.random()+random.random()+random.random())
		time.sleep(3)

		self.elm_ya = driver.find_elements_by_class_name("input__control")
		# self.print_text = text_find
		self.print_t(text_find,3)
		time.sleep(3+random.random()+random.random()+random.random())
		print(driver.current_url)
		# self.link_by_name("pythontutor",driver)
		# self.five_links(driver,6,3)
		time.sleep(3+random.random()+random.random()+random.random())
		d = []
		d = driver.find_elements_by_class_name("pager__item_kind_page")
		time.sleep(3+random.random()+random.random()+random.random())
		d[2].click()
		time.sleep(3+random.random()+random.random()+random.random())
		print(driver.current_url)
		self.link_by_name("9colours",driver)


	def print_t(self,str_text,list_i):
		words = []
		[words.append(i) for i in str_text]
		for i in words:
			self.elm_ya[list_i].send_keys(i)
			time.sleep(random.random()+0.2)
		self.elm_ya[list_i].send_keys(Keys.RETURN)


	def link_by_name(self,site_name,driver):
		my_link = driver.find_elements_by_xpath("//*[contains(text(), ' / 9colours.ru')]")
		my_link[0].click()
		time.sleep(2)
##		for i in self.elm_ya:
##                        print(i.get_attribute('href'))
##		self.five_links(driver,1,2)
		time.sleep(2)
##		for i in self.elm_ya:
##			if site_name in i.get_attribute('href'):
##                i.click()
                time.sleep(3+random.random())
                print(driver.current_url)
                self.change_web(1,driver)
                time.sleep(random.random()+1)
                self.find_links(driver)
                time.sleep(2+random.random())
                self.find_links(driver)
##                break

					
	def five_links(self,driver,num_srch,num_links):
		self.elm_ya = []
		self.elm_ya = driver.find_elements_by_class_name("organic__url")
		for i in range(0,num_srch):
			self.change_web(0,driver)
			self.elm_ya[i].click()
			time.sleep(random.randint(2,4)+random.random())
			self.change_web(1,driver)
			time.sleep(1+random.random())
			for i in range(1,num_links):
				self.find_links(driver)
			self.close_tab(1,driver)
			time.sleep(random.randint(2,4)+random.random())


	def change_web(self,num_windows,driver):
		driver.switch_to_window(driver.window_handles[num_windows])
		time.sleep(1)
		self.logs(driver.current_url)
		print(driver.current_url)
		return driver

	def find_links(self,driver):
		links=[]
		vis_links=[]
		links=driver.find_elements_by_xpath("//*[@href]")
		print(links.__len__())
		for i in range(1,links.__len__()):
			if links[i].is_displayed():
				print("Element found: ")
				vis_links.append(links[i])
				if i > 50:
					break
			else:
				print("element not found")
		self.go_links(vis_links,driver)


	def go_links(self,vis_links,driver):
		rand_slp = random.randint(1,4) + random.random()
		if vis_links.__len__() > 0:
			rand_link = random.randint(0,vis_links.__len__())
			ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
			time.sleep(rand_slp)
			vis_links[rand_link].send_keys(Keys.CONTROL + Keys.RETURN)
			time.sleep(1+random.random())
			ActionChains(driver).send_keys(Keys.CONTROL+'3').perform()
			time.sleep(1+random.random())
			driver = self.change_web(2,driver)
			if pgup.main():
				#################
				# self.UserPg(driver)
				# time.sleep(1+random.randint(60,120)) #Поменять время
				self.close_tab(2,driver)
				ActionChains(driver).send_keys(Keys.CONTROL+'2').perform()
				time.sleep(1+random.random())


	def close_tab(self,num_tab,driver):
		driver.close()
		time.sleep(1+random.random())
		driver.switch_to_window(driver.window_handles[num_tab-1])


	def logs(self,text):
		f = open('c:\log_py.txt','a')
		f.write(str(datetime.datetime.now())+' ' + text+'\n')
		f.close()


def logs(text):
	f = open('c:\log_py.txt','a')
	f.write(str(datetime.datetime.now())+' ' + text+'\n')
	f.close()

logs(change_res.changeScr())
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent="+user_agent.user_agent())
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.delete_all_cookies()
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://yandex.ru/")
time.sleep(2)
# try:
a = find_and_click(u"Где живет косметика спб",4,driver)
# except Exception:
# a.change_web(1,driver)
	# win_cmd = 'shutdown /r /t 0'
	# process = subprocess.Popen(win_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# time.sleep(5)
# a.go_links(1,driver)

