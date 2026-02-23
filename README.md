# E-commerce Scraper

A Python script designed to extract book data (prices, titles, availability, and ratings) from the [Books to Scrape](http://books.toscrape.com/) website.

## ✨ Features

*   **Multi-Page Scraping:** Scrapes data from the first 5 pages of the catalogue.
*   **Data Extraction:** Scrapes product details like Title, Price, Availability, and Rating.
*   **CSV Export:** Saves the collected data into an `output.csv` file for easy use with tools like Excel or Pandas.

## 🚀 Getting Started

This section will guide you through setting up the project locally.

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation

A step-by-step guide on how to get a development environment running.

1.  Clone the repo
    ```sh
    git clone https://github.com/abhay1190/ecommerce-data-scraper.git
    ```
2.  Navigate to the project directory
    ```sh
    cd ecommerce_scraper
    ```
3.  Install the required Python packages:
    ```sh
    pip install requests beautifulsoup4 pandas
    ```

## Usage

To run the scraper, execute the `scraper.py` script from your terminal.

```sh
python scraper.py
```

This command will run the script, which scrapes data from `books.toscrape.com`. Upon completion, you will see a message "Scraping completed. Data saved to output.csv", and you will find the extracted data in the `output.csv` file.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request


## 📧 Contact

Project Link: https://github.com/abhay1190/ecommerce-data-scraper
