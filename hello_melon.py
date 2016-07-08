import requests
import json
import time

#from __future__ import absolute_import, print_function
import tweepy

#headers = {'Referer': 'http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=15001801'}

while(True):
    r = requests.get('http://tktapi.melon.com/api/product/schedule/list.json?prodId=200063&pocCode=SC0002&perfTypeCode=GN0001&sellTypeCode=ST0001&v=1')
    r.encoding = 'euc-kr'
    cont = r.text.encode('ascii', 'ignore').decode('ascii')
    j = json.loads(cont)
    data = j['data']
    dayList = data['perfDaylist']

    for i in dayList:
        seatCount = i['perfTimelist'][0]['seatGradelist'][0]['seatCount']
        print(seatCount)
        if (seatCount != '0' and seatCount != '1'):
            print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            print 'gogogo!! seat'

            # twitter
            consumer_key="eOPi2p0UnDVv5wq8DWJbLMboi"
            consumer_secret="C2AVX09ucAzTrYj4A9I4PBZjHvesQjQpIphCHf8P8TjfxxmDFV"

            access_token="3140862638-wZJ9abCYe8pr9AIQoSYfZ3t3RNl73j2Span7Dld"
            access_token_secret="4JxD8ywJFvr26CJoGB8tL8yKRy2b0bKukUuufucG7BdIH"

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.secure = True
            auth.set_access_token(access_token, access_token_secret)

            api = tweepy.API(auth)
            msg = time.strftime("%Y/%m/%d %H:%M:%S @blue_supia ", time.localtime()) + i['perfDay'] + 'day gogogo!!  ' + seatCount

            api.update_status(status=msg)
        else:
            #print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            #print 'no seat;;'
            print( '.')

    time.sleep(60)
