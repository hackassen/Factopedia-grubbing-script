import requests, time
import random


def post(url, payload, headers, maxtrys:int=10, wait:int=10):

    responce=None
    for tryi in range(maxtrys):
        try:
            responce=requests.post(url, json=payload, headers=headers)
            responce.raise_for_status()
            break
        except requests.exceptions.BaseHTTPError as ex:
            print(f'!!! HTTPError occured: grub_ref_tree: {ex}')
        except requests.exceptions.ConnectionError as ex:
            print(f'!!! ConnectionError: try number: {tryi} of 10.')
            time.delay(wait)

    return responce

#-------------------------------

def get(url, headers, maxtrys:int=10, wait:int=10):

    responce=None
    for tryi in range(maxtrys):
        try:
            responce=requests.get(url, headers=headers)
            responce.raise_for_status()
            break
        except requests.exceptions.BaseHTTPError as ex:
            print(f'!!! HTTPError occured: {ex}')
        except requests.exceptions.ConnectionError as ex:
            print(f'!!! ConnectionError: try number: {tryi} of 10.')
            time.delay(wait)

    return responce
        

# sleeping for a random amount of seconds
def waitabit(sec_from:int, sec_to:int):
    sleep_duration=sec_from+(sec_to-sec_from)*random.random()
    time.sleep(sleep_duration)

