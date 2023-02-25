@echo off
:a
SET mypath=%~dp0
SET /p comm=%mypath:~0,-1%^>
%comm%
GOTO a