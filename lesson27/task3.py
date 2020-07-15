import requests

def weather_data(query, api_ad):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather',
                       params={'q': {query}, 'appid': {api_ad}, 'units': 'metric'})
    return res.json()


def print_weather(result, city):
    print(f"{city}, {result['main']['temp']}")


def main():
    city = input("Введите пожалуйста город: ")
    query = city
    api_ad = '82d874077256d593ec739f2feaeddbc2'
    weather = weather_data(query, api_ad)
    print_weather(weather, city)


if __name__ == '__main__':
    main()
