import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
        
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        booktitles=response.css("h3 > a::attr(title)").getall()
        for title in booktitles:
            print()
            print()
            print('title',title)
            print()
            print()
            print()
            yield{
                'title':title
            }
