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

****** AOS FATOS.ORG ****
buscar atributos
response.css('a.card::attr(href)')
----
 response.css('html')
Out[2]: [<Selector xpath='descendant-or-self::html' data='<html lang="pt-BR" dir="ltr">\n    <he...'>]
response.css('title').getall()
Out[5]: 
['<title>Aos Fatos | Valorize o que é real</title>',
 '<title>twitter</title>',
 '<title>Instagram</title>',
 '<title>Facebook</title>',
 '<title>WhatsApp</title>',
 '<title>YouTube</title>']
  response.css('title::text').getall()
Out[7]: 
['Aos Fatos | Valorize o que é real',
 'twitter',
 'Instagram',
 'Facebook',
 'WhatsApp',
 'YouTube']

 response.xpath('*//nav[@class="menu"]').getall()

 In [12]:  response.xpath('//nav//ul//li/a').getall()
Out[12]: 
['<a href="/noticias/checamos/verdadeiro/">Verdadeiro</a>',
 '<a href="/noticias/checamos/impreciso/">Impreciso</a>',
 '<a href="/noticias/checamos/exagerado/">Exagerado</a>',
 '<a href="/noticias/checamos/distorcido/">Distorcido</a>',
 '<a href="/noticias/checamos/contraditorio/">Contraditório</a>',
 '<a href="/noticias/checamos/insustentavel/">Insustentável</a>',
 '<a href="/noticias/checamos/falso/">Falso</a>',
 '<a href="/noticias/investigamos/">Investigamos</a>',
 '<a href="/noticias/explicamos/">Explicamos</a>',
 '<a href="/noticias/nas-redes/">Nas redes</a>',
 '<a href="/noticias/radar/">Radar</a>',
 '<a href="/noticias/tempo-real/">Tempo Real</a>',
 '<a href="/noticias/eleicoes-2020/">Eleições 2020</a>',
 '<a href="/noticias/analise/">Análises</a>',
 '<a href="/noticias/hq/">HQ</a>',
 '<a href="/aos-fatos-lab/">Aos Fatos Lab</a>',
 '<a href="/noticias/eleicoes-2018/">Eleições 2018</a>',
 '<a href="/noticias/">Tudo</a>',
 '<a href="/especiais/">Especiais</a>',
 '<a href="/noticias/manuais/">Manuais</a>',
 '<a href="/noticias/aos-graficos/">Aos Gráficos</a>']

*traz todos os links que tenha "checamos" marcado
 response.xpath('//nav//ul//li/a[re:test(@href,"checamos")]').getall()
Out[13]: 
['<a href="/noticias/checamos/verdadeiro/">Verdadeiro</a>',
 '<a href="/noticias/checamos/impreciso/">Impreciso</a>',
 '<a href="/noticias/checamos/exagerado/">Exagerado</a>',
 '<a href="/noticias/checamos/distorcido/">Distorcido</a>',
 '<a href="/noticias/checamos/contraditorio/">Contraditório</a>',
 '<a href="/noticias/checamos/insustentavel/">Insustentável</a>',
 '<a href="/noticias/checamos/falso/">Falso</a>']

fetch('url') executa o response em outra url

article/h1/"conteudo"
response.css('article h1::text').get()

response.css('p publish_date::text').get()
''join(response.css('p.publish_date::text').get().split())


response.xpath('//nav//ul//li/a[re:test(@href,"checamos")]').get()

response.css('article blockquote::text').getall()






