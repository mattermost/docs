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
if "%SPHINXOPTS%" == "" (
    set SPHINXOPTS=-j auto
)

if "%1" == "" goto help
if "%1" == "livehtml" goto livehtml
if "%1" == "linkcheck" goto linkcheck
if "%1" == "test" goto test
if "%1" == "compass-icons" goto compassicons

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

if not exist %BUILDDIR% md %BUILDDIR%
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O% -w "%WARNINGSFILE% 2>NUL
goto end

:livehtml
if not exist %BUILDDIR% md %BUILDDIR%
%SPHINXAUTOBUILD% %SOURCEDIR% %BUILDDIR%/html -d %BUILDDIR%/doctrees %SPHINXOPTS% %O%
goto end

:linkcheck
if not exist %BUILDDIR% md %BUILDDIR%
%SPHINXBUILD% -M linkcheck -D exclude_patterns=archive/*,process/* %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:test
pipenv run pytest
goto end

:compassicons
IF NOT EXIST source/_static/css MD source/_static/css
IF NOT EXIST source/_static/font MD source/_static/font
curl --no-progress-meter -o source/_static/css/compass-icons.css https://mattermost.github.io/compass-icons/css/compass-icons.css
curl --no-progress-meter -o "source/_static/font/compass-icons.#1" "https://mattermost.github.io/compass-icons/font/compass-icons.{eot,woff2,woff,ttf,svg}"
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
