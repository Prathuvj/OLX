# 🔍 OLX Car Cover Scraper

This Python script scrapes search results for **"Car Cover"** listings from [OLX India](https://www.olx.in/items/q-car-cover), extracting:

* **Title**
* **Price**
* **Location**

The data is saved into a CSV file: `olx_car_covers.csv`.

---

## 📆 Features

* Uses **Selenium WebDriver** to handle dynamic JavaScript content on OLX.
* Headless browser mode for fast and silent operation.
* Outputs results to a clean, ready-to-use `.csv` file.

---

## ⚙️ How It Works

1. Opens the OLX search page for "Car Cover".
2. Waits for the page to fully load using `time.sleep()`.
3. Locates each listing using CSS selectors.
4. Extracts title, price, and location from each item.
5. Saves all results into a CSV file using `pandas`.

---

## 🚀 Setup Instructions

### 1. Clone or Download the Script

```bash
git clone https://github.com/your-username/olx-car-cover-scraper.git
cd olx-car-cover-scraper
```

Or simply copy `scrape_olx_car_covers.py` to your project folder.

### 2. Install Dependencies

Make sure you have Python 3.7+ installed, then install the required packages:

```bash
pip install selenium pandas
```

### 3. Install ChromeDriver

Download ChromeDriver from the [official site](https://sites.google.com/chromium.org/driver/):

* Make sure the version matches your installed version of Google Chrome.
* Add the ChromeDriver binary to your system `PATH`, or update the script like this:

```python
from selenium.webdriver.chrome.service import Service
service = Service("/path/to/chromedriver")  # Update this line
```

### 4. Run the Script

```bash
python scrape_olx_car_covers.py
```

After a few seconds, it will generate a file:

```
olx_car_covers.csv
```

---

## 📁 Output Format

The CSV file will contain:

| Title                    | Price | Location  |
| ------------------------ | ----- | --------- |
| Car Cover for Maruti 800 | ₹500  | Mumbai    |
| Waterproof Car Cover     | ₹999  | Bengaluru |

---

## ❗ Notes

* OLX's page structure may change — update the CSS selectors accordingly.
* Avoid making too many repeated requests to prevent being blocked.
* Intended for **educational/personal use** only. Respect OLX’s terms of service.

---

## 🪠 Troubleshooting

* **ChromeDriver not found**: Make sure it's installed and added to PATH.
* **Empty CSV file**: Ensure OLX hasn’t changed their HTML structure. Try increasing `time.sleep()`.
