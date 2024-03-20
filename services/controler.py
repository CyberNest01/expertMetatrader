from services.meta_trader5 import MetaTrader5



class MetaTraderControler(MetaTrader5):

    def __init__(self, account: str, password: str, server: str, file_name: str) -> None:
        self.path_terminal = f'C:/Program Files/MetaTrader 5/{file_name}/terminal64.exe'
        self.account = account
        self.password = password
        self.server = server

    def send_equity(self) -> dict:
        return self.send_data("self.get_equity()")
    
    def send_account_info(self) -> dict:
        return self.send_data("self.account_info()")
    
    def send_position(self) -> dict:
        return self.send_data("self.position_info()")
    
    def get_symbol(self, symbol) -> dict:
        return self.send_data(f"self.get_symbol_info('{symbol}')")

    def send_order_history(self) -> dict:
        return self.send_data("self.order_history()")
    
    def orders(self) -> dict:
        return self.send_data("self.order()")
    
    def check_authorize(self) -> bool:
        authorize = self.authorize()
        self.shutdown()
        return authorize

    

    

