def arbitrage(buy_order, sell_order, order):
    while True:
        if buy_order[0][0] - sell_order[0][0] > 10:
            size = min(buy_order[0][1], sell_order[0][1], 10)
            sell_order[0][1] -= size
            if(sell_order[0][1] == 0):
                sell_order.pop(0)
            buy_order[0][1] -= size
            if(buy_order[0][1] == 0):
                buy_order.pop(0)
            order.append({
                "type": "add",
                "symbol": sell_order["symbol"],
                "dir": "BUY",
                "price": sell_order[i][0],
                "size": size
            })
            order.append({
                "type": "convert",
                "symbol": buy_order["symbol"],
                "dir": "BUY",
                "size": size
            })
            order.append({
                "type": "add",
                "symbol": buy_order["symbol"],
                "dir": "SELL",
                "price": buy_order[i][0],
                "size": size
            })
        else:
            break
def strategy(message_vale, message_valbz):
    order = []
    arbitrage(message_vale, message_valbz, order)
    arbitrage(message_valbz, message_vale, order)
    return order
