import argparse
import requests
import json
import socket
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument("-host", type=str, dest='target', required=True)

args = parser.parse_args()

lightblue =  '\033[94m'
clear =      '\033[0m'
bold =       '\033[01m'
red =        '\033[31m'
yellow =     '\033[93m'

ip  = args.target

api2 = "https://ipapi.co/"  #NOT WORKING ):

api2json = "/json/"         #NOT WORKING ):

api = "http://ip-api.com/json/"

apic = "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

ipv4 = "https://ip4.seeip.org/json"

ipv6 = "https://ip6.seeip.org/json"

coun = "https://api.myip.com/"

try:
        data = requests.get(api+ip+apic).json()
        data2 = requests.get(api2+ip+api2json).json()
        ipv4 = requests.get(ipv4).json()
        ipv6 = requests.get(ipv6).json()
        coun = requests.get(coun).json()
        sys.stdout.flush()
        blue = lightblue+bold+"[➛]"
        red = red+bold+"[▶]"
        yell = yellow+"[➛]"
        yell2 = yellow+"[↷]"
        print(red, "Script by D3m0ni4k,Darkstreet")
        print(yell, "Target:", data['query'])
        print(yell, "Lookup Status:", data['status'])
        print(blue, "ISP:", data['isp'])
        print(blue, "Organisation:", data['org'])
        print(blue, "City:", data['city'])
        print(blue, "Region name:", data['regionName'])
        print(blue, "Latitude:", data['lat'])
        print(blue, "Longitude:", data['lon'])
        print(blue, "AS Number:", data['as'])
        print(blue, "Zip:", data['zip'])
        print(blue, "Proxy:", data['proxy'])
        print(blue, "Reverse:", data['reverse'])
        print(blue, "Hosting:", data['hosting'])
        print(" "+clear)
        print(yell2, "What they see about you"  )
        print(blue, "Your Public IPV4:", ipv4['ip'])
        print(blue, "Your Public IPV6:", ipv6['ip'])
        print(blue, "Hostname:",socket.gethostname())
        print(blue, "Your Country:", coun['country'])


except KeyboardInterrupt:
        print('User requested exit'+clear)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red+bold+"[⌛]"+"Connection Error"+clear)
    sys.exit(1)
