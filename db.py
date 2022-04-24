import sqlite3
import pandas as pd

#table = users_app_product

data = pd.read_csv('scrape/scraped_books.csv', index_col=0)
con = sqlite3.connect('db.sqlite3')
cursorObj = con.cursor()
for id, row in data.iterrows():
    com = f"INSERT INTO users_app_product(title,author,price,genre,description,image,likes) VALUES('{row[0]}','{str(row[1]).replace(',','')}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}')"
    #ADD "" outside strings!
    cursorObj.execute(com) 

# cursorObj.execute('DELETE FROM users_app_product;')
con.commit()

