```
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata ./api/seed/0001_geek.json
python3 manage.py loaddata ./api/seed/0002_products.json
python3 manage.py runserver

```
