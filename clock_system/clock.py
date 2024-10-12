"""
Vom crea functionalitatea aplicatiei pentru a obtine ora curenta
si vom formata datele tinand cont de cerintele proiectului
"""
import time


class Clock:
    # Constructor
    def __init__(self):
        self.ora_curenta = None

    # Metoda pentru a seta data curenta
    def get_ora_curenta(self):
        self.ora_curenta = time.localtime()

    # Metoda pentru a formata datele
    def format_ora_curenta(self):
        ora_curenta_formatata = f'{self.ora_curenta.tm_hour:02d}o' \
                                f'{self.ora_curenta.tm_min:02d}o' \
                                 f'{self.ora_curenta.tm_sec:02d}'
        return ora_curenta_formatata

    # Metoda pentru a afisa datele in formatul solicitat
    @staticmethod
    def display_clock(time_string):
        dict_clock = {
            '0': [' _ ',
                  '| |',
                  '|_|'],

            '1': ['   ',
                  '  |',
                  '  |'],

            '2': [' _ ',
                  ' _|',
                  '|_ '],

            '3': [' _ ',
                  ' _|',
                  ' _|'],

            '4': ['   ',
                  '|_|',
                  '  |'],

            '5': [' _ ',
                  '|_ ',
                  ' _|'],

            '6': [' _ ',
                  '|_ ',
                  '|_|'],

            '7': [' _ ',
                  '  |',
                  '  |'],

            '8': [' _ ',
                  '|_|',
                  '|_|'],

            '9': [' _ ',
                  '|_|',
                  '  |'],

            'o': ['   ',
                  ' o ',
                  '   ']
        }

        linie_output = ['', '', '']
        for caracter in time_string:
            if caracter in dict_clock:
                numar = dict_clock[caracter]
                for i in range(3):
                    linie_output[i] += numar[i] + '   '

        for rand in linie_output:
            print(rand)
