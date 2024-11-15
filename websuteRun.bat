@echo off
chcp 65001 > nul
rem Configura la página de códigos a UTF-8 para manejar caracteres especiales.

rem Definir las variables de conexión
set host=192.14.12.1      rem Dirección IP del servidor remoto (Ejemplo: 192.14.12.1)
set port=22               rem Puerto SSH (por defecto 22)
set usuario=root          rem Usuario para la conexión SSH (Ejemplo: root)
set contraseña=servidorssh rem Contraseña para la autenticación SSH (Ejemplo: "servidorssh")

rem Mostrar mensaje de conexión
echo Conectando a %usuario%@%host%:%port%...
echo.
echo.

rem Establecer conexión SSH y ejecutar comandos en secuencia
plink.exe -batch -P %port% %usuario%@%host% -pw %contraseña% "cd .. && cd facebook/pm2 status && pm2 stop faceboot && pm2 start facebook"

rem Finalizar el script
exit
