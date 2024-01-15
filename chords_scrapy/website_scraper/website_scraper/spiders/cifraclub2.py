import scrapy


class CifrabotSpider(scrapy.Spider):
    name = 'cifrabot2'

    def start_requests(self):
        urls = ['https://www.cifraclub.com.br/stephen-sanchez/until-i-found-you/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Salvar a página HTML completa
        with open('cifraclub_page.html', 'wb') as file:
            file.write(response.body)

        # Extrair apenas o texto da letra
        letra = ' '.join(response.xpath("//pre//text()").extract())

        # Restante do código para extrair outras informações
        for elemento in response.xpath("//div[@class='g-1 g-fix cifra']"):
            yield {
                'autor': elemento.xpath(".//h2[@class='t3']/a/text()").get(),
                'titulo': elemento.xpath(".//h1[@class='t1']/text()").get(),
                'tom': elemento.xpath(".//span[@id='cifra_tom']/a/text()").get(),
                'capotraste': elemento.xpath("concat('Capo: ', substring-before(.//span[@data-cy='song-capo']/a/text(), 'ª'))").get(),
                'letra': letra
            }

'''
scrapy crawl cifrabot2 -O chords.csv
'''