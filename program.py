import requests
import bs4

def main():
    # print the header
    print_the_header()
    code = input("What zipcode do you want the weather for (97232)?")
    code = code.strip()
    html = get_html_from_web(code)
    get_weather_from_html(html)
    # display the forcast
    print("hello from main")


def print_the_header():
    print('-----------------------')
    print('------weather app------')
    print('-----------------------')


def get_html_from_web(zipcode):

    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    main()

