from datetime import datetime

import scrapy
from peewee import (DateTimeField, ForeignKeyField, IntegerField, Model,
                    SqliteDatabase, TextField)

db = SqliteDatabase("database.db")


class BaseModel(Model): 
    class Meta:
        database = db


class Autor(BaseModel):
    autor = TextField(unique=True)
    user = TextField(default="keyuser")
    date = DateTimeField(default=datetime.now)


class Quote(BaseModel):
    autor = ForeignKeyField(Autor, backref="quotes")
    title = TextField()
    # author = TextField()
    tags = TextField(default="tag")
    date = DateTimeField(default=datetime.now)


db.drop_tables([Quote, Autor])
db.create_tables([Quote, Autor])


class QuotesSpider(scrapy.Spider):

    name = "QuotesSpider"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath('*//div[@class="quote"]')
        yield
        for q in quotes:
            title = q.xpath('.//span[@class="text"]/text()').get()
            author = q.xpath('.//small[@class="author"]/text()').get()
            tag = q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()

            # print("**AUTOR***",author)
            # print("**AUTOR***",author)
            # print("**TAGS***",tag)
            # print("-"*15)

            Autor.insert(autor=author).on_conflict_ignore().execute()
            row = Autor.get(Autor.autor == author)
            Quote.insert(
                autor_id=row.id, title=title, tags=tag
            ).on_conflict_ignore().execute()

            next_page = response.xpath('*//li[@class="next"]/a/@href').get()

            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback = self.parse)
