from pathlib import Path
from sys import path
from csv import reader, writer


class CountableNouns:
    db_path = Path(path[0] + "\\words.csv")
    words = {}
    with open(db_path, newline='') as csvfile:
        word = reader(csvfile)
        for row in word:
            words[row[0]] = (row[1], row[2])
        
    @classmethod
    def pick(self, num, word):
        if word in self.words and num % 10 == 2:
            return self.words[word][0] 
        elif word in self.words and num % 10 == 5:
            return self.words[word][1] 
        elif word not in self.words:
            if num % 10 == 1:
                return word
            print(f'существительное "{word}" отсутствует в базе')
            self.save_words(word)
        
    @classmethod
    def save_words(self, word1=None):
        new_word_1 = word1 if word1 else input('  введите слово, согласующееся с числительным "один": ')
        new_word_2 = input('  введите слово, согласующееся с числительным "два": ')
        new_word_5 = input('  введите слово, согласующееся с числительным "пять": ')
        with open(self.db_path, "a", newline="") as csvfile:
            spamwriter = writer(csvfile, delimiter=",", lineterminator="\n")
            spamwriter.writerow([new_word_1, new_word_2, new_word_5])
        self.words[new_word_1] = (new_word_2, new_word_5)
        
        
    
# cn = CountableNouns()
# print(CountableNouns.pick(2, "есяц"))
# CountableNouns.save_words()
# print(CountableNouns.db_path.read_text(encoding='utf-8'))

# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(22, 'год')
# 'года'
# >>> CountableNouns.pick(365, 'день')
# 'дней'
# >>> CountableNouns.pick(21, 'попугай')
# 'попугай'
# >>> CountableNouns.pick(22, 'попугай')
# существительное "попугай" отсутствует в базе
  # введите слово, согласующееся с числительным "два": попугая
  # введите слово, согласующееся с числительным "пять": попугаев
# >>>
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
# >>>
# >>> CountableNouns.save_words()
  # введите слово, согласующееся с числительным "один": капля
  # введите слово, согласующееся с числительным "два": капли
  # введите слово, согласующееся с числительным "пять": капель
# >>>
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# попугай,попугая,попугаев
# капля,капли,капель