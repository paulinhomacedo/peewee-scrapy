import scrapy

# scrapy runspider aosfatos.py
# scrapy shell aosfatos.py
# scrapy shell https://www.aosfatos.org/
# scrapy shell https://www.aosfatos.org/noticias/checamos/verdadeiro/
# scrapy runspider aosfatos.py -s HTTPCACHE_ENABLED=1 -o test.json


class AosFatosSpider(scrapy.Spider):

    name = "aos_fatos"
    start_urls = ["https://www.aosfatos.org/"]

    def parse(self, response):
        links = response.xpath(
            '//nav//ul//li/a[re:test(@href,"checamos")]/@href'
        ).getall()
        for link in links:
            print("**** links:****")
            yield scrapy.Request(response.urljoin(link), callback=self.parse_category)

    def parse_category(self, response):
        # import ipdb
        # ipdb.set_trace()
        news = response.xpath(
            "*//div[@class='entry-card-list infinite-container']/a/@href"
        ).getall()
        for new_url in news:
            yield scrapy.Request(response.urljoin(new_url), callback=self.parse_new)

        # pages_url = response.css('.pagination a::attr(href)').getall()  
        # for pages in pages_url:
        #     yield scrapy.Request(response.urljoin(pages), callback=self.parse_category)  

    def parse_new(self, response):
        title = response.css("article h1::text").get()
        date = " ".join(response.css("p.publish_date::text").get().split())

        '''quotes = response.css('article blockquote')
        for quote in quotes:
            quotes_text = quote.css('::text').get()'''

        
        # quotes=
        # status_quotes=
        # url=
        yield {
            "title": title,
            "date": date,
            "url": response.url,
        }


       

