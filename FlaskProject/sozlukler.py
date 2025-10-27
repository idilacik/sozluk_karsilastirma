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

    liste_len = random.randint(1,6)
    random_list = []
    sayac = 1
    for i in range(liste_len):
        random_list.append(f"{sayac}.{kelime}")
        sayac += 1

    return  random_list




