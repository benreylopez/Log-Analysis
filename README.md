# Log-Analysis
Log Analysis Project from Udacity

Installation steps

1. Install Vagrant and VirtualBox
2. Download or clone from github fullstack-nandegree-vm repository
3. Now we got newsdata.sql in our vagrant directory.

Running the program steps

1. change directory to vagrant directory 
2. vagrant up
3. vagrant ssh (log into vm)
4. Use command psql -d news -f newsdata.sql to load database
    -use \c to connect to database="news"
    -use \dt to see the tables in database
    -use \dv to see the views in database
    -use \q to quit the database
5. Run python news_report.py 
