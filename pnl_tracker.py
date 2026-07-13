def calculate_pnl(buy_price, sell_price, gas_fee):
    gross_profit = sell_price - buy_price
    net_profit = gross_profit - gas_fee
    return net_profit

# Example: Bought at 100, Sold at 120, Gas 5
result = calculate_pnl(100, 120, 5)
print(f"Net Profit: ${result}")
