@echo off
del "%cd%\log\*.log"

start /b python "%cd%\control_start.py"
start /b python "%cd%\module_start.py"
start /b python "%cd%\wsgi.py"
