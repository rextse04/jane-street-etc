def strategy(message):
    order = []
    if len(message) == 0:
        return order
    if message["buy"][0][0] > 1000:
        trade = {
            "type": "add",
            "symbol": "BOND",
            "dir": "SELL",
            "price": message["buy"][0][0],
            "size": 1
        }
        for i in range(message["buy"][0][1]):
            order.append(trade)
    elif message["sell"][0][0] < 1000:
        trade = {
            "type": "add",
            "symbol": "BOND",
            "dir": "BUY",
            "price": message["sell"][0][0],
            "size": 1
        }
        for i in range(message["sell"][0][1]):
            order.append(trade)
    return order
            
