# YouTube Random Video Scraper
This Python script randomly chooses keywords from a keywords.txt file and scrapes the YouTube search engine to find a video link associated with the chosen keywords. The script allows the user to change the number of keywords that are randomly chosen as well as the location of the keywords.txt file by editing the config.ini file.

# Requirements
This script requires the following dependencies to be installed:

1. requests_html
2. configparser - (may be installed by default, I'm not sure.)

`pip install requests_html`
`pip install configparser`

# How to Use
1. Clone this repository or download the youtube_scraper.py, update_keywords.py, keywords.txt, and config.ini files.
2. Install the required dependencies by running pip install -r requirements.txt in the command line.
3. Open the config.ini file to edit the location of the keywords.txt file and the number of keywords to be included in the search term.
4. Run the youtube_scraper.py file in the command line by running `python youtube_scraper.py`.
5. The script will randomly choose a search term from the list of keywords in the keywords.txt file and scrape the YouTube search engine to find video links associated with the search term.
6. The script will output the search term and a random video link associated with the search term to the terminal.
7. Open the link in your web browser, and enjoy your random video.

# Configurations
The config.ini file allows the user to change the location of the keywords.txt file and the number of keywords to be included in the search term.

```
[Keywords]
keywords_path = "keywords.txt"
num_of_keywords = 2
```

keywords_path: The location of the keywords.txt file relative to the location of the youtube_scraper.py file.
num_of_keywords: The number of keywords to be included in the search term.

# Using the default keywords file
The program comes with a default keywords.txt file containing a list of keywords. If you want to use this file, leave the keywords_path variable in the config.ini file as is.

Although if you do have problems with Python not finding the path, just update the file to be the full path to wherever the file is kept.

`keywords_path = "/path/to/this/directory/keywords.txt"`

# Using a custom keywords file
If you want to use your own custom keywords file, create a new .txt file and add your list of keywords, each on a new line. Then, open the config.ini file and change the keywords_path variable to point to your new file.


# License
This script is licensed under the MIT License.