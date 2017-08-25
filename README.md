# Log Analysis

This project is a **internal reporting tool** that will use information from the database to discover the articles and authors the site's readers like.
## Design
1. This projects makes use of following tables and views
    **Tables**
          - Articles
           - Authors
           - Log
    **Views**
            - popular_articles
            - error_log
2. Python program `loganalysis.py` runs with following logic
        - it connects to the news database
        - it queries the views popular_articles and error_log based on the questions
        - it loops and prints the data based on the output format
### Pre-Requirements
1. Linux VM with vagrant. [Click here if not installed](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
2. News Tables needs to be loaded. Implement the following steps if not already installed
    - [Click here to download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    - After downloading, unzip and place the `newsdata.sql` inside vagrant.
    - run the command `psql -d news -f newsdata.sql` and load the data.
3. Create a githib account and Install git in the local machine. [Click here, if not already installed](http://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
## Installation Steps
1. Fork the github repository. The original repository can be found [here](https://github.com/vishyarjun/ArjunsPortfolio.git)
2. Open Terminal and change directory to Vagrant
3. Clone it to local repository using  `git clone <fork repository url>`
6. Run `vagrant up` and `vagrant ssh`
6. Run the command `cd /vagrant/loganalysis`
7. Run the command `psql news`
8. Execute the following code to create views
    - popular_articles
    ```
    create view popular_articles as Select authors.name,articles.title,logs.views from articles join (select replace(path,'/article/','') as slug, count(path) as views from log where path like '%/article%' group by path order by views desc) as logs on articles.slug=logs.slug join authors on articles.author=authors.id order by views desc;
    ```
    - error_log
    ```
    create view error_log as Select to_char(errlog.date, 'FMMonth FMDD, YYYY')as     date,errlog.count as error_count,logs.count as total_count,((errlog.count*100.00)/logs.count) as percentage  from (select cast(time as DATE) as date,count(*) as count from log where status like '%404%' group by CAST(time as DATE)) as errlog join (select cast(time as DATE) as date,count(*) as count from log group by CAST(time as DATE)) as logs on errlog.date=logs.date;
    ```
### FAQ
1. __How do I run the project?__
 - Open the Terminal window where vagrant is up and running.
 - Exit from psql
 - Run the program with the command `python3 loganalysis.py`

### Reference
1 [stackoverflow](www.stackoverflow.com)
2 [PostgreSQL](https://www.postgresql.org/docs/)
