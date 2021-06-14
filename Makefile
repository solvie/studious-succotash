.PHONY : setup run test

setup:
	pip3 install plotly pandas numpy --user

test:
	python3 -m unittest -v test/*.py

run: 
	python3 src/q_test_script.py
	