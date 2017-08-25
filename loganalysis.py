# Python Program to query the tables and views used as part of log analysis
# !/usr/bin/python3
import psycopg2
DBNAME = "news"
Q1 = "What are the most popular three articles of all time?"
Q2 = "Who are the most popular article authors of all time?"
Q3 = "On which days did more than 1% of requests lead to errors?"


def get_articles():
    """Queries the DB and prints all the log data."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, views from popular_articles limit 3")
    answer1 = c.fetchall()
    c.execute("Select name, sum(views) from popular_articles group by name" +
              " order by sum desc")
    answer2 = c.fetchall()
    c.execute("select date,percentage from error_log where percentage>1")
    answer3 = c.fetchall()
    db.close()
    print (Q1)
    for row in answer1:
        print ("\""+row[0] + "\"" + " - ", row[1], " views")
    print (Q2)
    for row in answer2:
        print (row[0] + " - ", row[1], " views")
    print (Q3)
    for row in answer3:
        print (row[0] + " - ", round(row[1], 2), "% errors")
get_articles()
