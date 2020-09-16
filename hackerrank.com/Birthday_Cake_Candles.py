def birthdayCakeCandles(candles):
    tallest = 0
    count = 0
    for candle in candles:
        if candle > tallest:
            tallest = candle
            count = 1
        elif candle == tallest:
            count += 1
    return(count)
