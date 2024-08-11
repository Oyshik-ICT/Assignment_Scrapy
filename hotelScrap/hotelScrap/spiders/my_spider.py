import scrapy
import json
import random
import os, requests
from ..items import HotelscrapItem

class MySpider(scrapy.Spider):
    name = "my_spider"

    def start_requests(self):
        url = "https://uk.trip.com/htls/getHotDestination?x-traceID=1723089042493.7cfaXTHBxWn7-1723181981937-1029942597"

        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'currency': 'GBP',
            'locale': 'en-GB',
            'origin': 'https://uk.trip.com',
            'p': '77464206474',
            'pid': '6551bd45-d8d8-4dab-8d77-b18b3b5ff4d3',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://uk.trip.com/hotels/?locale=en-GB&curr=GBP',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'trip-trace-id': '1723089042493.7cfaXTHBxWn7-1723181981937-1029942597',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-traceid': '1723089042493.7cfaXTHBxWn7-1723181981937-1029942597'
        }

        cookies = {
            'ibulanguage': 'EN',
            'cookiePricesDisplayed': 'GBP',
            'UBT_VID': '1723089042493.7cfaXTHBxWn7',
            '_abtest_userid': '3009283a-ee37-42a6-826e-535e6742fe79',
            'devicePixelRatio': '1',
            '_fwb': '229N5UnRhD8wqpEVGOJ2BK.1723088957101',
            '_gid': 'GA1.2.303000213.1723088958',
            '_gcl_au': '1.1.193305774.1723088958',
            '_tt_enable_cookie': '1',
            '_ttp': 'To5pHxdxAutsnJkjPZr1vUq3QBC',
            'nfes_isSupportWebP': '1',
            '_RF1': '182.160.106.203',
            '_RSG': 'WxKt_1OOsa1_LOrQLOQ00A',
            '_RDG': '287676d4558b1824c5307c893243324b58',
            '_RGUID': '19366180-7fdd-4ee0-a000-69855ad5857f',
            'ibu_online_permission_cls_ct': '1',
            'ibu_online_permission_cls_gap': '1723089061190',
            'GUID': '09031046112211562641',
            'GUID.sig': 'f1YJDZdO4EbJS34zilSW7GcqTlFRijoMlJVTXzuoiLg',
            'ibu_online_jump_site_result': '{"site_url":[],"suggestion":[]}',
            'ibu_online_home_language_match': '{"isRedirect":false,"isShowSuggestion":false,"lastVisited":true,"region":"bd","redirectSymbol":false}',
            '_tp_search_latest_channel_name': 'flights',
            'ibu_oh_pp_exposed': '1',
            'g_state': '{"i_p":1723182967127,"i_l":2}',
            'intl_ht1': 'h4%3D338_730568%2C359_996749%2C338_54429492%2C338_731925%2C722_2198258%2C338_6353548',
            'IBU_TRANCE_LOG_P': '77464206474',
            'ibulocale': 'en_gb',
            'oldLocale': 'en-GB',
            '_bfa': '1.1723089042493.7cfaXTHBxWn7.1.1723180262555.1723180272871.9.5.10320668148',
            'IBU_showtotalamt': '3',
            'wcs_bt': 's_33fb334966e9:1723180277',
            '_uetsid': '5967d940553911ef9ae817ff71e8ed40',
            '_uetvid': '59680130553911efaa3ff916fa4c3525',
            '_ga': 'GA1.1.1259192855.1723088958',
            '_ga_37RNVFDP1J': 'GS1.2.1723178735.8.1.1723180277.48.0.0',
            '_ga_2DCSB93KS4': 'GS1.2.1723178734.8.1.1723180278.47.0.0',
            '_ga_X437DZ73MR': 'GS1.1.1723178728.9.1.1723181980.0.0.0'
        }

        # Body of the request as a JSON object
        payload = {
            "lastUpdateTime": 0,
            "newHotDestinationFlag": True,
            "allDataFlag": True,
            "head": {
                "platform": "PC",
                "clientId": "1723089042493.7cfaXTHBxWn7",
                "bu": "ibu",
                "group": "TRIP",
                "aid": "",
                "sid": "",
                "ouid": "",
                "caid": "",
                "csid": "",
                "couid": "",
                "region": "GB",
                "locale": "en-GB",
                "timeZone": "6",
                "currency": "GBP",
                "p": "77464206474",
                "pageID": "10320668150",
                "deviceID": "PC",
                "clientVersion": "0",
                "frontend": {
                    "vid": "1723089042493.7cfaXTHBxWn7",
                    "sessionID": "9",
                    "pvid": "5"
                },
                "extension": [
                    {"name": "cityId", "value": ""},
                    {"name": "checkIn", "value": ""},
                    {"name": "checkOut", "value": ""}
                ],
                "tripSub1": "",
                "qid": "",
                "pid": "6551bd45-d8d8-4dab-8d77-b18b3b5ff4d3",
                "hotelExtension": {},
                "cid": "1723089042493.7cfaXTHBxWn7",
                "traceLogID": "557b258d7a9b1",
                "ticket": "",
                "href": "https://uk.trip.com/hotels/?locale=en-GB&curr=GBP"
            }
        }

        yield scrapy.Request(url=url, method='POST', headers=headers, cookies=cookies, body=json.dumps(payload), callback=self.parse)

    def parse(self, response):
        try:
            data = json.loads(response.text)

            countryInfo = [(item['id'], item['displayName'])  for item in data['group'][0]['hotDestination']]
            location, country = random.choice(countryInfo)

            print('00000000000000000000000000000000000000000', country)

            # Proceed to the next link
            next_url = "https://uk.trip.com/hotels/list?city=" + str(location)
            yield scrapy.Request(url=next_url, callback=self.parse_next, meta={'country': country})

        except json.JSONDecodeError as e:
            self.logger.error("Failed to decode JSON: %s", e)

    def parse_next(self, response):

        items = HotelscrapItem()
        hotels = response.css('.hotel-info')
        country = response.meta.get('country')
        hotels_info = []
        dirCreate = 0
        if not os.path.exists('photos'):
            os.makedirs('photos')

        country_dir = f"photos/{country}"
        if not os.path.exists(country_dir):
            dirCreate = 1
            os.makedirs(country_dir)

            for hotel in hotels:
                title =  hotel.css('.name::text').get()
                img_src_list = hotel.css('.m-lazyImg__img::attr(src)').getall()
                rating = hotel.css('.real::text').get()
                room = hotel.css('.room-panel-roominfo-name::text').get()
                price = hotel.css('#meta-real-price div::text').get()
                location = hotel.css('.transport span:nth-of-type(2)::text').get() 
                hotels_info.append([title, img_src_list, rating, room, price, location])

                if dirCreate == 1:
                    for img_src in img_src_list:
                        img_name = title + img_src.split("/")[-1]  # Get the image file name from the URL
                        img_path = os.path.join(country_dir, img_name)
                    self.download_image(img_src, img_path)

                items['country'] = country
                items['title'] = title
                items['img_src_list'] = img_src_list
                items['rating'] = rating
                items['room'] = room
                items['price'] = price
                items['location'] = location

                yield items

            print('kkkkkkkkkkkkkkk', hotels_info)

    def download_image(self, img_url, path):
        try:
            response = requests.get(img_url)
            with open(path, 'wb') as f:
                f.write(response.content)
            self.logger.info(f"Image saved to {path}")
        except Exception as e:
            self.logger.error(f"Failed to download {img_url}: {e}")





