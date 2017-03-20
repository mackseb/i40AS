@echo off
del "%cd%\log\*.log"

start cmd /k python "%cd%\control_start.py"
start cmd /k python "%cd%\module_start.py"
start cmd /k python "%cd%\wsgi.py"
