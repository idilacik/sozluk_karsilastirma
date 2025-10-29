import re
import requests
import random

def tdkSozluk(kelime):
    """Gelen kelimenin TDK sözlüğünden anlamını bulur"""

    url = f"https://sozluk.gov.tr/gts?ara={kelime}"

    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    response = requests.get(url, headers=headers)
    data = response.text


    pattern = re.compile(r'"anlam":".*?"')

    matches = pattern.findall(data)

    anlamlar = []

    if matches:
        sayac = 1
        for match in matches:
            anlamlar.append(f"{sayac}.{match[9:-1]}")
            sayac += 1

    return anlamlar

def kubbealtiSozluk(kelime):
    url = f"https://eski.lugatim.com/rest/s/{kelime}"

    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    response = requests.get(url, headers=headers)
    data = response.text

    pattern = re.compile(r'<span class=\\"ChampturkB150\\">\d. </span><span class=\\"Champturk150\\">(.*?)[:.]')


    matches = pattern.findall(data)

    anlamlarkubbe = []

    if matches:
        sayac = 1
        for match in matches:
            anlamlarkubbe.append(f"{sayac}.{match}")
            sayac += 1

    return anlamlarkubbe




