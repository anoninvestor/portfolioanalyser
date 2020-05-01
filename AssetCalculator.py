import requests
import gc


def fetch_NAV(url):
    try:
        temp = requests.get(url)
    except ConnectionError:
        print("NAV API timed out")
    nav = temp.json()["data"][0]["nav"]

    # just some safety stuff to clean memory
    del temp
    gc.collect()

    return nav


def fetch_total_value(details):
    total_value = dict()

    for key in details.keys():
        total_value[key] = details[key]["units"]*float(fetch_NAV(details[key]["nav_url"]))

    return total_value

