import requests
import time

# find this data in your browser's cookies, then insert them here
steamdata = {
    "appid": 250820,
    "sessionid": "placeholder",
    "loginsecure": "placeholder"
}

ids = """

""".strip().split("\n")

# -----------

formdata = {
    "sessionid": steamdata['sessionid'],
    "appid": steamdata['appid']
}
cookies = {
    "sessionid": steamdata['sessionid'],
    "steamLoginSecure": steamdata['loginsecure']
}

for id in ids:
    formdata['id'] = id
    response = requests.post("https://steamcommunity.com/sharedfiles/unsubscribe", data=formdata, cookies=cookies)

    if response.status_code != 200:
        print(f"couldn't unsubscribe from {id}, reason: {response.reason}")
        break

    print(f"workshop item {id}: unsubscribed (response: {response.status_code} {response.reason})")
    time.sleep(1)
