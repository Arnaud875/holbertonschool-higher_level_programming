#!/usr/bin/python3
"""
Contains function to fetch data from jsonplaceholder website.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch data and print status code and title.
    """
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(req.status_code))

    if req.status_code == 200:
        for i in req.json():
            print(i['title'])


def fetch_and_save_posts():
    """
    Fetch data and save data(id, title, body) in csv file.
    """
    req = requests.get("https://jsonplaceholder.typicode.com/posts")

    if req.status_code == 200:
        with open("posts.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()

            for i in req.json():
                del i["userId"]
                writer.writerow(i)
