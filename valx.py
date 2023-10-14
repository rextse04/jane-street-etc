def arbitrage(buy_sym, buy_order, sell_sym, sell_order, order):
    while True:
        if len(buy_order) == 0 or len(sell_order) == 0:
            return False
        if buy_order[0][0] - sell_order[0][0] > 10:
            size = min(buy_order[0][1], sell_order[0][1], 10)
            order.append({
                "type": "add",
                "symbol": sell_sym,
                "dir": "BUY",
                "price": sell_order[0][0],
                "size": size
            })
            order.append({
                "type": "add",
                "symbol": buy_sym,
                "dir": "SELL",
                "price": buy_order[0][0],
                "size": size
            })
            sell_order[0][1] -= size
            if(sell_order[0][1] == 0):
                sell_order.pop(0)
            buy_order[0][1] -= size
            if(buy_order[0][1] == 0):
                buy_order.pop(0)
        else:
            break
def strategy(message_vale, message_valbz):
    order = []
    arbitrage("VALE", message_vale["buy"], "VALBZ", message_valbz["sell"], order)
    arbitrage("VALBZ", message_valbz["buy"], "VALE", message_vale["sell"], order)
    return order
