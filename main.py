from hf_chatbot import HuggingFaceChatBot
from gnews import GNews
from newspaper import Article

hf_chatbot_obj = HuggingFaceChatBot()
gnews_obj = GNews()


class News:
    def __init__(self) -> None:
        pass

    def get(self):
        news = []
        tech_news = gnews_obj.get_news_by_topic("TECHNOLOGY")
        for item in tech_news:
            url = item.url
            full = gnews_obj.get_full_article(item["url"])
            article = Article(url)
            print(full)
            # ai_description = hf_chatbot_obj.conversation(item["description"])
            # news.append({"title": item["title"], "ai_description": ai_description})


news = News()
print(news.get())
