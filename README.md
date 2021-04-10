# peewee-scrapy
Apenas para fins de estudos


https://quotes.toscrape.com/

-requisicao na pagina, apos executar comando o scrapy
gera um log tambem.
scrapy shell https://quotes.toscrape.com/
caso o status seja 200.
2 formas de extrair os dados
 *respose.xpath
 *response.css
-response.url
***respose.xpath
response.xpath("*//div")
response.xpath("*//div/span")
response.xpath("*//div/span[@class='text']/text()").getall()
response.xpath("*//span[@class='text']/text()").getall()
response.xpath("*//small[@class='author']/text()").getall()
***response.css
response.css("small.author::text").getall()
response.css("a.tag::text").getall()
response.xpath("*//a[@class='tag']/text()").getall()

scrapy runspider scrapy-quotes.py 
scrapy runspider scrapy-quotes.py -o quotes.json
scrapy runspider scrapy-quotes.py -o quotes.csv
scrapy runspider scrapy-quotes.py -o result.json -t json
scrapy runspider scrapy-quotes.py-o quotes.json --logfile logfile.text
scrapy runspider scrapy-quotes.py -o some.json -t json 2> some.text


response.xpath('*//li[@class="next"]/a').get()
       

response.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').get()
response.xpath('*//div[@class="tags"]').get()
response.xpath('*//div[@class="tags"]/a').get()

git remote add origin https://github.com/paulinhomacedo/peewee-scrapy.git

git push origin --delete master to https://github.com/paulinhomacedo/peewee-scrapy.git




