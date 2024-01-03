import scrapy
from scrapy.crawler import CrawlerProcess


class IndeedPythonSpider(scrapy.Spider):
    # Identity
    name = 'jobsbot'
    # Request

    def start_requests(self):
        # Define url(s) to scrape
        urls = ['https://www.indeed.com/jobs?q=python']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response

    def parse(self, response):
        # this is where you should process what is returned from the response
        for item in response.xpath("//td[@class='resultContent']"):
            yield {
                'position': item.xpath(".//span[1]/text()").get(),
                'company_name': item.xpath(".//span[@data-testid='company-name']/text()").get(),
                'location': item.xpath(".//div[@data-testid='text-location']/text()").get(),
                'link': 'https://www.indeed.com' + item.xpath(".//a/@href").get()
            }

        try:
            next_page_link = response.xpath(
                "//a[@data-testid='pagination-page-next']/@href").get()
            print('#' * 10)
            print(next_page_link)
            print('#' * 10)

            if next_page_link is not None:
                complete_link = 'https://www.indeed.com' + next_page_link
                print('*' * 10)
                print('*', complete_link)
                print('*' * 10)
                yield scrapy.Request(url=complete_link, callback=self.parse)

        except Exception as error:
            print(error)
            print('Reached the last page')

# scrapy crawl jobsbot -O dados.csv
