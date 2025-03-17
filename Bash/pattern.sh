#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "USAGE: $0 n"
	exit 1
fi


n="$1"

if [ $n -lt 1 ]; then
	echo "ERROR: Expected 'n = $n' > 0." 
	exit 1
fi

for ((i=1; i<=n; i++)); do
	for ((j=1; j<=i; j++)); do
		echo -n "$j "
	done

	echo ""
done
