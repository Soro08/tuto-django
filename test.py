import psycopg2
import traceback
import requests, base64
import json
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
datas = {"references":["062FBX100"],"country":"FR","lang":"fr"}
r = requests.post("https://www.mister-auto.com/nwsAjax/ProductItem?id=67909&pageType=item&device=desktop", json=datas, headers = header)

#datas = {"references":["999BOL-1021","9784455","999BOL-100001","0300 986 461 769","999BOL-3360","999BOL-BD4750","0300 986 494 027","999BOL-1220W","999BOL-BD4752","999BOL-3311","021598463","021186693","999BOL-2630","999BOL-5010","062FBX100"],"pageType":"search/algolia","user_vehicle_id":0,"generic_id":0}
#r = requests.post("https://www.mister-auto.com/nwsAjax/ProductListingAlgolia?x-request-type=product-data", json=datas, headers = header)


print(r.status_code)
#print(r.text)

data = json.loads(r.text)

print(data)
