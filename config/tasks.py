from celery import shared_task
from services.controler import MetaTrader5Controler
from config.models import UserConfig
from services.send_data import SendData


@shared_task()
def send_order_info_mql5():
    context = {}
    configs = UserConfig.get_configs()
    for config in configs:
        meta = MetaTrader5Controler(
            int(config.account),
            config.password,
            config.server,
            config.file_name
        )
        data = meta.send_position()
        if data['status'] and data['data']:
            SendData(data, meta, config).request()
    return context

