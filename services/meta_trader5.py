import MetaTrader5 as mt5
from datetime import datetime, timedelta



class MetaTrader5:

    def __init__(self) -> None:
        self.account = None
        self.password = None
        self.server = None
        self.path_terminal = None

    def send_data(self, data) -> dict:
        context = {}
        if self.authorize():
            context.update({
                'status': True,
                'message': None,
                'data': eval(data)
            })
        else:
            context.update({
                'status': False,
                'message': "failed to connect at account #{}, error code: {}".format(self.account, mt5.last_error()),
                'data': None
            }) 
        self.shutdown()
        return context
    
    def authorize(self) -> bool:
        if not mt5.initialize(path=self.path_terminal):
            return False
        authorized = mt5.login(self.account, self.password, self.server)
        return authorized
    
    @staticmethod
    def position_info() -> tuple:
        return mt5.positions_get()
    
    @staticmethod
    def shutdown() -> bool:
        mt5.shutdown()
        return True

    @staticmethod
    def account_info() -> dict:
        return mt5.account_info()._asdict()
    
    @staticmethod
    def get_equity() -> dict:
        return {'equity': MetaTrader5.account_info()['equity']}
    
    @staticmethod
    def orders_info() -> tuple:
        return mt5.orders_get()
    
    @staticmethod
    def filter_by_range_date(symbol=None, start=None, end=None) -> list:
        return mt5.copy_rates_range(symbol, mt5.TIMEFRAME_D1, start, end)
    
    @staticmethod
    def rate_date(symbol=None, date=None, num=None):
        return mt5.copy_rates_from(symbol, mt5.TIMEFRAME_H4, date, num)
    
    @staticmethod
    def get_symbol_info(symbol):
        info = mt5.symbol_info(symbol)._asdict()
        return MetaTrader5.edit_data_symbol(info)
    
    @staticmethod
    def edit_data_symbol(info):
        return {
            'name': info['name'],
            'volume': info['volume'],
            'time': info['time'],
            'bid': info['bid'],
            'bidhigh': info['bidhigh'],
            'bidlow': info['bidlow'],
            'ask': info['ask'],
            'askhigh': info['askhigh'],
            'asklow': info['asklow'],
            'trade_tick_value': info['trade_tick_value'],
            'trade_tick_value_profit': info['trade_tick_value_profit'],
            'trade_tick_value_loss': info['trade_tick_value_loss'],
            'session_open': info['session_open'],
            'session_close': info['session_close'],
            'margin_hedged': info['margin_hedged'],
            'currency_base': info['currency_base'],
            'currency_profit': info['currency_profit'],
            'currency_margin': info['currency_margin']
        }
    
    @staticmethod
    def order_history() -> tuple:
        return mt5.history_orders_get(datetime.now() - timedelta(days=115), datetime.now() + timedelta(days=1))
    
    @staticmethod
    def get_orders_by_position_id(position_id) -> tuple:
        return mt5.history_orders_get(position=position_id)
    
    @staticmethod
    def order() -> dict:
        context = {}
        data = MetaTrader5.order_history()
        for count in range(len(data)):
            order_list = []
            position = data[count]._asdict()['position_id']
            for i in range(2):
                order_list.append(MetaTrader5.get_orders_by_position_id(position)[i]._asdict())
            context.update({order_list[0]['ticket']: order_list})
        return context

