import argparse
import sys
from random import randint
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
VJ_URL = "https://www.vietjetair.com/Sites/Web/vi-VN/Home"

TDN='AG48046301'
PAS='Tamtam60#'
FROM='Ho Chi Minh'
TO='Ha Noi'
DATE='15/08/2020'
NL='2'
TE=''
EB=''

def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))


class VietJetLogin:
    def __init__(self,loginID , password,Di,Den,Ngay,Nl):
        self.loginid = loginID
        self.password = password
        self.di=Di
        self.den=Den
        self.ngay=Ngay
        self.nl=Nl
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get(VJ_URL)
        self.driver.find_element_by_link_text('Đăng nhập').click()
        random_sleep(6,6)
        self.driver.find_element_by_link_text('Đại lý bán vé').click()
        random_sleep(8,8)
        
        
        loginid_ele = self.driver.find_element_by_css_selector('#txtAgentID')
        loginid_ele.send_keys(self.loginid)
        
        password_ele = self.driver.find_element_by_css_selector('#txtAgentPswd')
        password_ele.send_keys(self.password)
        self.driver.find_element_by_link_text('Truy cập').click()
        random_sleep(3,3)
    def sreach(self):
        self.driver.find_element_by_link_text('Đặt chuyến bay').click()
        random_sleep(5,5) 
        self.driver.find_element_by_css_selector('#chkRoundTrip1').click() 
        #điền địa điểm đi
        self.driver.find_element_by_css_selector('#lstOrigAP').send_keys(self.di)
        #điền địa điểm đến
        self.driver.find_element_by_css_selector('#lstDestAP').send_keys(self.den)
        #chọn ngày
        NGay = self.driver.find_element_by_css_selector('#departure1')
        ActionChains(self.driver).move_to_element(NGay).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(self.ngay).perform()
        #self.driver.find_element_by_css_selector('#departure1').clear()
        #self.driver.find_element_by_css_selector('#departure1').send_keys(self.ngay)
        #self.driver.find_element_by_css_selector('#txtNumAdults').clear().send_keys(self.nl)
        self.driver.find_element_by_link_text('Lựa chọn chuyến đi').click()
        

if __name__ == '__main__':
    vj = VietJetLogin(TDN,PAS,FROM,TO,DATE,NL)
    #Đăng Nhập
    vj.login()
    #bắt đầu tìm
    vj.sreach()
    
    
