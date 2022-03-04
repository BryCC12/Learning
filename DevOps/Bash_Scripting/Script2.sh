#!/bin/bash

Name="Bry"
num=400
Result=$(ps -ef | grep bash)

echo $Name
echo $num
echo $Result

((num++))
((num+=2))

echo $num