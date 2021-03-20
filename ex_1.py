#! /usr/local/bin/python3

import logging
import os
import urllib.parse

import argparse
import requests

logging.basicConfig(
    level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')


URL = 'https://api.macaddress.io/v1'
API_KEY = os.environ.get('API_KEY')


def main(mac_address: str) -> str:

    params = {
        'search': mac_address,
        'output': 'json'
    }

    url = URL + '?' + urllib.parse.urlencode(params, safe=':')
    try:
        with requests.get(url, headers={'X-Authentication-Token': API_KEY}) as resp:
            if resp.status_code == 200:
                company_name = resp.json()['vendorDetails']['companyName']
                return f'Company name: {company_name}'
            else:
                return f'Request failed with status code {resp.status_code}, msg={resp.text}'
    except requests.exceptions.RequestException:
        logging.exception('An error occurred processing your request.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This program get a mac address as parameter'
                    ' and return Company Name associated with that MAC address.')
    parser.add_argument('mac_address', action='store', help='MAC address')
    args = parser.parse_args()
    print(main(args.mac_address))
