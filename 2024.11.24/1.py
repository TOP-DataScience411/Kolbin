def deck() -> tuple:
    nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
    suit = ["черви", "бубны", "пики", "трефы"]
    
    for s in suit:
        for nom in nominal:
            yield nom, s
            
            
# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]