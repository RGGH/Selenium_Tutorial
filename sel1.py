# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
import os

def searches():
	# source file check
	if not os.path.isfile('champions.txt'):
		print ("The champions text file does not exist\n")
	else:
		print("text file found - now starting process\n")

	# get txt from source file
	with open ("champions.txt","r") as f:
		names=f.readlines()
		print(f'untreated list = {names}')
		print("\n")
		newnames = [name.replace("\n","") for name in names if (name !="\n")]
		print(newnames)
		print("\n")
	return(newnames)


def fetch_p(myvar):

	# create webdriver object 
	driver = webdriver.Chrome() 
	# Start URL 
	driver.get("https://www.wikipedia.org") 
	element = driver.find_element_by_id("searchInput")
	element.clear()
	element.send_keys(myvar)
	element.send_keys(Keys.RETURN);
	time.sleep(3)
	xpath_stringp2 = '//*[@id="mw-content-text"]/div[1]/p[2]'
	xpath_stringp3 = '//*[@id="mw-content-text"]/div[1]/p[3]'
	
	try:
		element = driver.find_element_by_xpath(xpath_stringp2).text
		if len(element) > 1:
			print(element)
			print("\n")
			return(element)
		else:
			element = driver.find_element_by_xpath(xpath_stringp3).text
			print(element)
			print("\n")
			return(element)
	except:
		pass

	finally:
		time.sleep(1)
		driver.close()


## main ##
if __name__== '__main__':

	# get the list of pages(names) to fetch
	snames = searches()

	# run
	for f1champion in snames: 
		dat = fetch_p(f1champion)
		with open("response.txt",'a') as f:
			f.write(dat)
			f.write("\n")

	print("All done!")
