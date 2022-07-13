# Django_assignment

## Local Setup

Install required package:

```
pip install -r requirements.txt
```



Run development server locally:

```
python manage.py runserver
```

Then navigate to http://localhost:8000

## Requests
Get all objects:
```
curl -X GET http://localhost:8000
```
Get all objects with name Product:
```
curl -X GET http://localhost:8000/detail/Product/ 
```
Get data from object with name Attribute and ID 9:
```
curl -X GET http://localhost:8000/detail/Attribute/9  
