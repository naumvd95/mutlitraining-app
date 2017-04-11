import requests
import json

send_url = 'http://freegeoip.net/json/188.235.130.135'
r = requests.get(send_url)
location_data = json.loads(r.text)
country = location_data['country_name']
city = location_data['city']
print country, city

