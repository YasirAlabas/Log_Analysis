LogAnalysis v.2.1

This programm is supposed to answer the following questions:

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

*In order to run the programme, follow the upcoming procedure:

1-downlod:
a. Vagrant:https://www.vagrantup.com/downloads.html
b. VirtualMachine:https://www.virtualbox.org/wiki/Downloads
c. Download a FSND virtual machine:https://github.com/udacity/fullstack-nanodegree-vm, which would include
d. database 'newsdata':https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
I reconmmend using a Unix based command prompet like Git Bash if you are using windows in order to run the programm.

2-After downloading the above softwares, change the directory('cd') to the directory were vagrant file is located, so if the file is located in a/b/c/vagrant directory you just type
'cd a/b/c/vagrant' in your command prompet.

3- after 'cding' to the vagrant file perform the following tasks in your command prompet:
vagrant up
vagrant ssh
cd /vagrant
mkdir log-analysis-projectcd
cd log-analysis-project

4-Move the “newsdata.sql” to your project folder “log-analysis-project”

5-type 'psql -d news -f newsdata.sql' in your command prompet to load the data

6-type 'psql -d news' to connect the database

7-Now the programm is ready to go! Just type 'python log.py' to see the results.

NOTE:The programm might take some time to load the results.
IMPORTANT NOTE: YOU MUST HAVE PYTHON INSTALLED IN YOUR COMPUTER TO RUN THE CODE, if you don't have it then download it from here:https://www.python.org/downloads/

By Yasir Alabas 