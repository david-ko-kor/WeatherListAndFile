
import requests
import os
from dotenv import load_dotenv
load_dotenv()
apikey=os.getenv("apikey")
lat=37.3514
lon=127.9453
url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}"
result=requests.get(url)
response=result.json()
list=[]
i=response['list'][0]

for i in response['list']:
    print(i['dt_txt'],i['main']['temp'],i['main']['temp_min'],i['main']['temp_max'],i['main']['humidity'],i['weather'][0]['description'])
    list.append(str(i['dt_txt'])+","+str(i['main']['temp'])+","+str(i['main']['temp_min'])+","+str(i['main']['temp_max'])+","+str(i['main']['humidity'])+","+str(i['weather'][0]['description']))
    # with open('weather.csv','a',encoding='utf-8') as f:
    #     f.write(str(i['dt_txt'])+","+str(i['main']['temp'])+","+str(i['main']['temp_min'])+","+str(i['main']['temp_max'])+","+str(i['main']['humidity'])+","+str(i['weather'][0]['description'])+"\n")
    #
    #



