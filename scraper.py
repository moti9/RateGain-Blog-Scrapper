# Import necessary libraries
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time
import pandas as pd

# Initialize variables to count good and faulty data
good_data = 0
faulty_data = 0

# Function to split a list into chunks
def chunksOfUrls(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

# Function to scrape data from a single URL
def scrape_url(url, blog_data):
    global good_data
    global faulty_data
    try:
        # Make a request to the URL
        response = session.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        blog_posts = soup.find_all('div', class_="wrap")

        for post in blog_posts:
            # Extract image data
            blog_img = post.find("div", class_="img")
            if blog_img:
                a = blog_img.find('a')
                blog_img = a['data-bg']
                good_data += 1
            else:
                # If no image data is found, mark as faulty
                faulty_data += 1
                continue

            # Extract other relevant data
            blog_title = post.find('h6').text
            blog_date = post.find('div', class_='blog-detail').find('span').text
            likes_count = post.find('a', class_='zilla-likes').text

            # Append data to the blog_data list
            blog_data.append([blog_title, blog_date, blog_img, likes_count])

        print(f"Done with URL: {url}")

    except requests.exceptions.RequestException as e:
        # Handle exceptions, print an error message
        print(f"Error loading URL {url}: {e}")



if __name__ == "__main__":
        
    # Set up headers and workbook
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    workbook = Workbook()
    sheet = workbook.active

    session = requests.Session()
    session.headers.update(headers)

    # Initialize start_time and blog_data
    start_time = time.time()
    blog_data = []

    # Get maximum page number
    url = "https://rategain.com/blog/page/1"
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    number_tags = soup.find_all("a", class_="page-numbers")
    maximum = max(int(num.text) for num in number_tags if num.text.isdigit())

    print("\nTotal Pages: ", maximum, "\n")

    # List of URLs
    base_url = "https://rategain.com/blog/page/"
    urls = [f"{base_url}{page}" for page in range(1, maximum + 1)]

    # Split the list of URLs into chunks
    chunk_size = 5
    url_chunks = list(chunksOfUrls(urls, chunk_size))

    # Scrape pages and fill the blog_data list using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(scrape_url, url, blog_data) for url_chunk in url_chunks for url in url_chunk]
        concurrent.futures.wait(results)

    # Create a DataFrame from blog_data
    df = pd.DataFrame(blog_data, columns=["Blog Title", "Blog Date", "Blog Img", "Likes Count"])

    # Write the DataFrame to an Excel file
    df.to_excel("blog_data.xlsx", index=False)

    print("\nGood Data: ", good_data, " Faulty Data: ", faulty_data, "\n")

    print(f"Finished in: {time.time() - start_time} sec\n")
