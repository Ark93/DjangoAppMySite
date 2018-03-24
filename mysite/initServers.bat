@echo off

echo iniciando servidores
echo cambiando de ambiente
call workon djangoDB
echo cambiando de directorio
cd C:\Users\santo\DjangoAppMySite\mysite
start initJupyter.bat
call python manage.py runserver
