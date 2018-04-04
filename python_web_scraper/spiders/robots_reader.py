import requests

def get_allowed_urls_from_text_file(robots_text):
    all_user_agent = 'User-agent: *'
    agent = 'User - agent:'
    allowed_url = 'Allow'
    allowed_urls = []
    critical_area = False
    for text in robots_text:
        text = text.strip()
        if text == all_user_agent:
            critical_area = True

        if critical_area:
            if text.startswith('%s' % agent):
                critical_area = False
                break
            elif text.startswith(allowed_url):
                allowed_urls.append(text[7 : len(text)+1])
    return allowed_urls

def read_text_from_url(url):
    text = requests.get(url).text
    robots_text = open('robots.txt', 'w')
    robots_text.truncate()
    robots_text.write(text)

def get_allowed_urls_to_scrape():
    choice = input('Enter 1 for scraping all allowed urls on a website, 2 if you know pages to scrape : ')
    allowed_urls = []
    if int(choice) == 1:
        url = input('URL of Website to explore, for ex : https://google.com : ')
        robots_url = url + '/robots.txt'

        read_text_from_url(robots_url)
        allowed_urls = get_allowed_urls_from_text_file(open('robots.txt', 'r'))
        allowed_urls = [url + allowed_url for allowed_url in allowed_urls]
    elif int(choice) == 2:
        urls = input('Enter all URLs seperated by comma -> ')
        allowed_urls = urls.split(',')
        allowed_urls = [allowed_url.strip() for allowed_url in allowed_urls]
    else:
        print('Invalid input!')
    return allowed_urls