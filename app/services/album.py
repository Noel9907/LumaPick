import requests
import os
from dotenv import load_dotenv
load_dotenv()

api = os.getenv("GOOGLE_DRIVE_KEY")
def home():
    t = "https://drive.google.com/drive/folders/16OctDipLvelBRxmwD6eevZ60AAym6gsO?usp=sharing"
    m=t.find("folders/")
    l=t.find("?")
    response = requests.get(f"https://www.googleapis.com/drive/v3/files?q='{t[m+8:l]}'+in+parents+and+mimeType+contains+'image/'&fields=files(id,name,mimeType)&key={api}")

    return(response.json())