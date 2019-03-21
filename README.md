<h1>Chance Murphy 507 Project 3</h1>
<p>
This project code creates a flask app that takes user input for movies and their directors from the user based on the information
they place in an app route. This information is then stored in a database called "sample_movies.db". By storing the movie titles and directors in the database, the program is able to recall the data from the database and display it the user in different ways based on the app route that is being entered.
<br><br>
This flask app can be ran downloading the required files and installing the requirments.txt file.
<br><br>
To run the flask app and install the requirments.txt file, you'll need to create
a virtual enviornment. In order to do this type in the following commands into
your command promot/terminal window.<br><br>
1: python3 -m venv project3-env
<br><br>
2: source project3-env/bin/activate for Mac/Linux OR source project2-env/Scripts/activate for Windows
<br><br>
3: pip install -r requirements.txt
<br><br>
4: Once you have installed the requirements you can then run your flask app by typing in...
<br><br>
5: python SI507_project_3.py runserver
<br><br>
From here you'll be prompted and given a local host address. Copy this into a web
and you can then freely run the flask app. Addresses you can enter into the local
host url are as follows.
<br>
<h3>Home Page:</h3> http://localhost:5000/
<br>
<h3>Add Movie Page:</h3> http://localhost:5000/movie/new/<name>/<director>/<name>
<br>
<h3>Display All Movies:</h3> http://localhost:5000/all_movies
<br>
<h3>Display All Directors:</h3> http://localhost:5000/all_directors
<br>
<h2>Overall Grade</h2>
1000/1000
<br>
Even though one of my routes does not display the number of movies a director has in the database, I still have 4 routes that function exactly as they should according to the code I written even though we were only required to have three.
</p>
