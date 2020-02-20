#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
from translate import replace_icelandic, clean_special_characets
import requests
import shutil

# parameter: html | returns: text without html tags


def renderHTML(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def create_folder(name):
    try:
        os.makedirs(name)
    except OSError:
        if not os.path.isdir(name):
            raise


# writes ONE movie to folder & file
# parameter: movie object | writes to file
def save_one_movie(movie, parent_folder_name):

    filename = replace_icelandic(
        replace_icelandic(
            clean_special_characets(movie.title.lower().replace(" ", "_"))
        )
    )
    file_extension = ".txt"

    directory = parent_folder_name + "/" + filename.encode("ascii", errors="ignore").decode() + "/"

    create_folder(directory)

    # save info!
    save_location = directory + filename + file_extension

    # save image!
    if movie.image.url is not "":
        save_one_image(movie.image.url, directory, movie.image.filename)

    # make a json copy!
    create_json_copy(movie, directory)

    with open(save_location, "w", encoding="utf-8") as f:
        f.write("Title: " + replace_icelandic(clean_special_characets(movie.title)))
        f.write("\n\n")
        f.write("Description: " + renderHTML(movie.content))
        f.write(
            "Image: "
            + "\n"
            + "url: "
            + movie.image.url
            + "\n"
            + "Filename: "
            + movie.image.filename
            + "\n"
            + "Title: "
            + movie.image.title
        )
        f.write("\n\n")
        f.write("Trailer URL: " + movie.trailerURL)
        f.write("\n\n")
        f.write("Playtime: " + movie.playtime)
        f.write("\n\n")
        f.write("Director: " + movie.director)
        f.write("\n\n")
        f.write("Producer: " + movie.producer)
        f.write("\n\n")
        if len(movie.otherCredits) > 0:
            f.write("Other credits: \n")
            for item in movie.otherCredits:
                f.write(item.role + ": " + item.name + "\n")


def save_one_image(url, path, image_filename):

    # This is the image url.
    image_url = url

    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)

    # Open a local file with wb ( write binary ) permission.
    with open(path + replace_icelandic(image_filename), "wb") as local_file:

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True

        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)

        # Remove the image url response object.
        del resp


def save_whole_year_to_folder(root_folder_name, movies):
    # Create folder with name folder_name
    create_folder(root_folder_name)

    # For each movie in that year, create folder & file
    for movie in movies:
        save_one_movie(movie, root_folder_name)

    print("Successfully saved all movies from year " + root_folder_name)


def create_json_copy(movie, directory):

    with open(directory + "data.json", "w") as json_file:
        json_file.write(movie.toJSON())
