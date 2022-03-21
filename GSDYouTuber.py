import GSDWebScraper

web_content = None

def start_project():
    print("Loading....")

def get_web_content():
    print("Web content created")
    web_content = "Content Scrapped from the Web"

def display_web_content():
    web_content = GSDWebScraper.get_data_from_web()
    if web_content is not None:
        print(web_content)
    else:
        print("no web content to display")