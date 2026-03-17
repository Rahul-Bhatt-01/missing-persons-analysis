# 🔍 Delhi Police Missing Persons — Data Scraping & Analysis

A data science project that scrapes, collects, and analyzes missing persons records from the **Delhi Police official website**. This repository contains a Selenium-based web scraper, an API-based data collection script, and a Jupyter Notebook with full exploratory data analysis (EDA).

---

## 📁 Repository Structure

```
├── main.py                  # Selenium-based scraper for Delhi Police missing persons portal
├── analysis.ipynb           # Jupyter Notebook with full EDA and visualizations
├── data.jsonl               # Raw scraped data (JSONL format, collected via API)
└── README.md
```

---

## 📌 Project Overview

Missing persons data is publicly listed on the [Delhi Police website](https://zipnet.delhipolice.gov.in/Victims/MissingPersons). This project attempts to:

1. **Scrape** the missing persons listings using browser automation (Selenium)
2. **Collect** structured data via the underlying API in JSONL format
3. **Analyze** the data to uncover trends — age groups, gender distribution, time patterns, area-wise statistics, and more

---

## 🗂️ File Descriptions

### `main.py` — Selenium Scraper

A browser-automation script built with **Selenium WebDriver** that navigates the Delhi Police missing persons portal and extracts records page by page.

**Features:**
- Automated pagination through multiple pages of listings
- Extracts key fields per missing person entry (name, age, gender, area, date reported, etc.)
- Saves data incrementally to avoid data loss on failure

**Known Issue:**
> The scraper currently works successfully for **2–3 pages** before encountering an error (likely due to dynamic content loading, CAPTCHA triggers, or session timeouts on the Delhi Police website). A fix/workaround is a work in progress.

**Dependencies:**
```
selenium
webdriver-manager
```

**Usage:**
```bash
pip install selenium webdriver-manager
python main.py
```

> Make sure you have **Google Chrome** installed. The script uses ChromeDriver managed automatically via `webdriver-manager`.

---

### `data.jsonl` — API-Collected Dataset

This file contains structured missing persons records collected directly through the **Delhi Police API endpoint** (discovered via browser network inspection).

Each line is a valid JSON object representing one record. Example fields may include:

```json
{
  "name": "...",
  "age": "...",
  "gender": "...",
  "district": "...",
  "date_of_missing": "...",
  "police_station": "...",
  ...
}
```

The JSONL format allows easy streaming and line-by-line processing.

---

### `analysis.ipynb` — Exploratory Data Analysis

A Jupyter Notebook that loads the JSONL dataset and performs comprehensive analysis.

**Analysis includes:**
- 📊 Distribution of missing persons by **age group**
- 🚻 **Gender-wise** breakdown
- 🗺️ **District/area-wise** analysis — which parts of Delhi report the most cases
- 📅 **Time-series trends** — missing cases over months/years
- 🚓 **Police station-wise** case counts
- 🔎 Insights and observations drawn from the data

**Dependencies:**
```
pandas
matplotlib
seaborn
jupyter
```

**Usage:**
```bash
pip install pandas matplotlib seaborn jupyter
jupyter notebook analysis.ipynb
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- Google Chrome (for Selenium scraper)
- Jupyter Notebook or JupyterLab

### Install all dependencies
```bash
pip install selenium webdriver-manager pandas matplotlib seaborn jupyter
```

---

## ⚠️ Known Issues & Limitations

| Issue | Details |
|-------|---------|
| Scraper fails after 2–3 pages | Likely caused by session expiry, dynamic JS rendering, or anti-bot measures on the Delhi Police portal |
| Data completeness | The JSONL dataset was collected via API and reflect the full database till 15-feb-2026 |
| Website changes | The Delhi Police website structure may change, breaking the scraper |

---

## 🔧 Future Work

- Fix Selenium pagination issues
- Automate dataset updates
- Build dashboard using Plotly / Power BI
- Apply Machine Learning models for pattern detection

---

## 📊 Data Source

- **Source:** [Delhi Police Official Website](https://zipnet.delhipolice.gov.in/Victims/MissingPersons)
- **Data Type:** Publicly available missing persons records
- **Collection Method:** Selenium browser automation + API endpoint

> **Disclaimer:** This data is used solely for educational and analytical purposes. All information is publicly available on the Delhi Police website. No private or sensitive information beyond what is publicly disclosed has been collected.

---

## 🙋 Author

**Rahul Bhatt**
- GitHub: [@Rahul-Bhatt-01](https://github.com/Rahul-Bhatt-01)

---

## 📄 Disclaimer

This project is created for **educational and analytical purposes only**.  
All data belongs to the respective government authorities.