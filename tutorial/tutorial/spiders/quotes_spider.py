import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    quote_count = 1
    f = open("quotes.txt","a",encoding = "UTF-8")
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        #command: scrapy crawl  quotes -o quotes.json

        """
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            
            yield {
                "title":title,
                "author":author,
                "tags":tags    
            }
        """
        #command: scrapy crawl  quotes
        
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            self.f.write(str(self.quote_count)+"***********************************\n")
            self.f.write("Quote: "+title+"\n")
            self.f.write("By: "+author+"\n")
            self.f.write("Tags: "+str(tags)+"\n")
            self.quote_count+=1

        next_url = response.css("li.next a::attr(href)").get()

        if next_url is not None:
            next_url = "http://quotes.toscrape.com/" + next_url
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.f.close()

#response.css("li.next a::attr(href)").get()