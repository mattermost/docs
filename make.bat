@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=pipenv run sphinx-build
)
if "%SPHINXAUTOBUILD%" == "" (
	set SPHINXAUTOBUILD=pipenv run sphinx-autobuild
)
set SOURCEDIR=source
set BUILDDIR=build
set WARNINGSFILE=%BUILDDIR%/warnings.log
set ERRORSFILE=%BUILDDIR%/errors.log
if not "%SPHINXOPTS%" == "" (
    set SPHINXOPTS=-j auto -w %WARNINGSFILE%
)

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O% 2>%ERRORSFILE%
goto end

:livehtml
%SPHINXAUTOBUILD% %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
