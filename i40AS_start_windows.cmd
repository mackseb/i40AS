@echo off
del "%cd%\log\*.log"

start cmd /k python "%cd%\control_start.py"
start cmd /k python "%cd%\backend_start.py"
start cmd /k python "%cd%\frontend_start.py"
start cmd /k python "%cd%\wsgi.py"
