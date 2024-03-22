This is an example website put together to assist the students of IY4103 Website Development. Feel free to make use of code shown here for your assignment but remember that just copying and pasting this website will not be able to be counted as a proper submission. Make sure you take the code and work it into your own project and properly demonstrate to me that you understand how it works. 

You may need to install packages for this. You can do that by writing the following commands into the terminal:

pip install flask_sqlalchemy
pip install flask_migrate

Note: The above statements might be slightly different in your setup

To initialise, migrate and update your database:

flask db init
flask db migrate
flask db upgrade

Note: Again, the above statements might be slightly different in your setup. Make sure you run the statements in the folder containing app.py.