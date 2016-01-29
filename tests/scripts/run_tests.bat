

set PYTHONPATH=.

START /B python app.py --settings=tests/config/test_settings.json

python -m unittest discover tests
