#!/usr/bin/env python

import psycopg2


def db_connect():
    """
    Creates and returns a connection to the database defined by DBNAME,
    as well as a cursor for the database.
    Returns:
        db, c - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    db = psycopg2.connect(database="news")
    c = db.cursor()
    return db, c


def execute_query(query):
    """
    execute_query takes an SQL query as a parameter.
    Executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    db, c = db_connect()
    c.execute(query)
    return c
    db.close()


def print_top_articles():
    """Prints out the top 3 articles of all time."""
    print "1. What are the most popular three articles of all time?"
    query = """
            SELECT title, count(*) AS pv
            FROM articles a INNER JOIN log l
            ON '/article/' || a.slug = l.path
            GROUP BY title, path
            ORDER BY pv DESC
            LIMIT 3;
            """
    results = execute_query(query)

    for row in results:
        print "\"{}\" - {} views".format(row[0], row[1])


def print_top_authors():
    """Prints a list of authors ranked by article views."""
    print "2. Who are the most popular article authors of all time?"
    query = """
            SELECT authors.name, count(*) AS views
            FROM log l INNER JOIN articles a
            ON '/article/' || a.slug = l.path
            INNER JOIN authors
            ON a.author = authors.id
            GROUP BY authors.name
            ORDER BY views DESC
            LIMIT 5;
            """
    results = execute_query(query)
    for row in results:
        print "{} - {} views".format(row[0], row[1])


def print_errors_over_one():
    """
    Prints out the days where more than 1%
    of logged access requests were errors.
    """
    print "3. On which days did more than 1% of requests lead to errors?"
    query = """
            SELECT to_char(t1.Date, 'FMMonth DD, YYYY'),
                 ROUND(t1.errors*100.0/t2.sum, 1)
            FROM (
            SELECT time::date AS Date, count(*) AS errors
            FROM log
            WHERE status LIKE '4%'
            GROUP BY Date
            ) t1
            INNER JOIN (
            SELECT time::date AS Date, count(*) AS sum
            FROM log
            GROUP BY Date
            ) t2
            ON t1.Date = t2.Date
            WHERE t1.errors*100/t2.sum > 1;
            """
    results = execute_query(query)

    for row in results:
        print "{} - {}% errors".format(row[0], row[1])

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
