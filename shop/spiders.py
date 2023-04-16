import scrapy


class VekSpider(scrapy.Spider):
    name = "21vek.by"
    allowed_domains = ["www.21vek.by"]
    start_urls = ["https://www.21vek.by/special_offers/dacha_all.html"]

    def parse(self, response, **kwargs):
        for product in response.css(".widget_selection .result__item"):
            data = {
                "external_id": int(product.attrib.get("data-code")),
                "name": product.attrib.get("result__name").strip(),
                "price": product.attrib.get("data-price").strip(),
                "category": product.attrib.get("data-category").strip(),
                "link": f"{self.allowed_domains[0]}{product.css('.mindbox-pr-view result__link::attr(href)').get()}",
            }
            yield data
