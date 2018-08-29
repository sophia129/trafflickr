import requests
import json
import urllib2
url = "https://ic-media-service.run.aws-usw02-pr.ice.predix.io/v2/mediastore/ondemand/assets/CAM-ATL-0008-1/media"

querystring = {"mediaType":"VIDEO","timestamp":"1509552826000"}

headers = {
    'authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1MWU4ZDY3YzljZTY0Njk1YjQ5ZDRmN2I2YjMwNmM0NyIsInN1YiI6ImhhY2thdGhvbiIsInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImllLWN1cnJlbnQuU0RTSU0tSUUtUFVCTElDLVNBRkVUWS5JRS1QVUJMSUMtU0FGRVRZLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEFSS0lORy5JRS1QQVJLSU5HLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEVERVNUUklBTi5JRS1QRURFU1RSSUFOLkxJTUlURUQuREVWRUxPUCJdLCJjbGllbnRfaWQiOiJoYWNrYXRob24iLCJjaWQiOiJoYWNrYXRob24iLCJhenAiOiJoYWNrYXRob24iLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlmMWYyYzRkIiwiaWF0IjoxNTA5ODQyMTA1LCJleHAiOjE1MTA0NDY5MDUsImlzcyI6Imh0dHBzOi8vODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3IiwiYXVkIjpbImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBBUktJTkcuSUUtUEFSS0lORy5MSU1JVEVEIiwiaWUtY3VycmVudC5TRFNJTS1JRS1QVUJMSUMtU0FGRVRZLklFLVBVQkxJQy1TQUZFVFkuTElNSVRFRCIsInVhYSIsImhhY2thdGhvbiIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBFREVTVFJJQU4uSUUtUEVERVNUUklBTi5MSU1JVEVEIl19.Ph6vSrRHx6x1Lf1O2gps7cDDmyPGSNkFzzUrYJSKgO4iFVYx77TIYsQbjtulz9dMlqYC6fsJc6wsaTK6nGN7PL63823Q6Q4OmBN2fiPRUDnVbk4075-OI50Z6fVy5oY5VCKPpJgTYaiIw0qufBOe3gPgylxRXxEHHsxJmzbrjYyeLB4vmAoMZsb13h9E4qhXhMW3l3htyoKZZxL6VIvzbsZMOQ7oo1VSCncQBuzbfZiWUiG4ZTb1mC9_4tj89LAxxUKy5-VnZNPqwXD6FxWkScAwuqlA9N6NOj9qfrhCxWb1efSRqdes7xe-KljrTvCnw6LjTKCHTjzAOiZdYK9AQg",
    'predix-zone-id': "SDSIM-IE-PUBLIC-SAFETY",
    'cache-control': "no-cache",
    'postman-token': "2d285110-e4f3-de3b-51f0-7ef3b200dcb1"
    }

r1 = requests.request("GET", url, headers=headers, params=querystring)

# print(r1.text)
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

print(r3.text)
r4 = json.loads(r3.text)

url = r4['listOfEntries']['content'][0]['url']

headers = {
    'authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1MWU4ZDY3YzljZTY0Njk1YjQ5ZDRmN2I2YjMwNmM0NyIsInN1YiI6ImhhY2thdGhvbiIsInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImllLWN1cnJlbnQuU0RTSU0tSUUtUFVCTElDLVNBRkVUWS5JRS1QVUJMSUMtU0FGRVRZLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEFSS0lORy5JRS1QQVJLSU5HLkxJTUlURUQuREVWRUxPUCIsImllLWN1cnJlbnQuU0RTSU0tSUUtUEVERVNUUklBTi5JRS1QRURFU1RSSUFOLkxJTUlURUQuREVWRUxPUCJdLCJjbGllbnRfaWQiOiJoYWNrYXRob24iLCJjaWQiOiJoYWNrYXRob24iLCJhenAiOiJoYWNrYXRob24iLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlmMWYyYzRkIiwiaWF0IjoxNTA5ODQyMTA1LCJleHAiOjE1MTA0NDY5MDUsImlzcyI6Imh0dHBzOi8vODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiODkwNDA3ZDctZTYxNy00ZDcwLTk4NWYtMDE3OTJkNjkzMzg3IiwiYXVkIjpbImllLWN1cnJlbnQuU0RTSU0tSUUtVFJBRkZJQy5JRS1UUkFGRklDLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBBUktJTkcuSUUtUEFSS0lORy5MSU1JVEVEIiwiaWUtY3VycmVudC5TRFNJTS1JRS1QVUJMSUMtU0FGRVRZLklFLVBVQkxJQy1TQUZFVFkuTElNSVRFRCIsInVhYSIsImhhY2thdGhvbiIsImllLWN1cnJlbnQuU0RTSU0tSUUtRU5WSVJPTk1FTlRBTC5JRS1FTlZJUk9OTUVOVEFMLkxJTUlURUQiLCJpZS1jdXJyZW50LlNEU0lNLUlFLVBFREVTVFJJQU4uSUUtUEVERVNUUklBTi5MSU1JVEVEIl19.Ph6vSrRHx6x1Lf1O2gps7cDDmyPGSNkFzzUrYJSKgO4iFVYx77TIYsQbjtulz9dMlqYC6fsJc6wsaTK6nGN7PL63823Q6Q4OmBN2fiPRUDnVbk4075-OI50Z6fVy5oY5VCKPpJgTYaiIw0qufBOe3gPgylxRXxEHHsxJmzbrjYyeLB4vmAoMZsb13h9E4qhXhMW3l3htyoKZZxL6VIvzbsZMOQ7oo1VSCncQBuzbfZiWUiG4ZTb1mC9_4tj89LAxxUKy5-VnZNPqwXD6FxWkScAwuqlA9N6NOj9qfrhCxWb1efSRqdes7xe-KljrTvCnw6LjTKCHTjzAOiZdYK9AQg",
    'predix-zone-id': "SDSIM-IE-PUBLIC-SAFETY",
    'cache-control': "no-cache",
    'postman-token': "2ac84b46-5bc7-19c9-eb7d-bc3848f0e097"
    }

# print(r5.text)
r5 = requests.request("GET", url, headers=headers, stream=True)
handle = open("test222.mp4", "wb")
for chunk in r5.iter_content(chunk_size=512):
	if chunk:  # filter out keep-alive new chunks
		handle.write(chunk)