import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY= os.getenv("TMDB_API_KEY")


if not API_KEY:
    raise ValueError("TMDB_API_KEY not found")
else:
    print("Successful")


url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
    
}

response = requests.get(url, headers=headers)

data = response.json()

print(data["results"][0]["title"]) #1st movie
