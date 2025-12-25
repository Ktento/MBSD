@echo off
set PYTHON_VERSION=3.9.12
set PYTHON_DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
set INSTALLER_NAME=python-%PYTHON_VERSION%-amd64.exe

echo Downloading Python installer...
curl -O %PYTHON_DOWNLOAD_URL%

echo Installing Python...
start /wait %INSTALLER_NAME% /quiet InstallAllUsers=1 PrependPath=1

echo Cleaning up...
del %INSTALLER_NAME%

echo Python %PYTHON_VERSION% has been installed.

