#!/usr/bin/env python3.5

# Copyright (c) 2019 Fernando
# Url: https://github.com/dlfernando/
# License: MIT

# USAGE COMMAND TO CHECK DOMAIN.ES AVAILABILITY EVERY 0.2 SECONDS:
# You should install linux command "watch". Example usage:
# watch -n 0.2 -d -g ./piton.py DOMAIN.ES

import requests
import sys
import os
from bs4 import BeautifulSoup

class spider:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.session = requests.session()
        self.check_url = 'https://www.nic.es/sgnd/dominio/publicBuscarDominios.action?request_locale=en'
        self.headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en,hi;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'DNT': '1', 'Host': 'www.nic.es', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    def get_key(self):
        res = self.session.get(self.check_url)
        if res.status_code == 200:
            key = BeautifulSoup(res.text, 'lxml').find('input',{'name':"_DXD_OHF_"})['value']
            return key
        return None

    def get_domain_info(self):
        key = self.get_key()
        if key is not None:
            data = {'_DXD_OHF_':key, 'tDominio.nombreDominio':self.domain_name}
            res = self.session.post(self.check_url, data=data)
            if res.status_code == 200:
                table = BeautifulSoup(res.text,'lxml').find('table',{'class':"dominios"})
                the_row = table.find('tr',{'class':"alt"})
                name = the_row.find('th',{'class':"name"}).text.strip()
                avaibility = the_row.find('td' ,{'class':"disp"}).img['alt']
                if avaibility == 'yes':
                    shellcommand = 'WRITE HERE SHELL COMMAND TO EXECUTE IS AVAILABLE. YOU CAN USE REGISTRANTS API TO GET DOMAIN INSTANTLY FOR EXAMPLE'
                    #os.system(shellcommand)  #uncomment this line to execute command.
                    return (f'{name} DOMAIN IS AVAILABLE')
                else:
                    return (f'{name} DOMAIN IS NOT AVAILABLE')
            else:
                return f'request returned erro {res.status_code}'
        else:
            return "Some Error Occured"


# domain_name = input('Enter the domain Name: ')
domain_name =sys.argv[1]
s = spider(domain_name)
status = s.get_domain_info()
print(status)


