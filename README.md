### drf_project
django, drf


### install
```sh
git clone https://github.com/asj214/drf_project.git && cd drf_project

cp .env.example .env

python -m venv .venv

. .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver_plus
```


### commands
```sh
# show urls
python manage.py show_urls

# fixture dumps
python manage.py dumpdata codes.Code --format=yaml > scripts/fixtures/codes.yaml

# fixture loads
python manage.py loaddata scripts/fixtures/codes.yaml

# test
```