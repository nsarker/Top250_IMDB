from __future__ import annotations

import csv

import requests
from bs4 import BeautifulSoup

def write_movies2(filename: str = "IMDb_Top_250_Movies_v2.csv") -> None:
    url = "https://www.imdb.com/chart/top/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    titles = soup.find_all("td", attrs="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")
    years = soup.find_all("span", class_="secondaryInfo")
    movieids = soup.find_all("td", class_="watchlistColumn")
    
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Movie title","Movie title with year", "Year","IMDb rating", "movieid"])
        for title, rating, year, movieid in zip(titles,ratings,years,movieids):
            writer.writerow([title.a.text, title.a.text+" " + year.text, year.text[:-1][1:], rating.strong.text, movieid.div['data-tconst']])


if __name__ == "__main__":
    write_movies2()
