Team "Birk and Socks:" Henry Gardner, Miller Hickman, and George Gardner
CSC210 Final Project
Prof. Zhupa
11/11/21

Apollo Music Platform

Folders:
    venv                 -> virtual enviornment  
    __pychache__         -> "compiled" python files
    src                  -> the main directory containing all of the source code
    src/static/*         -> folder containing the visuals used in display
    src/templates        -> folder containing all the client-side files



How to run:

Access the virtual ennviornment through:
	
	python3 -m venv venv

Then we need to activate the virtual enviornment via:

	. venv/bin/activate

Before we continue, make sure to install flask (and corresponding elements of flask) in this folder, complete this with the following command:
	
        pip3 install flask flask-sqlalchemy flask-login

Lastly, we need to initialize flask to our python file through the following command:

	export FLASK_APP=src

Now we can run the program by executing:

	flask run

