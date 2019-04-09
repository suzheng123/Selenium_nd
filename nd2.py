'''
read data from webinfo/userinfo files
log in a .txt file
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from nd2_getinfo import get_webinfo,get_userinfo
from test_log import Log_info

def openBrowser():			#open browser
	browser = webdriver.Firefox(executable_path='/Users/JacZh/Downloads/webdrivers/geckodriver')
	browser.set_window_size(920,650)
	return browser

def openUrl(browser, url):	#open url
	browser.get(url)

def findElement(browser, arg_dict): # find input fields
	# arg must be dict
	emailField = browser.find_element_by_name(arg_dict['email'])	
	pwdField = browser.find_element_by_name(arg_dict['pwd'])
	button = browser.find_element_by_css_selector(arg_dict['button'])

	return emailField,pwdField,button

def sendKeys(browser, ele_tuple, account_dict):	#send keys to input fields
	keys = ['useremail','userpwd']
	i = 0
	for key in keys:
		ele_tuple[i].send_keys('')
		ele_tuple[i].clear()
		ele_tuple[i].send_keys(account_dict[key])
		i+=1
	browser.implicitly_wait(5)
	ele_tuple[2].click()

def checkResult(browser,selector,account,log): #check whether account correct
	result = False
	browser.implicitly_wait(10)
	try:
		err = browser.find_element_by_css_selector(selector)
		print(err.text)
		msg = 'ERROR! -->%s: email: %s pwd:%s \n'%(err.text, account['useremail'],account['userpwd']) 
		log.log_write(msg)
	except:
		print('Done!')
		msg = 'Sucess! email: %s pwd: %s \n'%(account['useremail'],account['userpwd'])
		log.log_write(msg)
		result = True
	return result

def logout(browser,arg_dict): # log out
	user = browser.find_element_by_partial_link_text(data_dict['user_text']).click()
	logout = browser.find_element_by_partial_link_text(data_dict['logout_text']).click()


def login(data_dict,user_list):
	browser = openBrowser()
	log = Log_info() # log test info into to .txt file
	url_open = openUrl(browser, data_dict['url'])

	signin = browser.find_element_by_partial_link_text(data_dict['login_text']).click()
	signin2 = browser.find_element_by_css_selector('.Tg2rV').click()

	inputFields_tuple = findElement(browser, data_dict)

	for account in user_list:
		sendKeys(browser,inputFields_tuple,account)	
		browser.implicitly_wait(5)
		result = checkResult(browser, data_dict['error_selector'],account,log)
		if result == True:
			logout(browser,data_dict)
			inputFields_tuple = findElement(browser, data_dict)
	log.log_close() #close the log file

if __name__ == '__main__':
	url = 'https://shop.nordstrom.com/'
	login_text = 'Sign'

	data_dict = get_webinfo(r'nd2_webinfo')
	user_list = get_userinfo(r'/Users/JacZh/desktop/resources/pycharm_selenium/test1/nd3/nd2_userinfo')
	
	# user_list = [{'useremail':'jac@selenium.com', 'userpwd':'try123'}]


	login(data_dict,user_list)


