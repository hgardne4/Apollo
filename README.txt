Team "Birk and Socks:" Henry Gardner, Miller Hickman, and George Gardner
CSC210 Final Project
Prof. Zhupa
11/11/21

Apollo Music Platform

Hosted on GitHub.com in a public repository:
http://www.github.com/hgardne4/Apollo

Folders (inside the Apollo Directory):
    venv                 -> virtual enviornment  
    __pychache__         -> "compiled" python files
    src                  -> the main directory containing all of the source code
    src/static/*         -> folder containing the visuals used in display
    src/templates        -> folder containing all the client-side files

How to "run":

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

Upon executing the above command, open the output link to view our project!	

LOGIN INFORMATION:
Since this project has a login feature, you can test by creating a user and/or band account or use one of the following testing one's we have made:

	TEST USER ACCOUNTS:
		1. Account email:    test@gmail.com
		   Account password: test
		   Account name:     Foo
		2. Account email:    henry@gmail.com
		   Account password: henry
		   Account name:     Henry
		3. Account email:    miller@gmail.com
		   Account password: miller
		   Account name:     Miller
		4. Account email:    george@gmail.com
		   Account password: george
		   Account name:     George

	TEST BAND ACCOUNTS:
		1. Band email:    tame@gmail.com
		   Band password: tame
		   Band name:     Tame Impala
		2. Band email:    peach@gmail.com
		   Band password: peach
		   Band name:     Peach Pit
		3. Band email:    king@gmail.com
		   Band password: king
		   Band name:     King Gizzard and the Lizard Wizard
		4. Band email:    beach@gmail.com
		   Band password: beach
		   Band name:     Beach House

PROJECT MOTIVATION:
Each of the developers are very passionate about music, therefore, it was inevitable that we designed something to connect people to something music related. We sought to combine the idea of a social media platform with musical exploration, where users can interact with other fans and even bands! Band exposure, exploration, and so much more are offered in our platform.

PROJECT DEVELOPMENT:
When designing a project, it is always beneficial to put in the work early preparing the design before any coding. We brainstormed and discussed several architectural implementations before we settled on the final build. 

From a brief overview, it was clear that we needed an interaction between the front/back ends and a database to store important details. Using Python's Flask we were able to manage and scale these necessary tasks. For our database we went with SQLAlchemy due to the flexibility with Flask. 

Throughout the project lifecycle we divided the work among the developers such that there were "front end" and "back end" teams. Each was responsible for tasks that were eventually linked. The front end team was responsible for all the client-side displays using HTML, CSS, WTForms, etc. The back end team built the Python framework making sure to incorporate features like secure logins with Flask-Login, database management tools with Flask-SQLAlchemy, etc. 


CHALLENGES:
We have split up the challenges into sections.

Front End:
We originally started the project by having the front end team build the home page while the back end team developed the behind the scenes. The problem with this approach is that when we attempted to link them, there were significant issues in the styling. Therefore, it was a significantly tedius task to "fix" these styling features, especially because the front-end team built a 500+ line CSS file. 

Another challenge was familiarizing ourselves with the WTForm and HTML conditional statements. A lot of time was spent "messing around," so to speak, with these features to work around our needs. They ended up being incredibly important in displaying needed information and limiting the number of .html files through the power of the HTML conditional blocks.

The most difficult challenge in the front end development was the amount of tweaking necessary to be visually pleasing to our desires. The thing about web development is that it is never really done, so we spent a lot more time than necessary fixing the aesthetics that didn't really need changes. 

Back End: 
A lot of bugs and errors occured throughout the development of the back end, but the most significant follow. To start, there was a lot to learn in the development of secure login. We spent a long time reviewing the Flask-Login and Flask-SQLAlchemy documentation to understand how to link and update a database based on user login/signups. We ran into problems with the database initialization and how to properly format/create tables to store information. 

The biggest obstacle in developing with Flask-Login was that we had 2 different login types, so to speak. We wanted the ability to have both a user/fan and band login. However, the LoginManager in Flask-Login does not have a "login type" feature yet. We originally planned to have 2 login tables one for users and one for bands that would all be directed through the LoginManager, however, as this is not currently supported in Flask-Login, we modified the design to have one User table with a section indicating the account type. From here, we had another Band table that would have a foreign key of the user id (of those users that were account type bands) to have the same features we originally planned to develop, just using a work around. This particular challenge took a lot of creative thinking, but ended up working out potentially better than if LoginManager had the ability for login types.   

Another significant challenged faced was with the redirecting. We made several functions in the main.py and auth.py folders that corresponded to user redirects in the client-side. The problem with these is that we needed a way to redirect based on very specific input. Therefore, we had to make several functions redirect to similar pages when certain criteria were met. For example, the profile.html page needed a user id, but if the user wanted to go on their profile with extension /profile, we would get significant errors. As the user will never know their id that is stored in the table, this needed a work around. So, we created another redirect soley for the /profile extension that would redirect to which ever user is currently logged in. As one can tell from the description of this example, there were a lot of edge cases to handle when designing the redirects. 

The database design for multiple tables was a difficult task at first, but became very easy upon working through several examples/commits. Our current design has 5 tables: User, Band, Merchendise, Discography, and Blog. Each have their respective columns initialized to integer, string, etc. values that store important data about who is logged on, or back information that is used in the client-side display. We hard coded several foreign keys that would link tables together to perform necessary join statements. The difficulty in the table development came from editing the number of columns/column types and adding new tables. We ran into several exceptions and errors when making these changes because we forgot to delete the old database that was trying access data or data types that did not exist. Additionally, we had several problems adding to tables and creating new tables, but worked around this through the commit() the create_all() functions. 

Online Hosting:
Over the course of the project lifecycle some developers ran into several GitHub merge errors and clashes that required complete deletion of the local verion of the project. Therefore, it was super beneficial to update and commit changes periodically. 

WHAT'S NEXT:
As mentioned before, with web development, a project is never really done. There is always room to improve and develop/scale. Creating better visuals, interactions, etc. is a great place to start. Adding the ability to actually purchase items, instead of "mock purchasing" them, having the ability to upload songs in desired formats, have the user play a song, etc. are all features that we can continue to develop. What we have done is provided a good framework to scale and build before any release.

We are currently adding the platform to AWS and administering IAM users and roles to the current developers. 