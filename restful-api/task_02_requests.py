#!/usr/bin/python3
"""
Module for interacting with the JSONPlaceholder API.

Contains two functions:
- fetch_and_print_posts(): fetches all posts and prints their titles.
- fetch_and_save_posts(): fetches all posts and saves them into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.

    Sends a GET request to the API and checks the status code.
    If the request is successful (200), converts the response to JSON
    and prints the title of each post.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code != 200:
        print("Error during the request")
        return

    print("Status Code:", response.status_code)
    data = response.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them to a CSV file.

    Sends a GET request to the API and checks the status code.
    If the request is successful (200), converts the response to JSON,
    creates a list of dictionaries containing id, title, and body,
    and writes this list into 'posts.csv'.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code != 200:
        print("Error during the request")
        return

    data = response.json()
    simplified_posts = []

    for post in data:
        post_dict = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        simplified_posts.append(post_dict)

    with open("posts.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for post in simplified_posts:
            writer.writerow(post)
