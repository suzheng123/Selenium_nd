# webinfoPath=(r'/Users/JacZh/desktop/resources/pycharm_selenium/test1/nd2_webinfo')
# userinfoPath=(r'/Users/JacZh/desktop/resources/pycharm_selenium/test1/nd2_userinfo') 

def get_webinfo(webinfo_path):
	webinfo_dict = {}
	config=open(webinfo_path)
	for line in config:
		pairs = [ele.strip() for ele in line.split('=')] 
		# webinfo_dict.update(dict([result]))
		webinfo_dict[pairs[0]]= pairs[1]
	
	return webinfo_dict

def get_userinfo(userinfo_path):
	userinfo_list = []
	config = open(userinfo_path)
	for line in config:
		user_dict = {}
		user = [ele.strip() for ele in line.split(';')] # create a list

		for account in user: #create dict-elements, put into list
			detail = [ele.strip() for ele in account.split('=')]
			user_dict[detail[0]]=detail[1]
		userinfo_list.append(user_dict)
	return userinfo_list


# webinfoPath=(r'/Users/JacZh/desktop/resources/pycharm_selenium/test1/nd2_webinfo')
# userinfoPath=(r'/Users/JacZh/desktop/resources/pycharm_selenium/test1/nd2_userinfo') 
# result=get_userinfo(userinfoPath)
# print (result)