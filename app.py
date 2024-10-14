"""
In acest fisier vom rula aplicatia
sa din windows terminal: python app.py
"""
from clock_system.clockDigital import DigitalClockApp

if __name__ == "__main__":
    app = DigitalClockApp()
    app.run()
