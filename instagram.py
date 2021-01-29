from speech import *
import time
from selenium import webdriver
from googletrans import Translator
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Instagram:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/?hl=en")
        self.driver.maximize_window()

    def login(self):
        a = self.driver.find_element_by_name("username")
        a.send_keys("harshasoriya1998")
        b = self.driver.find_element_by_name("password")
        with open('password', mode='r') as pw:
            p = pw.read()
            b.send_keys(p)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div').click()
        # time.sleep(10)
        path = '/html/body/div[4]/div/div/div/div[3]/button[2]'
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, path)))
        element.click()
        time.sleep(2)

    def home(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()

    def message(self):
        self.driver.find_element_by_xpath(r"//a[@href='/direct/inbox/']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div/button").click()
        speak("to whom you want to send message")
        m = listen().lower()
        q = self.driver.find_element_by_name("queryBox")
        q.send_keys(m)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button").click()
        lang_list = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
                     'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
                     'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese': 'zh-cn',
                     'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
                     'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
                     'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el',
                     'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw',
                     'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig',
                     'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw',
                     'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
                     'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt',
                     'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
                     'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my',
                     'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl',
                     'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm',
                     'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd',
                     'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
                     'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',
                     'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi',
                     'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil',
                     'Hebrew': 'he'}
        speak("Choose your Language")
        lang=listen().lower()
        while True:
            if lang in lang_list:
                speak("Speak the Message!!")
                while True:
                    m = listen()
                    msg=Translator().translate(m, src='en', dest=lang_list[lang])
                    self.driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
                    text_box = self.driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                    text_box.send_keys(msg.text)
                    self.driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                    speak('Do you want to send more.')
                    ch = listen().lower()
                    if 'no' in ch:
                        self.driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[1]/div/a').click()
                        break
                    else:
                        speak("Speak the Message!!!")
            elif lang=='none':
                speak("You have not choosen any language, please choose your language")
            else:
                speak('Sorry!! I cannot process that request. Do you want to try again!!')
                qur=listen().lower()
                if 'no' in qur:
                    break




    def notification(self):
        self.driver.find_element_by_xpath(r"//a[@href='/accounts/activity/']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a').click()

    def like(self):
        self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/section/div/div[3]/div/article[1]/div[3]/section/span[1]/button").click()

    def newsfeed(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
        time.sleep(5)

    def open(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div').click()
        while True:
            query = listen().lower()
            if "like" in query:
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(3)

            elif "comment" in query:
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
                input_box = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                speak('speak your comment')
                input_box.send_keys(listen().lower())
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
                time.sleep(5)

            elif "next" in query:
                try:
                    t = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
                except NoSuchElementException:
                    t = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
                t.click()
                time.sleep(3)

            elif "previous" in query:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[1]').click()
                time.sleep(3)

            elif "close" or "back" in query:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
                break

    def profile(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]').click()
        time.sleep(5)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def comment(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/section/div/div[3]/div/article[4]/div[3]/section[3]/div/form/textarea').click()
        time.sleep(3)
        textarea2 = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/section/div/div[3]/div/article[4]/div[3]/section[3]/div/form/textarea')
        speak("speak your comment")
        textarea2.send_keys(listen().lower())
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/section/div/div[3]/div/article[4]/div[3]/section[3]/div/form/button').click()

    def search(self, name):
        c = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        c.send_keys(name)
        speak("is it correct name?")
        while True:
            s = listen().lower()
            if "yes" in s:
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
                break
            elif "incorrect" in s:
                c.clear()
                speak("Please speak name once again!!")
                name = listen().lower()
                name = name.replace('search', '')
                self.search(name)

    def follow(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()

    def unfollow(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()

    def close(self):
        self.driver.close()
