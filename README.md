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