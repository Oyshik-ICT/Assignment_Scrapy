# Hotel Scraper

This project is a web crawler built using Scrapy. The crawler scrapes hotel information from a specific website by first obtaining location data through an AJAX endpoint, selecting a random location, and then scraping hotel details such as title, images, rating, room type, price, and location. The scraped data is stored in a PostgreSQL database using SQLAlchemy.

## Project Structure

- `my_spider.py`: The main spider file containing the logic for making requests to the AJAX endpoint, selecting a random location, and scraping hotel information.
- `pipelines.py`: Handles the storage of scraped data into a PostgreSQL database using SQLAlchemy.
- `items.py`: Defines the data structure for the scraped items.
- `.env`: Contains environment variables, including the database connection string.
- `requirements.txt`: Lists the dependencies required to run the project.
- `.gitignore`: Specifies files and directories to be ignored by Git, including the virtual environment and `.env` file.

## How the Scraper Works

1. **Initial Request**: The spider sends a POST request to an AJAX endpoint to retrieve location data (including country name and location code).
2. **Random Location Selection**: From the retrieved locations, a random location is selected.
3. **Scraping Hotel Information**: The spider makes a request to the chosen location's URL and scrapes hotel data including the title, image sources, rating, room type, price, and location.
4. **Photo Directory Creation**: When the code is first run, a "photos" directory is created. For each randomly selected location, a subdirectory is created with the name of that location. During each iteration, the photos for each hotel are saved within this location directory, with filenames corresponding to the hotel names.
5. **Storing Data**: The scraped data is stored in a PostgreSQL database using SQLAlchemy. If a new country is scraped, a directory is created to store the hotel's images locally.

## Installation and Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- A PostgreSQL database with a user and password

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/hotel-scraper.git
   cd hotel-scraper
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   - Create a `.env` file in the root directory with the following content:
     ```
     DATABASE_URL=postgresql+psycopg2://<username>:<password>@localhost:5432/<database_name>
     ```
   - Replace `<username>`, `<password>`, and `<database_name>` with your PostgreSQL credentials.

5. **Create the Database Table**:
   - The table will be automatically created when the spider runs for the first time.

## Running the Spider

To start the spider and begin scraping:

```bash
scrapy crawl my_spider
```

## Notes

- Ensure that PostgreSQL is running and that the database specified in the `.env` file is accessible.
- The spider might require specific headers and cookies to successfully scrape the data. These are already set in `my_spider.py`.
