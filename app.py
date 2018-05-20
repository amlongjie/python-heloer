from crawler.crawler_api import do_crawler
from opdb import database


# do crawler
print do_crawler("http://www.baidu.com")

# db
db = database.Connection(host="127.0.0.1",
                         database='',
                         user='',
                         password='123456')
# query one
db.get()
# query many
db.query()
# update and return count
db.execute_rowcount()

