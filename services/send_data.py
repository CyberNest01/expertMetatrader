import json
import requests


class SendData:
    ENDPOINT = 'http://127.0.0.1:8000/'

    def __init__(self, data, meta, config):
        self.data = data
        self.meta = meta
        self.config = config

    def __req(self, method, action_apt, data):
        kwargs = {}
        if method == 'post':
            kwargs['json'] = data
        else:
            kwargs['params'] = data
        request = requests.request(method, self.ENDPOINT + action_apt, **kwargs)
        return request

    def request(self):
        data = self.edit_data()
        response = self.__req('post', 'get/meta/data/', data)
        if response.status_code == 200:
            response = response.json()
            return {'response': response}
        raise Exception('Can not create request!')

    def edit_data(self):
        data_list = []
        context = {}
        for item in self.data['data']:
            data_list.append(self.meta.get_symbol(item._asdict()['symbol'])['data'])
        context.update({self.config.account: {
            'data': data_list,
            'equity': self.meta.send_equity()['data']['equity']
        }})
        return context
