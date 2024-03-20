from celery import shared_task
from services.controler import MetaTraderControler
from config.models import UserConfig



def send_order_info():
    context = {}
    configs = UserConfig.get_configs()
    for config in configs:
        meta = MetaTraderControler(
            int(config.account),
            config.password,
            config.server,
            config.file_name
        )
        data_list = []
        data = meta.send_position()
        if data['status'] and data['data']:
            for item in data['data']:
                data_list.append(meta.get_symbol(item._asdict()['symbol']))
            context.update({config.account: {
                'data': data_list,
                'equity': meta.send_equity()
            }})
    return context

