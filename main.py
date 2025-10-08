import sys
sys.stdout.reconfigure(encoding='utf-8')

import phonenumbers
import folium
from test import number
from phonenumbers import geocoder
key = '0608a4e06169408a94d4becda948ea10' 

n = phonenumbers.parse(number)
urloc = geocoder.description_for_number(n,"en")
print(urloc)

#get service provider

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder= OpenCageGeocode(key)
query=str(urloc)
res = geocoder.geocode(query)
#print(res)

lat =res[0]['geometry']['lat']
lng =res[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location = [lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup=urloc).add_to((myMap))

myMap.save("mylocation.html")