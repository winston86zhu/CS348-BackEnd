CS 348 Backend
==============

Never actually do this in real life


Setup
-----

To build and run the backend, ensure you have Docker and docker-compose installed. Then run

```
docker-compose up -d --build
```

and you should have two containers running. Postgres (the database) on `<host_ip>:5432` and the API on `<host_ip>:5000`.


SQL Script 
===============
Python file @: `perfectparty\app\extensions\main_backend.py`

python command 
- selection
    + Attributes are dilimited by comma
    + Format for where: {\"attribute\" : <value>}
        - Special e.g. "{\"userid\" : 3}" 
```
python3.7 main_backend.py -c select -t <table> -s <selected attribute> -w <where clause>

python3.7 #main_backend.py -c select -t user -s FirstName,LastName -w "{\"userid\" : 3}"
```

- Insertion

```
main_backend.py -c insert -t <tablename> <attr1,attr2,attr3...>

python3.7 main_backend.py -c insert -t user "2,andr,tam,123,qqq@uwaterloo.ca"

```
- Delete
    + Delete all records
    + Delete selected records (using where)
```
python3.7 main_backend.py -c delete -t <tablename> 
python3.7 main_backend.py -c delete -t <tablename> <key>

#main_backend.py -c delete -t user userid=1
```

- Update 
    -Add `'\str\'` for string
```
python3.7 main_backend.py -c update -t <tablename> <key> <new_value> 
#python3.7 main_backend.py -c update -t "user" FirstName=\'win\' UserID=2
```
