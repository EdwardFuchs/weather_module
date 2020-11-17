def weather(event):
    import requests
    import json
    import datetime
    if len(event.splited)<3:
        event.message_send("Ошибка! В команде нужно указывать город.")
        return False
    elif len(event.splited)>3:
        event.message_send("Ошибка! В команде нужно указывать только 1 город.")
        return False
    city = event.splited[2]
    weather = requests.get('http://api.openweathermap.org/data/2.5/weather', params={
        'lang':'ru',
        'units': 'metric',
        'APPID': 'ef23e5397af13d705cfb244b33d04561',
        'q': city
    }).json()
    if weather["cod"] == "404" or weather["cod"] == 404:
        event.message_send(f"Город {city} не найден.")
        return False
    elif weather["cod"] != "200" and weather["cod"] != 200:
        event.message_send(weather["message"])
        return False
    country = weather['sys']['country']
    temp = weather["main"]["temp"]
    weather_desc = weather["weather"][0]["description"]
    wind_speed = weather["wind"]["speed"]
    clouds = weather["clouds"]["all"]
    humidity = weather["main"]["humidity"]
    utc = int(weather["timezone"]/3600)
    utc = f"+{utc}" if utc>=0 else utc
    city = weather["name"]
    time_update = datetime.datetime.fromtimestamp(weather["dt"]).strftime('%H:%M')
    current_weather = f"""Погода в {country}/{city}:
&#8195;•Температура: {temp}°C
&#8195;•Состояние: {weather_desc}
&#8195;•Скорость ветра: {wind_speed} м/с
&#8195;•Облачность: {clouds}%
&#8195;•Влажность: {humidity}%
&#8195;•Время обновления: {time_update} UTC{utc}"""
    event.message_send(f"""{current_weather}""")
    return True
    
HandleCmd('погода', 0, weather)