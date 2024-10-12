"""
In cadrul acestui fisier vom dezvolta functionalitatea
pentru a rula aplicatia
"""
import os
import time
from clock_system.clock import Clock


class DigitalClockApp:
    # Constructor
    def __init__(self):
        self.clock = Clock()

    # Metoda pentru a rula aplicatia
    def run(self):
        while True:
            self.clock.get_ora_curenta()
            formatare_ora_curenta = self.clock.format_ora_curenta()
            self.clock.display_clock(formatare_ora_curenta)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
