#!/usr/bin/env python3
import psycopg2

DBNAME = "news"

print('What are the most popular three articles of all time?')
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug) "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")
posts = c.fetchall()
for i in posts: 
  print i[0],
  print ':',  
  print i[1],  
  print 'views'
  

print('Who are the most popular article authors of all time?')
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug) where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")
posts = c.fetchall()
for i in posts: 
  print i[0],
  print ':',  
  print i[1],  
  print 'views'

print('On which days did more than 1% of requests lead to errors?')
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("select day, percintage from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "percintage from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by percintage desc) as final_query "
    "where percintage >= 1")
posts = c.fetchall()
for i in posts: 
  print(i[0]) 
db.close()
