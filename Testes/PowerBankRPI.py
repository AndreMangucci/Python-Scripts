#/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import datetime

data = datetime.datetime.now()

while 1 :
	data = str(datetime.datetime.now())
	f = open("C:\\Users\\André Hermann\\Desktop\\teste.txt","a")
	f.write("{} \n".format((data[:19])))
	f.close()
	time.sleep(60)
