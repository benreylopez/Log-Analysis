# Log-Analysis
Log Analysis Project from Udacity

Installation steps

1. Install Vagrant and VirtualBox
    Vagrant - https://www.vagrantup.com/downloads.html
    VirutalBox - https://www.virtualbox.org/wiki/Downloads

2. Download fullstack-nanodegree-vm repository

Running the program steps

1. change directory to vagrant directory 
2. vagrant up
3. vagrant ssh (log into vm)
4. Use command psql -d news -f newsdata.sql to load database
    use the following commands to check if you can access the 'newsdata.sql' database. 
    -use \dt to see the tables in database
    
    psql news
    select * from articles;
    
    If you can seem the table of artcles then you have succesfully loaded the database.
    
5. Run python news_report.py 
