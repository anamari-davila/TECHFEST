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


# for f in range(len(data["results"])):
#     print(data["results"][f]["title"]) #1st movie


print(data["results"][2])

print(    [(f"https://image.tmdb.org/t/p/original{data["results"][x]["poster_path"]}") for x in range(len(data["results"]))]
)