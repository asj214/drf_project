### drf_project
django, drf


### links
- [노션](https://asj214.notion.site/Request-Example-97e8234608124cf7ade8a5bff06cf4db#62c06b8822734630882a9fb710d5aa38)

### install
```sh
git clone https://github.com/asj214/drf_project.git && cd drf_project

cp .env.example .env

python -m venv .venv

. .venv/bin/activate

# install packages
pip install -r requirements.txt

# migrations
python manage.py migrate

# fixture
sh init.sh

# run server
python manage.py runserver_plus
```


### commands
```sh
# show urls
python manage.py show_urls

# fixture dumps
python manage.py dumpdata users.User --format=yaml > scripts/fixtures/users.yaml

# fixture loads
python manage.py loaddata scripts/fixtures/users.yaml

# test
python manage.py test
```