#!/bin/bash

echo "Creating migrations..."
python manage.py makemigrations projectmanagement
echo "============================================"

echo "Applying migrations..."
python manage.py migrate
echo "============================================"

echo "Starting Django server on 0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000
