CS 348 Backend
==============

Never actually do this in real life


To create the database, first ensure you have Docker running, then run the following commands:

```
cd db/
docker build -t db .
docker run -it -p 5432:5432 db
```

SQL Wrapper 
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