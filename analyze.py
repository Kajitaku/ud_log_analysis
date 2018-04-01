#!/usr/bin/env python

import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

print "1. What are the most popular three articles of all time?"

query_1 = (
    "select (select title from articles where slug = "
    "substr(log.path, 10)) as title, count(*) as pv from log "
    "where path <> '/' group by title order by pv desc limit 3"
    )
c.execute(query_1)
for row in c:
    print "\"{}\" - {} views".format(row[0], row[1])

print "\n2. Who are the most popular article authors of all time?"

join_2_1 = "inner join articles on substr(log.path, 10) = articles.slug"
join_2_2 = "inner join authors on articles.author = authors.id"
query_2 = (
    "select authors.name, count(*) as views from log "
    "{} {} "
    "group by authors.name order by views desc limit 5"
    ).format(join_2_1, join_2_2)
c.execute(query_2)
for row in c:
    print "{} - {} views".format(row[0], row[1])

print "\n3. On which days did more than 1% of requests lead to errors?"

subquery_3_1 = (
    "(select to_char(time, 'Mon DD, YYYY') as Date, count(*) as errors "
    "from log where status like '4%' group by Date)"
    )
subquery_3_2 = (
    "(select to_char(time, 'Mon DD, YYYY') as Date, count(*) as sum "
    "from log group by Date)"
    )
query_3 = (
    "select t1.Date, ROUND(t1.errors*100.0/t2.sum, 1) "
    "from {} as t1 inner join {} as t2 on (t1.Date = t2.Date) "
    "where ROUND(t1.errors*100.0/t2.sum, 1) >= 1.0"
    ).format(subquery_3_1, subquery_3_2)
c.execute(query_3)
for row in c:
    print "{} - {}% errors".format(row[0], row[1])
db.close()