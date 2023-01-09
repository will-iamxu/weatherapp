import datetime as dt 
import requests 
from tkinter import*
from configparser import ConfigParser
from tkinter import messagebox

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ddcc4d2cd5f25752069bbd67f7074350'

def getWeather(city):
    '''gets the weather from a city'''
    cityJSON = requests.get(url.format(city))
    if cityJSON:
        #return a tuple (City, Country, Temp F, icon, weather, humidity)
        json = cityJSON.json()
        city = json['name']
        country = json['sys']['country']
        temp = json['main']['temp']
        temp = f'{(temp - 273.15)*9/5+32:.2f}'
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['description']
        hum = json['main']['humidity']
        final = (city, country, temp, icon, weather, hum)
        return final
    else:
        return None
def search():
    
    c = city.get()
    weather = getWeather(c)
    if weather:
        locationLabel['text'] = f'{weather[0]}, {weather[1]}'
        temp['text'] = f'{weather[2]}°'
        weatherlbl['text'] = f'{weather[4]}'
        humidity['text'] = f'{weather[5]}% Humidity'
        img["file"] = f'weather\\weather_icons\\{weather[3]}@2x.png'
        
    else:
        messagebox.showerror('Error', f"Cannot find city {c}")
        
#creates the app and sizes it
app = Tk()
app.title("Simple Weather App")
app.geometry('480x480')
#Makes a entry place
city = StringVar()
city_entry = Entry(app, textvariable=(city), width = 40)
city_entry.pack()

#search button
searchButton = Button(app, text = 'Search Weather', width=12, command=search)
searchButton.pack()

#location label
locationLabel = Label(app, text="", font=('bold', 20))
locationLabel.pack()

#image
img = PhotoImage(file="")
image = Label(app, image=img)
image.pack()

#temp
temp = Label(app, text="")
temp.pack()

#weather label
weatherlbl = Label(app, text = "")
weatherlbl.pack()

#humidity
humidity = Label(app, text = "")
humidity.pack()
app.mainloop()

    
