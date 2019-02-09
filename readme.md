weerstation poging met flask

in pycharm venv_tg aangeroepen in de settings 

Om flask te starten is het commando 
set FLASK_APP=weer_tg.py
en vervolgens:  flask run

om niet elke keer dat set commando te hoeven geven, 
is in de root nu een .flaskenv opgenomen met daarin het commando:
FLASK_APP=weer_tg.py
Nu is flask run voldoende om de server te starten

  