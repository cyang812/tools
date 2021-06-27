@echo OFF
 
:LOOP
 
	set index=%1
 
	if %index%! == ! goto END
 
	echo 	File name :	%index%	MD5	SHA1	SHA256
	echo.
	certutil -hashfile "%index%" MD5
	echo.
	certutil -hashfile "%index%" SHA1
	echo.
	certutil -hashfile "%index%" SHA256
	echo.
	echo.
 
	shift
 
	goto LOOP
 
:END
 
echo "Checksum ends."
 
pause