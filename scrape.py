from bs4 import BeautifulSoup
import requests
import csv

f = open('movie_countr.csv', 'w')
writer = csv.writer(f)

movies = []
with open('movies.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        movie = []
        if row[3] != "" and row[2] != "":
          movie.append(row[2])
          movie.append(row[3])
          print(movie)
        movies.append(movie)

# movies = [["Sholay", "tt0073707"], ["War", "tt7430722"], ["Dhoom", "tt0422091"], ["Wish", "tt11304740"], ["Road House", "tt3359350"]] # A list of the movie names and IMDb IDs

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
className = "ipc-link ipc-link--base sc-43930a5b-3 igDZPp"

counter = 0

for movie in movies:
  if (len(movie) != 0):
    counter += 1
    url = "https://www.imdb.com/title/" + movie[1] + "/locations/?ref_=tt_dt_loc"
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, "html.parser")
    locations = soup.find_all("a", class_=className)
    countries = []
    
    for location in locations:
      countries.append(((location.text).split(", "))[-1])
    
    countries = list(set(countries))
    countries_str = ""
    
    for country in countries:
      countries_str += str(country) + "$"

    if (countries_str != ""):
      print(str(counter) + "/" + str(len(movies)) + "\t" + str(int(100 * counter/len(movies))) + "%\t" + str(movie[0]) + "\t" + str(countries))
      writer.writerow([movie[0], url, countries_str[:-1]])

f.close()