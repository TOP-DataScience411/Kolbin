def taxi_cost(length: int, waiting=0) -> int | None:
    total = 80
    if type(length).__name__ != "int" or type(waiting).__name__ != "int" or length < 0 or waiting < 0:
        return None
    if length == 0:
        total += 80 + waiting * 3
    elif length > 0:
        total += length / 150 * 6
        total += waiting * 3
    return round(total)
    
    
    
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))