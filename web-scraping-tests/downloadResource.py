import requests
import base64

# url = "https://courses.cscc.edu/bbcswebdav/pid-13980741-dt-content-rid-86881986_1/courses/MATH-2153-001-40861-SU-2020/2153%20-%201%20-11.1-11.4%20Vectors%20and%20vector%20operations.pdf"
url = 'https://courses.cscc.edu/bbcswebdav/pid-13980741-dt-content-rid-86881986_1/xid-86881986_1'
user = 'sjanardhan'
pw = 'Krisna3227'
encoded = base64.b64encode(bytes(f"{user}:{pw}", 'utf-8'), altchars=None)
basic_auth_key = f"Basic {encoded.decode('utf-8')}"
headers = {
  'Authorization': basic_auth_key,
  # 'Cookie': 'JSESSIONID=B2E99FB77B4A09AD852FEBF453708908; AWSELB=ED2DE12B0256CCC57238C5D881EB90ED0041AAE8DF058709709AC417EECD9124A2750630F545372BC61E2AA7B3B6D5DE3054175C7FF4DE3DED353D9EE9B862C4A7657218BF; AWSELBCORS=ED2DE12B0256CCC57238C5D881EB90ED0041AAE8DF058709709AC417EECD9124A2750630F545372BC61E2AA7B3B6D5DE3054175C7FF4DE3DED353D9EE9B862C4A7657218BF; BbRouter=expires:1596411738,id:4F4EFC193F80D270073B91E16ADEAF36,signature:d4e546959359bb96ae9455cbb92d2902f3af47654151f03ddd1106d35720c679,site:8922e8cc-ab7b-4abf-8d37-ed2f4338a3c9,timeout:10800,user:7c74f8dc0d46483da022103a61ee199a,v:2,xsrf:f1ac4ea9-0913-42c6-962a-012782a6f57d'
}

response = requests.request("GET", url, headers=headers)

open('downloads\\facebook.pdf', 'wb').write(response.content)

def download_from_url(url_input, file_name):
  url = url_input
  user = 'sjanardhan'
  pw = 'Krisna3227'
  encoded = base64.b64encode(bytes(f"{user}:{pw}", 'utf-8'), altchars=None)
  basic_auth_key = f"Basic {encoded.decode('utf-8')}"
  headers = {
    'Authorization': basic_auth_key,
  }

  response = requests.request("GET", url, headers=headers)

  open(f'downloads\\{file_name}', 'wb').write(response.content)