from Tkinter import *
import time
import requests
import json
import urllib2
import os

root = Tk() #root makes the window with title bar only one per program
w = Label(root, text="Surveillance Camera")
#labels can display text, icon, or images
w.pack()
#tells text to size itself and become visible
E1 = Entry(root, bd =5)
E2 = Entry(root, bd =5)
#Fcanvas = Canvas(bg="black", height=600, width=170)

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createTextbox()
        self.createWidgets()

    def createTextbox(self):
        self.label1 = Label(root, text = "Enter a start date (MM/DD/YYYY HH:MM:SS)")
        #E1 = Entry(root, bd =5)
        E1.pack()
        self.label1.pack()

        self.label2 = Label(root, text = "Enter in a file name")
        E2.pack()
        self.label2.pack()

    def getDate():
        def getName():
            return E2.get()
        getName()
        thetime = E1.get()
        time_tuple = time.strptime(thetime, '%m/%d/%Y %H:%M:%S')
        time_epoch = int(time.mktime(time_tuple) * 1000)
        print E1.get()
        print time_epoch

        url = "https://ic-media-service.run.aws-usw02-pr.ice.predix.io/v2/mediastore/ondemand/assets/CAM-ATL-0008-1/media"

        querystring = {"mediaType":"VIDEO","timestamp": str(time_epoch)}

        headers = {
            'authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1MWU4ZDY3YzljZTY0Njk1YjQ5ZDRmN2I2YjMwNmM0NyIsInN1YiI6ImhhY2thdGhvbiIsInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImllLWN1cnJlbnQuU0RTSU0tSUUtUFVCTElDLVNBRkVUWS5JRS1QVUJMSUMtU0FGRVRZLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEFSS0lORy5JRS1QQVJLSU5HLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEVERVNUUklBTi5JRS1QRURFU1RSSUFOLkxJTUlURUQuREVWRUxPUCJdLCJjbGllbnRfaWQiOiJoYWNrYXRob24iLCJjaWQiOiJoYWNrYXRob24iLCJhenAiOiJoYWNrYXRob24iLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlmMWYyYzRkIiwiaWF0IjoxNTA5ODQyMTA1LCJleHAiOjE1MTA0NDY5MDUsImlzcyI6Imh0dHBzOi8vODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3IiwiYXVkIjpbImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBBUktJTkcuSUUtUEFSS0lORy5MSU1JVEVEIiwiaWUtY3VycmVudC5TRFNJTS1JRS1QVUJMSUMtU0FGRVRZLklFLVBVQkxJQy1TQUZFVFkuTElNSVRFRCIsInVhYSIsImhhY2thdGhvbiIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBFREVTVFJJQU4uSUUtUEVERVNUUklBTi5MSU1JVEVEIl19.Ph6vSrRHx6x1Lf1O2gps7cDDmyPGSNkFzzUrYJSKgO4iFVYx77TIYsQbjtulz9dMlqYC6fsJc6wsaTK6nGN7PL63823Q6Q4OmBN2fiPRUDnVbk4075-OI50Z6fVy5oY5VCKPpJgTYaiIw0qufBOe3gPgylxRXxEHHsxJmzbrjYyeLB4vmAoMZsb13h9E4qhXhMW3l3htyoKZZxL6VIvzbsZMOQ7oo1VSCncQBuzbfZiWUiG4ZTb1mC9_4tj89LAxxUKy5-VnZNPqwXD6FxWkScAwuqlA9N6NOj9qfrhCxWb1efSRqdes7xe-KljrTvCnw6LjTKCHTjzAOiZdYK9AQg",
            'predix-zone-id': "SDSIM-IE-PUBLIC-SAFETY",
            'cache-control': "no-cache",
            'postman-token': "2d285110-e4f3-de3b-51f0-7ef3b200dcb1"
            }

        r1 = requests.request("GET", url, headers=headers, params=querystring)

        #print(r1.text)
        r2 = json.loads(r1.text)
        url = r2['pollUrl']

        querystring = {"page":"0","size":"100"}

        headers = {
            'authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1MWU4ZDY3YzljZTY0Njk1YjQ5ZDRmN2I2YjMwNmM0NyIsInN1YiI6ImhhY2thdGhvbiIsInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImllLWN1cnJlbnQuU0RTSU0tSUUtUFVCTElDLVNBRkVUWS5JRS1QVUJMSUMtU0FGRVRZLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEFSS0lORy5JRS1QQVJLSU5HLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEVERVNUUklBTi5JRS1QRURFU1RSSUFOLkxJTUlURUQuREVWRUxPUCJdLCJjbGllbnRfaWQiOiJoYWNrYXRob24iLCJjaWQiOiJoYWNrYXRob24iLCJhenAiOiJoYWNrYXRob24iLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlmMWYyYzRkIiwiaWF0IjoxNTA5ODQyMTA1LCJleHAiOjE1MTA0NDY5MDUsImlzcyI6Imh0dHBzOi8vODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3IiwiYXVkIjpbImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBBUktJTkcuSUUtUEFSS0lORy5MSU1JVEVEIiwiaWUtY3VycmVudC5TRFNJTS1JRS1QVUJMSUMtU0FGRVRZLklFLVBVQkxJQy1TQUZFVFkuTElNSVRFRCIsInVhYSIsImhhY2thdGhvbiIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBFREVTVFJJQU4uSUUtUEVERVNUUklBTi5MSU1JVEVEIl19.Ph6vSrRHx6x1Lf1O2gps7cDDmyPGSNkFzzUrYJSKgO4iFVYx77TIYsQbjtulz9dMlqYC6fsJc6wsaTK6nGN7PL63823Q6Q4OmBN2fiPRUDnVbk4075-OI50Z6fVy5oY5VCKPpJgTYaiIw0qufBOe3gPgylxRXxEHHsxJmzbrjYyeLB4vmAoMZsb13h9E4qhXhMW3l3htyoKZZxL6VIvzbsZMOQ7oo1VSCncQBuzbfZiWUiG4ZTb1mC9_4tj89LAxxUKy5-VnZNPqwXD6FxWkScAwuqlA9N6NOj9qfrhCxWb1efSRqdes7xe-KljrTvCnw6LjTKCHTjzAOiZdYK9AQg",
            'predix-zone-id': "SDSIM-IE-PUBLIC-SAFETY",
            'cache-control': "no-cache",
            'postman-token': "c5af3c2d-4b15-655d-89e1-3ac66ae0b7b1"
            }

        r3 = requests.request("GET", url, headers=headers, params=querystring)

        #print(r3.text)
        r4 = json.loads(r3.text)

        url = r4['listOfEntries']['content'][0]['url']

        headers = {
            'authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1MWU4ZDY3YzljZTY0Njk1YjQ5ZDRmN2I2YjMwNmM0NyIsInN1YiI6ImhhY2thdGhvbiIsInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImllLWN1cnJlbnQuU0RTSU0tSUUtUFVCTElDLVNBRkVUWS5JRS1QVUJMSUMtU0FGRVRZLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEFSS0lORy5JRS1QQVJLSU5HLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEVERVNUUklBTi5JRS1QRURFU1RSSUFOLkxJTUlURUQuREVWRUxPUCJdLCJjbGllbnRfaWQiOiJoYWNrYXRob24iLCJjaWQiOiJoYWNrYXRob24iLCJhenAiOiJoYWNrYXRob24iLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlmMWYyYzRkIiwiaWF0IjoxNTA5ODQyMTA1LCJleHAiOjE1MTA0NDY5MDUsImlzcyI6Imh0dHBzOi8vODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3IiwiYXVkIjpbImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBBUktJTkcuSUUtUEFSS0lORy5MSU1JVEVEIiwiaWUtY3VycmVudC5TRFNJTS1JRS1QVUJMSUMtU0FGRVRZLklFLVBVQkxJQy1TQUZFVFkuTElNSVRFRCIsInVhYSIsImhhY2thdGhvbiIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBFREVTVFJJQU4uSUUtUEVERVNUUklBTi5MSU1JVEVEIl19.Ph6vSrRHx6x1Lf1O2gps7cDDmyPGSNkFzzUrYJSKgO4iFVYx77TIYsQbjtulz9dMlqYC6fsJc6wsaTK6nGN7PL63823Q6Q4OmBN2fiPRUDnVbk4075-OI50Z6fVy5oY5VCKPpJgTYaiIw0qufBOe3gPgylxRXxEHHsxJmzbrjYyeLB4vmAoMZsb13h9E4qhXhMW3l3htyoKZZxL6VIvzbsZMOQ7oo1VSCncQBuzbfZiWUiG4ZTb1mC9_4tj89LAxxUKy5-VnZNPqwXD6FxWkScAwuqlA9N6NOj9qfrhCxWb1efSRqdes7xe-KljrTvCnw6LjTKCHTjzAOiZdYK9AQg",
            'predix-zone-id': "SDSIM-IE-PUBLIC-SAFETY",
            'cache-control': "no-cache",
            'postman-token': "2ac84b46-5bc7-19c9-eb7d-bc3848f0e097"
            }

        print(url)
        r5 = requests.request("GET", url, headers=headers, stream=True)
        handle = open(getName(), "wb")
        for chunk in r5.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)

    submit = Button(root, text ="Submit", command = getDate)
    submit.pack(side = BOTTOM)

    def createWidgets(self):
        def getName2():
            return E2.get()

        def snd1():
            print(os.path.abspath(getName2()))
            os.system(os.path.abspath(getName2()))
            #os.system("C://test.mp4")
            #var = IntVar()

        self.QUIT = Button(root)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack(side =RIGHT)

        self.video = Button(root)
        self.video["text"] = "Play Video"
        self.video["fg"] = "blue"
        self.video["command"] = snd1
        self.video.pack(side =LEFT)


app = Application(master=root)

app.mainloop() #program executes when you enter main loop

root.destroy()