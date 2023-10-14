def strategy(message):
    order = []
    
    if len(message["buy"]) > 0 and message["buy"][0][0] > 1000:
        trade = {
            "type": "add",
            "symbol": "BOND",
            "dir": "SELL",
            "price": message["buy"][0][0],
            "size": 1
        }
        for i in range(message["buy"][0][1]):
            order.append(trade)
    elif len(message["sell"]) > 0 and message["sell"][0][0] < 1000:
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
            
