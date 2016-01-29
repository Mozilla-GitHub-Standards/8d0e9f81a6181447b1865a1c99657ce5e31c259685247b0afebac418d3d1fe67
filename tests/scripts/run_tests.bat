
set PYTHONPATH=.

START /B python app.py

python -m unittest discover tests
