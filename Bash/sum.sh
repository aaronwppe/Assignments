#!/bin/bash

if [ "$#" -lt 1 ]; then
	echo "USAGE: $0 n1 [n2 [n3 [...]]]"
	exit 1
fi

sum=0

for n in "${@}";
do 
	sum=$(($sum + $n))
done

echo "$sum"
