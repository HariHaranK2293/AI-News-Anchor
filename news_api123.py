# news_api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
news_api_key = "02149e8e8f884e2fad23ee38b07e308d"
class NewsAPI:
    def __init__(self, news_api_key):
        self.news_api_key = news_api_key

    def get_news(self, query, num_news):
        url = f'https://newsapi.org/v2/everything?q={query}&from=2024-02-10&sortBy=popularity&pageSize={num_news}&language=en&apiKey={self.news_api_key}'
        
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            return news_data.get("articles", [])
        else:
            return []

    def get_news_descriptions(self, query, num_news):
        news = self.get_news(query, num_news)
        desc_list = [news_item['description'] for news_item in news]
        return desc_list

    def get_news_string(self, query, num_news):
        desc_list = self.get_news_descriptions(query, num_news)
        desc_string = ". ".join(desc_list)
        return desc_string