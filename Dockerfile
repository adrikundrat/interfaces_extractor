FROM python:3.9
ADD sql_dump/table.sql /docker-entrypoint-initdb.d/