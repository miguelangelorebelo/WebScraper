import json
import random
import re
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class DontPayEconomist:
    def __init__(
        self, date_format="%Y-%m-%dT%H:%M:%SZ", base_url="https://www.economist.com/"
    ):
        
        self.date_format = date_format
        self.base_url = base_url

        # Send a GET request to the webpage
        response = requests.get(base_url)

        # Parse the HTML content using Beautiful Soup
        self.soup = BeautifulSoup(response.text, "html.parser")

    def _collect_news_links(self) -> list:

        print("Collecting the list of news in the main page of The Economist")
        latest_news = []

        # Collect top_stories (the first few news)
        latest_news.extend(
            self.soup.find_all(
                "a", attrs={"data-analytics": re.compile("top_stories:headline_\d")}
            )
        )

        # Collect the topical content below the top stories
        latest_news.extend(
            self.soup.find_all(
                "a",
                attrs={"data-analytics": re.compile("topical_content_\d:headline_\d")},
            )
        )

        # Build the links using the base url
        self.titles_urls = DontPayEconomist.__build_links(latest_news, self.base_url)

        print(f"Collected {len(self.titles_urls)} urls")

        return self.titles_urls

    def bulk_extraction(self):

        instances = []

        for i in tqdm(range(len(self.titles_urls)), desc="Parsing Economist URLs"):
            url = self.titles_urls[i][1]

            # Extract that page with the developed function
            (
                headline,
                description,
                articleBody,
                image,
                datePublished,
            ) = DontPayEconomist.__url_extraction(url, self.date_format)

            instances.append(
                {
                    "Headline": headline,
                    "Description": description,
                    "Body": articleBody,
                    "Image": image,
                    "URL": url,
                    "Date": datePublished,
                }
            )

            # Wait with randomized time - throtle
            time.sleep(random.choice(range(1, 2)))

        print(f"completed the extraction of {len(instances)} novel news")

        return instances

    @staticmethod
    def __build_links(latest_news, base_url):
        urls = []
        titles = []

        for line in latest_news:
            urls.append(base_url + line["href"][1:])
            titles.append(line.text)

        titles_urls = [
            i for i in zip(titles, urls) if "FilmFilm" not in i[0]
        ]  # don't extract films

        return titles_urls

    @staticmethod
    def __url_extraction(url, date_format):

        # Send a GET request to the webpage
        response = requests.get(url)

        # Parse the HTML content using BS4
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the <script> element containing the JSON data
        script_element = soup.find("script", type="application/ld+json")

        # Get the JSON content and load it as a dictionary
        json_content = json.loads(script_element.string)

        # Access the keys in the dictionary
        headline = json_content["headline"]
        articleBody = json_content["articleBody"]
        description = json_content["description"]
        image = json_content["image"]

        # Transform to datetime the string containing the date
        datePublished = datetime.strptime(
            json_content["datePublished"], date_format
        )

        return headline, description, articleBody, image, datePublished
