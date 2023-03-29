import requests, json
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


# GET Request to api and load response
#r = requests.get("",
#                 headers={"apikey": ""})
#print(r.text)

#r = requests.put("", headers={"apikey": ""})
#print(r.text)

#data = response.json()

posts_url = 'https://jsonplaceholder.typicode.com/posts'
comments_url = 'https://jsonplaceholder.typicode.com/comments'

posts_response = requests.get(posts_url)
comments_response = requests.get(comments_url)

posts_json = posts_response.json()
comments_json = comments_response.json()

df = pd.read_json(json.dumps(posts_json))
#df6 = df.rename(columns={'userID': 'user_id'})
df2 = df.drop('userId', axis=1)


print(df2)

# connect to PostgreSQL database
conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password=""
)

# create a cursor object
cur = conn.cursor()

# create table in PostgreSQL database
#cur.execute("""
  #  CREATE TABLE IF NOT EXISTS newPosts (
  #      column1 user_id,
  #      column2 id,
  #      column3 title,
  #      column4 body
  #  )
#""")
# insert DataFrame rows into PostgreSQL table
for index, row in df2.iterrows():
    cur.execute("""
        INSERT INTO posts (user_id, id, title, body)
        VALUES (%s, %s, %s, %s)
    """, (row['userId'], row['id'], row['title'], row['body']))

# commit changes to database
conn.commit()

# close cursor and database connection
cur.close()
conn.close()

response = requests.post("", headers={"apikey": ""})
print(response.text)
#json_obj = json.loads(posts)
#df = pd.DataFrame.from_records(json_obj)
#print(df)


#print(posts)
#print(comments)


