import time

class Log_info(object):
	def __init__(self, path = '', mode = 'w'):
		file_name = 'test_log: ' + time.strftime('%m-%d-%y', time.gmtime())
		self.log = open(path + file_name + '.txt', mode)#can not have dupi file name

	def log_write(self,msg):
		self.log.write(msg)

	def log_close(self):
		self.log.close()


if __name__ == '__main__':
	log = Log_info()
	log.log_write('test')
	log.log_close()