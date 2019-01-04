
def main():
    # print the header
    print_the_header()
    code = input("What zipcode do you want the weather for (97232)?")
    code = code.strip()
    get_html_from_web(code)

    # get html from web
    # parse the html
    # display the forcast
    print("hello from main")


def print_the_header():
    print('-----------------------')
    print('------weather app------')
    print('-----------------------')


def get_html_from_web(zipcode):

    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print(url)


if __name__ == '__main__':
    main()

