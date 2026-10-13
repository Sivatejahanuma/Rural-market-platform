def get_price_advice(crop_name):
    crop_name = crop_name.lower()

    # Simple mock average prices
    avg_prices = {
        "tomato": [22, 24, 26, 28, 30, 34],
        "onion": [42, 40, 38, 35, 32, 30],
        "paddy": [1850, 1880, 1900, 1920, 1910, 1920],
        "chilli": [110, 115, 120, 125, 130, 50]
    }

    # If crop not in database
    if crop_name not in avg_prices:
        return f"No historical data for {crop_name}. Try entering Tomato, Onion, Paddy, or Chilli."

    prices = avg_prices[crop_name]

    # Pure Python calculations
    current_price = prices[-1]
    avg_price = sum(prices) / len(prices)
    trend = prices[-1] - prices[0]  # last price - first price

    # Simple logic
    if current_price > avg_price and trend > 0:
        suggestion = "Price is rising. Good time to sell!"
    elif current_price < avg_price and trend < 0:
        suggestion = "Prices falling. Consider waiting if possible."
    else:
        suggestion = "Stable market. You may sell anytime."

    return (
        f"Crop: {crop_name.capitalize()}\n"
        f"Current Market Price: ₹{current_price}\n"
        f"Average Price: ₹{avg_price:.2f}\n"
        f"Trend: {'Upward' if trend > 0 else 'Downward'}\n"
        f"Recommendation: {suggestion}"
    )
