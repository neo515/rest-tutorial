#!/bin/bash

source /Library/Frameworks/Python.framework/Versions/3.8/bin/virtualenvwrapper.sh
workon haina

pip3 -V
python -V

#nohup ./manage.py runserver 0.0.0.0:8000 >> svc.log 2>&1 &
./manage.py runserver 0.0.0.0:8000
