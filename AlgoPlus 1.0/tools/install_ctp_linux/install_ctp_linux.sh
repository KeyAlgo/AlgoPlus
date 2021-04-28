rm -rf ../../src/AlgoPlus/CTP/*.cpp

rm -rf  ./AlgoPlus
rm -rf  ./build
rm -rf  ./dist
rm -rf  ./AlgoPlus.egg-info

python setup.py build_ext --inplace
python setup.py install

rm -rf ../../src/AlgoPlus/CTP/*.cpp
rm -rf  ./AlgoPlus
rm -rf  ./build
rm -rf  ./AlgoPlus.egg-info