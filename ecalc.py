#coding: utf-8

import selenium, time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Opening browser
browser = webdriver.Firefox()            #Chrome also works fine but Firefox better
browser.get('http://www.ecalc.ch/motorcalc.php')

#Handling alert message
alert = browser.switch_to_alert()
alert.accept()

#Setting Motor Cooling to "execellent"
select = Select(browser.find_element_by_id("inGMotorCooling"))
select.select_by_value("excellent")

#Setting Controller "max 10A"
select1 = Select(browser.find_element_by_id("inEType"))
select1.select_by_value("10")

#.............................Collecting data..............................

batterylist = []
select2 = browser.find_element_by_xpath("//select[@id='inBCell']")
batteryoptions = select2.find_elements_by_tag_name("option")
for battery in batteryoptions:
	batterylist.append(battery.get_attribute("value"))

manufacturerlist = []
select3 = browser.find_element_by_xpath("//select[@id='inMManufacturer']")
manufactureroptions = select3.find_elements_by_tag_name("option")
for manufacturer in manufactureroptions:
	manufacturerlist.append(manufacturer.get_attribute("value"))

propellertypelist = []
select4 = browser.find_element_by_xpath("//select[@id='inPType']")
propellertypes = select4.find_elements_by_tag_name("option")
for propeller in propellertypes:
	propellertypelist.append(propeller.get_attribute("value"))


#..............................MAIN PROGRAM...................................

#While loop answer
answer = 'n'

print "\nBattery list: ",
print batterylist
print "\nPropeller List: ",
print propellertypelist
propeller_modified_list = [u'1', u'3', u'4', u'7']
print "\nPropeller modified list: ",
print propeller_modified_list

#Changing battery value by choosing from battery list
select5 = Select(browser.find_element_by_id("inBCell"))
select5.select_by_value("1")                                                   #Change the integer to value given in battery list

for i in manufacturerlist[1:]:
	#Setting motor manufacturer
	select6 = Select(browser.find_element_by_id("inMManufacturer"))
	select6.select_by_value(str(i))
	
	#Generating motor type list
	motortypelist = []
	select7 = browser.find_element_by_xpath("//select[@id='inMType']")
	motortypes = select7.find_elements_by_tag_name("option")
	for motor in motortypes:
		motortypelist.append(motor.get_attribute("value"))
	
	#Setting motor type
	for j in motortypelist[1:]:
		select8 = Select(browser.find_element_by_id("inMType"))
		select8.select_by_value(str(j))
		
		#Setting propeller type
		for k in propellertypelist[1:]:
			answer = 'n'
			while answer == 'n':
				select9 = Select(browser.find_element_by_id("inPType"))
				select9.select_by_value(str(k))

				for l in range(0,10):
					diameter = browser.find_element_by_id('inPDiameter').clear()
					alert.accept()
					diameter = browser.find_element_by_id('inPDiameter')
					diameter.send_keys(l)
				
					'''
					pitch = browser.find_element_by_id('inPPitch').clear()
					alert.accept()
					pitch = browser.find_element_by_id('inPPitch')
					pitch.send_keys(1)
					'''

					#dia = browser.find_element_by_id('inPDiameter')
					#diavalue = dia.find_elements_by_tag_name("value").value()
					#print diavalue

					#Clicking "calculate" button
					clickbutton = browser.find_element_by_name("btnCalculate")
					clickbutton.click()
			
					#Handling alert message that appears after hitting calculate button
					alert.accept()

					#Checking condition for while loop								#Hit 'n' to repeat same value or any key to continue
					answer = raw_input("Paused. Hit 'y' to continue: ")             #to next value
