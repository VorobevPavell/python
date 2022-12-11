from cgitb import text
import tkinter as tk
import requests 
win = tk.Tk()


def get_weather():
    city = entry_city.get() # Получаем данные от пользователя 
    key = '7cf02696ca5288d8a875756866efe105' # ключ API c сайта https://openweathermap.org/
    url = 'http://api.openweathermap.org/data/2.5/weather'  # Делаем запрос по этой ссылке, чтобы получить JSON ответ
    params = {'APPID' : key, 'q' : city ,'units' : 'metric'}
    result = requests.get(url,params=params)
    weather = result.json()
    f_weather = 'good =)' if weather["main"]["temp"] > 5 else 'bad =('
    precipitation = weather['weather'][0]["main"]
    info_label['text'] = f'{str(weather["name"]).lower()} : {precipitation.lower()} \n temperature : {weather["main"]["temp"]}°c \n feels like : {weather["main"]["feels_like"]}°c \n the weather is {f_weather}' 


frame_label = tk.Frame(win,bg='#323646')
frame_label.place(relheight=0.4,relwidth=1,rely=0.4)

info_label = tk.Label(frame_label,bg='#323646',fg='#9900FF',font=('Arial',18))
info_label.pack()

name_frame = tk.Frame(bg='#323646')
name_frame.place(relwidth=0.3,relheight=0.1,rely=0.1)



frame_entry = tk.Frame(win,bg='#323646')
frame_entry.place(relwidth=1,relheight=0.2,rely=0.03)

name_lbl = tk.Label(frame_entry,bg='#323646',text='write your city : ',fg='white',font='Arial')
name_lbl.pack() 

frame_btn = tk.Frame(win,bg='#323646',bd=5)
frame_btn.place(relx=0.18,rely=0.25)

entry_city = tk.Entry(frame_entry,fg='white',text='write your city')
entry_city.pack()

get_weather = tk.Button(frame_btn,text='what weather is it now?',command=get_weather,fg='#9900FF',bg='#323646',font='Arial')
get_weather.grid()

win['bg'] = '#323646'
win.resizable(False,False)
win.geometry('300x280+500+280')
win.title('Weather') # попробывать реализовать is good/is bad now при помощи f строки
win = tk.mainloop()