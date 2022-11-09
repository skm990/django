from django.shortcuts import render
from pickle import GET
from urllib import response
import requests
from django.shortcuts import render
import json
import requests
from .models import *
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(req):
    ip_address = get_ip()
    response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=9a478c56e92ed658dfb9497bf8a42b01').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region_name"),
        "country": response.get("country_name"),
        "lat":response.get("latitude"),
        "lon":response.get("longitude"),
        "zip-code":response.get("zip")
    }
    ob=User_profile()
    ob.email         = req.GET.get("n1")
    ob.auth_id       = req.GET.get("n2")
    ob.first_name    = req.GET.get("n3")
    ob.last_name     = req.GET.get("n4")
    ob.moblie_no     = req.GET.get("n5")
    ob.tenant_id     =  req.GET.get("n6")
    ob.is_active     = req.GET.get("n7")
    ob.location_tacking = location_data
    ob.created_at  = req.GET.get("n9")
    ob.save()
    return render(req, 'index.html')
