CS 348 Backend
==============

Never actually do this in real life


To create the database, first ensure you have Docker running, then run the following commands:

```
cd db/
docker build -t db .
docker run -it db
```