from flask import Flask
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

# Define a function to generate URLs for freezing
@freezer.register_generator
def amenities_urls():
    # Replace 'amenities' with the endpoint name of your amenities route
    yield '/amenities'

if __name__ == '__main__':
    freezer.freeze()