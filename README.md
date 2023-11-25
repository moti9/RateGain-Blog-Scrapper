

# RateGain Blog Scraper

## Overview

The RateGain Blog Scraper is a Python script designed to extract blog data from the [RateGain blog website](https://rategain.com/blog/). It leverages the BeautifulSoup library for web scraping and concurrent.futures for parallelizing the scraping process. The scraped data is stored in an Excel file using the Pandas library.

## Hackathon: Web Scraping Challenge

<p align="center">
  <img src="rategain.png" alt="RateGain">
</p>

This hackathon challenges participants to showcase their coding skills and creativity by solving a real-world problem: extracting valuable data from web pages.

### Task

The mission is to develop a program capable of extracting specific information from web pages. The target URL for this exercise is [RateGain Blog](https://rategain.com/blog).

The application must identify and collect data from numerous blog posts on this webpage. The task involves navigating through various pages to gather data comprehensively. The application should extract the following details:

- **Blog Title:** Capture the titles of the blog posts.
- **Blog Date:** Retrieve the publication dates of each blog post.
- **Blog Image URL:** Extract the URLs of the images associated with the blogs.
- **Blog Likes Count:** Record the number of likes each blog post has received.

### Data Management

The gathered data should be organized and saved efficiently. The preferred format for storage is either Excel or CSV. Ensure that the extracted data is accurately structured for easy analysis.

## Usage

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/moti9/RateGain-Blog-Scrapper.git
    cd RateGain-Blog-Scrapper
    ```

2. **Run the script:**

    ```bash
    python scrapper.py
    ```

## Installation

Before running the script, ensure that you have Python and pip installed on your machine. Install the required dependencies by executing the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Customization
We can customize the script to suit your needs. Here are a few things you might want to consider:

Adjust the headers in the headers variable to mimic a different user agent or handle anti-scraping measures.
Modify the `scrape_url` function to extract additional information from the blog posts if needed.


## Team(Destination)
Meet the awesome team behind the RateGain Blog Scraper:

- Team Member 1:
    -   Role: Developer
    -   GitHub: [VishnuSandeep1108](https://github.com/VishnuSandeep1108)

- Team Member 2:

    -   Role: Developer
    -   GitHub: [moti9](https://github.com/moti9)

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are highly appreciated.


---
*Disclaimer: The information provided in this README is for illustrative purposes and may not reflect the actual links or resources. Participants are encouraged to refer to the official documentation and resources provided by RateGain during the hackathon. Use the script responsibly and adhere to legal and ethical considerations when scraping data from websites.*

