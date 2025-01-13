class ChessKing:
    files = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
    
    def __init__(self, color="white", square=None):
        self.color = color if color == "white" or color == "black" else "white"
        if square and square[0] in files and square[1] in ranks:
            self.square = square  
        else:
            if color == "white":
                self.square = "e1" 
            else:
                self.square = "e8"
                
    def __repr__(self):
        kings_color = self.color[0].upper()
        return f"'{kings_color}K: {self.square}'"
        
    def __str__(self):
        kings_color = self.color[0].upper()
        return f"{kings_color}K: {self.square}"
        
    def is_turn_valid(self, new_pos):
        if new_pos[0] in self.files and new_pos[1:] in self.ranks:
            dif_pos_files = self.files[self.square[0]] - self.files[new_pos[0]]
            dif_pos_rank = self.ranks[self.square[1:]] - self.ranks[new_pos[1:]]
            if -1 <= dif_pos_files <= 1 and -1 <= dif_pos_rank <= 1:
                return True
            else:
                return False
        else:
            return False
        
    def turn(self, new_pos):
        if self.is_turn_valid(new_pos):
            self.square = new_pos
        else:
            raise ValueError
        
        
        

# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('e2')
# >>> wk
# 'WK: e2'
# >>> wk.turn('d4')
# Traceback (most recent call last):
  # File "<python-input-6>", line 1, in <module>
    # wk.turn('d4')
    # ~~~~~~~^^^^^^
  # File "C:\My\Учеба\Kolbin\Kolbin\2024.12.15\3.py", line 41, in turn
    # raise ValueError
# ValueError
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8