#!/bin/bash

if [ "$1" ==  "" ] ; then 

echo "usage build.sh <tag>"
exit 1

fi


echo "tag: $1"

cp -pr ../toDoListPro toDoListPro 

docker build . -t $1


rm -rf tests
rm -rf toDoListPro
