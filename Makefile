init:
	@echo "Installing from requirements"
	pip install -r requirements.txt

test:
	@echo "Running tests"
	py.test tests

.PHONY: init test

#install dependency and add to requirements
#usage: make pipinstall i="dependency-name"
pip-install:
	@echo "installing $i and adding to requirements"
	# if [ "$#" -eq  "0" ]
	# then
	# 	echo "No arguments supplied"
	# fi
	# else
	# 	echo "Hello world"
	# fi
	pip install $i && pip freeze | grep $i >> requirements.txt
helpme:
	@echo "run /"make init/" to install the programs requirements from requirements.txt"
	@echo "run \"make test\" to run the test files"
	@echo "run \"make pip-install i=\"dependency-name\"\" to install a requirement and add it to requirements.txt"


wtf:
	if [[ $# -ge 3 ]]; then
		echo script has at least 3 arguments
	fi