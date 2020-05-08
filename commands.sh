virtualenv -p python3 .
pip install django==2.0.7
sudo apt install default-libmysqlclient-dev
pip install mysqlclient
mkdir src
cd src
django-admin startproject trackprice .
python manage.py runserver
python manage.py createsuperuser
# Username: jawad
# Email: jawad.siddiqui2011@gmail.com
# Password: abc123ABC 
python manage.py startapp sites

