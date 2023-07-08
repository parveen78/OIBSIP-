import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin

def download_images(person_name, num_images):
    # Create a directory to store the downloaded images
    if not os.path.exists(person_name):
        os.makedirs(person_name)

    # URL encode the person's name for the Google search query
    query = quote(person_name)

    # Generate the Google Images search URL
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    # Send a GET request to the Google Images search URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the image elements in the HTML
    images = soup.find_all("img")

    # Download the specified number of images
    count = 0
    for image in images:
        if count == num_images:
            break
        try:
            image_url = image["src"]
            if not image_url.startswith("http"):
                image_url = urljoin(url, image_url)

            response = requests.get(image_url)
            response.raise_for_status()

            # Save the image to the local directory
            with open(f"{person_name}/{count+1}.jpg", "wb") as file:
                file.write(response.content)

            count += 1
        except Exception as e:
            print(f"Error downloading image {count+1}: {str(e)}")

    print(f"Downloaded {count} images of {person_name}.")

# Prompt the user to enter the person's name and number of images to download
person_name = input("Enter the person's name: ")
num_images = 50

# Call the function to download the images
download_images(person_name, num_images)



