import requests


class Notify:

    def __init__(self):
        self.__base_url = "https://webhook.site/"

    
    def send_event(self, data):
        requests.post(f"{self.__base_url}b5788a97-98f2-465b-b8f6-3c939dd19446", json=data)