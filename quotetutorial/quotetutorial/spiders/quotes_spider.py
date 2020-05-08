import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.amazon.co.uk/Logitech-Performance-Special-Adjustable-Programmable/dp/B07W7MQMD9/ref=sxin_1_ac_d_rm?ac_md=0-0-ZzUwMg%3D%3D-ac_d_rm&crid=CMFY695ODFTT&cv_ct_cx=g502&dchild=1&keywords=g502&pd_rd_i=B07W7MQMD9&pd_rd_r=25e999fe-0942-48d5-b1a2-e7f7da6ae717&pd_rd_w=hrpan&pd_rd_wg=9KhPa&pf_rd_p=c73f405e-e4f8-4128-b33f-b51584101765&pf_rd_r=SDX71A87041CYE97PXZE&psc=1&qid=1588927661&sprefix=G502%2Caps%2C349&sr=1-1-fe323411-17bb-433b-b2f8-c44f2e1370d4'
    ]

    def parse(self, response):
        price = response.css('#priceblock_ourprice::text').extract()
        yield {'price' : price}