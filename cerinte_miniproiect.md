## ⏮️ Ceas Digital – Varinata 1: miniproiect pilonii OOP / Varianta2: miniproiect web framework Django
Să se realizeze o aplicație care afișează ora curentă sub forma unui ceas digital în mod text, 
folosind caracterele _ și | astfel: 
Ora curentă se va afișa la interval de 1 secundă. Valorile mai mici de 10 vor fi precedate de un 0. 
Atenție la fusul orar, e posibil ca la ore să trebuiască adăugată o anumită valoare pentru a obține ora României.
Pentru separatorii dintre valori se va folosi caracterul 'o’.

Fiecare cifra din afișaj ar trebui să ocupe 4 caractere, iar punctele de separare - 3 caractere. 

## Varinata 1: miniproiect pilonii OOP - structura proiect

ClockDigitalApp14/
- clock-system - va fi un python package
  - __init__.py
  - clock.py 
  - clockDigital.py
- app.py -aici vom rula aplicatie

Plan:
```commandline
ClockDigitalApp14/
│
├── clock_system/  # Package pentru logica de ceas
│   ├── __init__.py
│   ├── clock.py  # Modul care gestionează ora și fusul orar
│   └── clockDigital.py  # Modul care transformă ora în cifre digitale din caractere
│
└── app.py  # Fisierul principal pentru a rula aplicația

```