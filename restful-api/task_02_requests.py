#!/usr/bin/python3
"""Module that consumes JSONPlaceholder posts using the requests library.

It provides:
- fetch_and_print_posts(): prints status code and titles of posts.
- fetch_and_save_posts(): saves posts (id, title, body) into posts.csv.
"""
import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print status code and post titles."""
    response = requests.get(URL, timeout=10)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save selected fields into posts.csv."""
    response = requests.get(URL, timeout=10)

    if response.status_code != 200:
        return

    posts = response.json()
    data = []
    for post in posts:
        data.append({
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        })

    with open("posts.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(data)
