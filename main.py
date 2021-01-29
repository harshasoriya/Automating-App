import instagram
from speech import *


speak("Hello, How can i help you")
while True:
    l = listen().lower()
    if "instagram" in l:
        n = instagram.Instagram()
        speak("here is your instagram, from which id i have to login")
        while True:
            b = listen().lower()
            if "harsh" in b:
                n.login()
                speak("what you want to do")
                while True:
                    b = listen().lower()
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
                        c = b.replace('search', '')
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
            elif 'none' == b:
                speak('Please speak from which login id to login !!')

            else:
                speak('You have spoken wrong id')
                speak('Do you want to try again')
                l = listen().lower()
                if 'no' == l:
                    n.close()
                    exit()
                    break




    elif "close" in l:
        speak("call me anytime you want, Thank You!!")
        break
