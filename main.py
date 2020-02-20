#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from service import fetch_movies_by_year

# from filewrite import save_whole_year_to_folder
from filewrite import save_whole_year_to_folder, save_one_movie

years = [2019]


def get_all_movies(years):
    for year in years:
        movies = fetch_movies_by_year(year)
        save_whole_year_to_folder("../sarpur/" + str(year), movies)


get_all_movies(years)

# movies = fetch_movies_by_year(2010)
# save_one_movie(movies[4], "../Sarpur/" + str(2010))
