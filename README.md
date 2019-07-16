CS 348 Backend
==============

Never actually do this in real life


Setup
-----

To build and run the backend, first ensure you have Docker installed and running. Then follow the steps below:

```
docker build -t db db/.
docker run -it -p 5432:5432 db

docker build -t perfectparty perfectparty/.
docker run -it -p 5000:5000 perfectparty
```

Now you should have two containers running: Postgres (the database) on `<host_ip>:5432` and the API on `<host_ip>:5000`!