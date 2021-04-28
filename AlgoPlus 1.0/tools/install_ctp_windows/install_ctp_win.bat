@echo off

del ..\..\src\AlgoPlus\CTP\*.cpp  /F

rd/s/q .\AlgoPlus
rd/s/q .\build
rd/s/q .\dist
rd/s/q .\AlgoPlus.egg-info

set nls_lang=SIMPLIFIED CHINESE_CHINA.UTF8
python setup.py build_ext --inplace
python setup.py install

del ..\..\src\AlgoPlus\CTP\*.cpp  /F
rd/s/q .\AlgoPlus
rd/s/q .\build
rd/s/q .\AlgoPlus.egg-info
pause