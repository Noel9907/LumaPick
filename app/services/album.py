import sqlite3
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()

api = os.getenv("GOOGLE_DRIVE_KEY")

class Albumlink(BaseModel):
    folderlink : str
    name:str

class Gallery(BaseModel):
    name: str

class Like(BaseModel):
    id: str


async def album(data : Albumlink):
    cursor.execute("""CREATE TABLE IF NOT EXISTS studio (id INTEGER PRIMARY KEY,file_id TEXT UNIQUE,name TEXT,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    link = data.folderlink
    m=link.find("folders/")
    l=link.find("?")
    print(link[m+8:l])
    name = data.name
    response = requests.get(f"https://www.googleapis.com/drive/v3/files?q='{link[m+8:l]}'+in+parents+and+mimeType+contains+'image/'&fields=files(id,name,mimeType)&key={api}").json()
    cursor.execute("""select * from studio""")
    for i in response["files"]:
        cursor.execute("""Insert OR IGNORE into studio(file_id,name) VALUES (?,?)""",(i["id"],name))
    conn.commit()
    cursor.execute("""select * from studio""")
    return(cursor.fetchall())

async def GetImage(data:Gallery):
    cursor.execute("""select * from studio where name = (?)""",(data.name,))
    i = cursor.fetchall()
    dic = []
    for img in i:
        dic.append(f"https://drive.google.com/thumbnail?id={img[1]}&sz=w1000")
    return(dic)


def likeImage(data: Like):
    cursor.execute("""CREATE TABLE IF NOT EXISTS like (id INTEGER PRIMARY KEY,file_id TEXT UNIQUE,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    cursor.execute("""INSERT OR IGNORE INTO  like(file_id) values (?)""",(data.id,))
    conn.commit()
    cursor.execute("""select * from like""")
    return(cursor.fetchall())

    
#download imaage : f"https://drive.google.com/uc?export=download&id={file_id}"
