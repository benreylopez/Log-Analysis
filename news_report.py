#! /usr/bin/env python

import psycopg2
DBNAME = "news"


def query_report(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

    # SQL Query to define:
    # what are the most popular three articles of all time?

popular_articles = """
  SELECT
    articles.title,
    COUNT(log.id) as views
  FROM
    articles, log
  WHERE
    log.path=CONCAT('/article/', articles.slug)
  GROUP BY
    articles.title
  ORDER BY
    views DESC
  LIMIT 3;
"""
# SQL Query to define:
# Who are the most popular article authors of all time?

popular_authors = """
  SELECT
      authors.name, count(*) as views
  FROM
    articles
  INNER JOIN
    authors on articles.author = authors.id
  INNER JOIN
    log on log.path LIKE CONCAT('%', articles.slug, '%')
  WHERE
    log.status
  LIKE
    '%200%'
  GROUP BY
    authors.name
  ORDER BY views DESC
"""
# SQL Query to define:
# On which days did more than 1% of requests lead to errors?

lead_errors = """
    SELECT
        *
    FROM (
        SELECT
            date(time),
        round(100.0*sum(case log.status
                        when '200 OK' then 0 else 1 end)/count
                        (log.status),3) as error
        FROM log
        GROUP BY
            date(time)
        ORDER BY
            error desc
    ) as subq
    WHERE
        error > 1;
"""

# Python code to print the title
print("1. The 3 most popular articles of all time are:" + "\n")
# Python code to print out report results
for report in query_report(popular_articles):
    print('%s - %s' % (report[0], report[1]) + " views" + "\n")

print("2. The most popular article authors of all time are:" + "\n")

for report in query_report(popular_authors):
    print('%s - %s' % (report[0], report[1]) + " views" + "\n")

print("3. Days with more than 1% of request that lead to an error:" + "\n")

for report in query_report(lead_errors):
    print('%s - %s' % (report[0], report[1]) + "% errors" + "\n")
