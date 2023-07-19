#!/bin/bash

dir_list=( 01 02 03 04 05 )
for dd in ${dir_list[@]}; do
	cd ${dd}
	cp ../myclass.py ./
	cp ../generator.py ./
	echo 'Generating in' ${dd}
	python generator.py > netdata-${dd}.log
	rm myclass.py
	rm generator.py
	cd ../
done
