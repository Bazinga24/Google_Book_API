import requests
from pprint import pprint
from django.shortcuts import render

API_KEY='AIzaSyCyF4BKUHwXuBGNHIfATPnqMamYe_kCkuE'
base_url = "https://www.googleapis.com/books/v1/volumes"

def fetch_books( category,val):

    if category=="title":
        query=f'intitle:{val}'
    elif category =="author":
        query=f'inauthor:{val}'
    elif category == 'category':
        query=f'subject:{category}' 
    else:
        return None    
    # Construct the query parameters
    params = {
        'q': query,
        'key': API_KEY,
    }
    
    # Make the request to the Google Books API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        books_data = response.json()
        book_list=[]
        for books in books_data["items"]:
            book=books["volumeInfo"]
            book_item={}

            # relevant information from the book 
            book_item["title"]= book['title']
            book_item["description"] = book['description']
            book_item['previewlink'] = book['previewLink']
            book_item["imagelink"] = book["imageLinks"]["smallThumbnail"]

            book_list.append(book_item)
        return book_list
    
    else:
        return None    
           

