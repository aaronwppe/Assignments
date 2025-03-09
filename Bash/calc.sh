#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Usage: $0 [add|sub|mul|div]  num1 num2"
	exit 1
fi

op=$1

n1=$2
n2=$3

case "$op" in
	add)
		echo $((n1 + n2))
		;;

	sub)
		echo $((n1 - n2))
		;;
	
	mul)
		echo $((n1 * n2))
		;;

	div)
		if [ "$n2" -eq 0 ]; then
			echo "ERROR: Division by zero."
			exit 1
		fi

		echo $((n1 / n2))
		;;
	
	*)
		echo "ERROR: Invalid operation"
		;;
esac
