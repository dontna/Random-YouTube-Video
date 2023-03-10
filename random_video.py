import random
import update_keywords
import os
import configparser
import sys

from requests_html import HTMLSession

def import_keywords_from_file(filename: str):
    """Reads a file with a list of keywords and returns the keywords as a list.

    Args:
        filename (str): The name of the file containing the list of keywords.

    Returns:
        list: A list of keywords read from the file.
    """
    keywords = []

    if not os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/keywords.txt"):
        print("No keywords file found, creating it now...")
        update_keywords.update_keywords()

    with open(f"{os.path.dirname(os.path.abspath(__file__))}/{filename}", "r") as f:
        for keyword in f.readlines():
            keywords.append(keyword.strip().lower())

    return keywords 

def create_random_search_term(keywords: list, num_of_keywords=2):
    """Generates a random search term by choosing a random keyword from the provided list.

    Args:
        keywords (list): A list of keywords to choose from.
        num_of_keywords (int, optional): The number of keywords to include in the search term. Defaults to 2.

    Returns:
        str: The generated search term.
    """
    search_term = []

    for x in range(num_of_keywords):
        random_keyword = random.choice(keywords)

        if random_keyword.__contains__(' '):
            random_keyword = random_keyword.replace(' ', '+')

        search_term.append(random_keyword)

    return '+'.join(search_term)

def get_video_links_for_term(search_term: str, always_newest=False):
    """Uses the YouTube search engine to find video links for the provided search term.

    Args:
        search_term (str): The search term to use for the YouTube search.
        always_newest (bool, optional): Whether to search for only the newest videos. Defaults to False.

    Returns:
        list: A list of video links found for the search term.
    """
    video_links = []

    upload_date_int = random.randint(0, 5)

    # Dict of suffixs, allows the script to make youtube search for more recent videos.
    upload_date_suffix_dict = {
        1:'&sp=EgIIAQ',
        2:'&sp=EgQIAhAB',
        3:'&sp=EgQIAxAB',
        4:'&sp=EgQIBBAB',
        5:'&sp=EgQIBRAB'
    }

    # Chooses a random suffix from the dict.
    if always_newest == False:
        if upload_date_int != 0:
            upload_date_suffix = upload_date_suffix_dict[upload_date_int]
        else:
            upload_date_suffix = ""
    else:
        upload_date_suffix = upload_date_suffix_dict[1]


    if upload_date_int == 0:
        print("Upload date: Not Specified")
    elif upload_date_int == 1:
        print("Uploade date: Last Hour")
    elif upload_date_int == 2:
        print("Upload date: Today")
    elif upload_date_int == 3:
        print("Upload date: This week")
    elif upload_date_int == 4:
        print("Upload date: This month")
    elif upload_date_int == 5:
        print("Upload date: This year")

    with HTMLSession() as s:
        r = s.get(f'https://www.youtube.com/results?search_query={search_term}{upload_date_suffix}')

        r.html.render(sleep=2)

        video_cards = r.html.find('a#video-title')

        if len(video_cards) == 0:
            return -1

        for card in video_cards:
            href = card.attrs['href']
            full_link = f"https://www.youtube.com{href}"
            
            video_links.append(full_link)

    return video_links

def main():
    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(os.path.abspath(__file__))}/config.ini")

    keywords_file = config['Keywords']['keywords_path'].replace('"', '').replace('\'', '')
    num_of_keywords = int(config['Keywords']['num_of_keywords'])

    links_found = False

    print("Importing Keywords...")
    keywords = import_keywords_from_file(keywords_file)

    while not links_found:
        print("Creating a random search term...")
        search_term = create_random_search_term(keywords, num_of_keywords)

        print(f"Getting video links...")
        video_links = get_video_links_for_term(search_term)

        if video_links == -1:
            continue
        else:
            links_found = True

    print(f"\nYour search term: {search_term.replace('+', ' ')}")
    print(f"Your random video link: {random.choice(video_links)}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "update":
            update_keywords.update_keywords()
            exit(0)

    main()