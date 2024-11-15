@echo off 
chcp 65001 > nul
set host= ip servidor remoto (192.14.12.1)
set port=puerto servidor ssh
set usuario=root
set contraseña=servidorssh

echo Conectando a %usuario%@%host%:%port%...
echo.
echo.

rem Establecer conexión SSH y ejecutar comandos en secuencia en el servidor remoto
plink.exe -batch -P %port% %usuario%@%host% -pw %contraseña% "cd ..&& cd facebook/pm2 status && pm2 stop faceboot && pm2 start facebook"

exit
