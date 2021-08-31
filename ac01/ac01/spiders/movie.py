# -*- coding: utf-8 -*-
import scrapy
from ..items import Ac01Item
import json



class TxmsSpider(scrapy.Spider):
    name = 'txms'
    allowed_domains = ['cair.cambricon.com']
    start_urls = [
        'https://cair.cambricon.com/sharecloud-boot/resource/page?pageNo=1&pageSize=90']
    offset = 0

    # def start_requests(self):
    #     for i in range(0, 121, 30):
    #         url = self.url.format(i)
    #         yield scrapy.Request(
    #             url=url,
    #             callback=self.parse
    #         )

    def parse(self, response):
        items = Ac01Item()
        # lists = json.loads(response.text)
        lists = json.loads(response.body_as_unicode())
        detail_data = lists.get('result')
        de1_date = detail_data.get('records')
        indexs = len(de1_date)

        # print(de1_date, type(de1_date))
        # print(de1_date[0]['id'])
        #
        # for dz in lists:
        #     name = dz.get('result').get('records').get('id')
        #     print(name)

        for index in range(0, indexs):
            items['name'] = de1_date[index]['name']
            items['id_1'] = de1_date[index]['id']
            items['description'] = de1_date[index]['description']

            yield items

        # if self.offset < 120:
        #     self.offset += 90
        #     url = 'https://cair.cambricon.com/sharecloud-boot/resource/page?pageNo=1&pageSize=90'.format(
        #         str(self.offset))
        #
        #     yield scrapy.Request(url=url, callback=self.parse)
