@echo off
cd /d "D:\my ai therapist\model 1"
start cmd /k python therapist.py
timeout /t 5 >nul
start "" http://127.0.0.1:5000/
exit
