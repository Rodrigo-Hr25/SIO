@echo off
setlocal

set "APP=%~1"
set "PORT=%~2"

set "FLASK_APP=%APP%/__init__.py"
set "FLASK_RUN_PORT=%PORT%"
set "FLASK_DEBUG=1"

flask run

endlocal