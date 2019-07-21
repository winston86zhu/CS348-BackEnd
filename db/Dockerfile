FROM postgres:9.4

# Copy over schema files into entrypoint directory
# Upon startup, thse sql queries will all be run
COPY schema.sql /docker-entrypoint-initdb.d/
