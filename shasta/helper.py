import requests
import json


class Caller:
    def __init__(self, endpoint, header):
        self.enp = endpoint
        self.header = header

    def get(self, endpoint, data=None):
        return requests.get(self.enp + endpoint, headers=self.header, data=json.dumps(data))

    def get_list(self, endpoint, limit=10, cursor=None, data=None):
        return requests.get('{}{}?limit={}&cursor={}'.format(self.enp, endpoint, limit, cursor), headers=self.header,
                            data=json.dumps(data))

    def post(self, endpoint, data):
        return requests.post(self.enp + endpoint, headers=self.header, data=json.dumps(data))

    def patch(self, endpoint, data):
        return requests.patch(self.enp + endpoint, headers=self.header, data=json.dumps(data))

    def delete(self, endpoint, data=None):
        return requests.delete(self.enp + endpoint, headers=self.header, data=json.dumps(data))
