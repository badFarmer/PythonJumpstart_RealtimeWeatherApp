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
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    print(loc, condition, temp, scale)

if __name__ == '__main__':
    main()

