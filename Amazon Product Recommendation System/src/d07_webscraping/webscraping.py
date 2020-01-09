import requests
import scrapy

class WebsiteData(scrapy.Spider):
    name = "website_data"
    start_url = ['URL']