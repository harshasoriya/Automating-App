import pyttsx3
import time
import speech_recognition as sr
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from googletrans import Translator
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

en= pyttsx3.init()
en.setProperty('rate', 190)
voices=en.getProperty('voices')
en.setProperty('voice',voices[1].id)
en.setProperty('volume', 1)

def speak(audio):
    en.say(audio)
    en.runAndWait()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak...')
        r.pause_threshold = 0.5
        v=r.listen(source)
    
    try:
        print('working on your command...')
        text=r.recognize_google(v,language="en-in") 
        print("you said:",text)
        
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"

    return text 


class Instagram:
    
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.instagram.com/?hl=en")
        self.driver.maximize_window()
        
    def login(self):
        a=self.driver.find_element_by_name("username")
        a.send_keys("harshasoriya1998")
        b=self.driver.find_element_by_name("password")
        with open('password.txt',mode='r') as pw:
                    p=pw.read()
                    b.send_keys(p)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div').click()
        #time.sleep(10)
        path='/html/body/div[4]/div/div/div/div[3]/button[2]'
        element=WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, path)))
        element.click()
        time.sleep(2)
    
    def home(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()
        
    
    def message(self):
        self.driver.find_element_by_xpath(r"//a[@href='/direct/inbox/']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div/button").click()
        speak("to whom you want to send message")
        m=listen().lower()
        q=self.driver.find_element_by_name("queryBox")
        q.send_keys(m)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button").click()
        speak("Speak the Message!!")
        while True:
            text= listen()
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
            text_box=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            text_box.send_keys(text)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            speak('Do you want to send more.')
            ch=listen().lower()
            if 'no' in ch:
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[1]/div/a').click()
                break
            else:
                speak("Speak the Message!!!")
            

    def notification(self):
        self.driver.find_element_by_xpath(r"//a[@href='/accounts/activity/']").click()
        time.sleep(10)


    def like(self):
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[3]/div/article[1]/div[3]/section/span[1]/button").click()
    
    def newsfeed(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
        time.sleep(5)
    
    def open(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div').click()
        while True:
            query=listen().lower()
            if "like" in query:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(3)
        
            elif "comment" in query:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
                input_box=self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                speak('speak your comment')
                input_box.send_keys(listen().lower())
                time.sleep(3)
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                time.sleep(5)

            elif "next" in query:
                try:
                    t=self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
                except NoSuchElementException:
                    t=self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
                t.click()
                time.sleep(3)

            elif "previous" in query:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[1]').click()
                time.sleep(3)

            elif "close" or "back" in query:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
                break


    def profile(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]').click()
        time.sleep(5)

    

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    def comment(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[3]/div/article[4]/div[3]/section[3]/div/form/textarea').click()
        time.sleep(3)
        textarea2=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[3]/div/article[4]/div[3]/section[3]/div/form/textarea')
        speak("speak your comment")
        textarea2.send_keys(listen().lower())
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[3]/div/article[4]/div[3]/section[3]/div/form/button').click()
        
    def search(self,name):
        c=self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        c.send_keys(name)
        speak("is it correct name?")
        while True:
            s=listen().lower()
            if "yes" in s:
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
                break
            elif "incorrect" in s:
                c.clear()
                speak("Please speak name once again!!")
                name=listen().lower()
                name=name.replace('search','')
                self.search(name)

    def follow(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
    
    def unfollow(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()

    def close(self):
        self.driver.close()







speak("Hello, How can i help you")
while True:
    l=listen().lower()
    if "instagram" in l:
        n=Instagram()
        speak("here is your instagram, from which id i have to login")
        while True:
            b=listen().lower()
            if "harsh" in b:
                n.login()
                speak("what you want to do")
                while True:
                    b=listen().lower()
                    if "like" in b:
                        n.like()
                    elif "comment" in b:
                        n.comment()
                    elif "my profile" in b:
                        n.profile()
                    elif "home page" in b:
                        n.home()
                    elif "message" in b:
                        n.message()
                    elif "notification" in b:
                        n.notification()
                    elif "feed" in b:
                        n.newsfeed()
                    elif "open" in b:
                        n.open()
                    elif "search" in b:
                        c=b.replace('search','')
                        n.search(c)
                    elif "unfollow" in b:
                        n.unfollow()
                    elif "follow" in b:
                        n.follow()
                    elif "down" in b:
                        n.scroll()
                    elif "close" in b:
                        n.close()
                        exit()
                        break   
            elif 'none'==b:
                speak('Please speak from which login id to login !!')

            else:
                speak('You have spoken wrong id')
                speak('Do you want to try again')
                l=listen().lower()
                if 'no'==l:
                    n.close()
                    exit()
                    break    


    
        
    elif "close" in l:
        speak("call me anytime you want, Thank You!!")
        break                 

