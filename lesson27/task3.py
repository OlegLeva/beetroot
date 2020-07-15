import requests

def weather_data(query):
    res = requests.get(f'https://openweathermap.org/find?utf8=%E2%9C%93&q={query}')
    return res.text


def print_weather(result, city):
    print(f"{}")


def main():
    city = input("Введите пожалуйста город: ")
    query = city
    weath = weather_data(query)
    print_weather(weath, city)


if __name__ == '__main__':
    main()
