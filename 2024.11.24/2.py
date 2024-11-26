from collections.abc import Iterable

def product(iterable: Iterable[float]) -> float:
    it = list(iterable)
    if len(it) > 1:
        it[0] = float(it.pop(0) * it[0]) + 0
        return product(it)
    else:
        return it[0]
    
    
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# 0.0
# >>> product(range(10, 60, 10))
# 12000000.0