@ECHO OFF
ECHO Activate virtual environment..
CALL ..\..\venv\Scripts\activate
REM ECHO Change directory..
REM CHDIR .\whisper_demo
ECHO Run python app..
python app.py
@PAUSE