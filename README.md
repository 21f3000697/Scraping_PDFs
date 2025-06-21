# Scraping PDF Student Marks

This project automates the extraction and analysis of student marks from a PDF file containing tables of scores in various subjects (Maths, Physics, English, Economics, Biology) for multiple student groups.

## Purpose

EduAnalytics empowers Greenwood High School to:
- **Identify Performance Trends:** Quickly spot areas where students excel or need support.
- **Allocate Resources Effectively:** Direct teaching resources to groups and subjects that require attention.
- **Enhance Reporting Efficiency:** Reduce manual data processing time.
- **Support Data-Driven Strategies:** Use accurate data to improve student outcomes.

## Task Example
Calculate the total Economics marks of students who scored 79 or more in Economics in groups 1-30 (inclusive).

## How It Works
- Extracts all text from the PDF using `PyPDF2`.
- Uses regular expressions to find and parse tables for each group.
- Filters for groups 1-30 and students with Economics marks ≥ 79.
- Sums and reports the total marks for this cohort.
- Saves a detailed analysis to `economics_analysis_results.txt`.

## Requirements
- Python 3.7+
- pandas
- PyPDF2

Install dependencies with:
```bash
pip install pandas PyPDF2
```

## Usage
1. Place your PDF file (e.g., `q-extract-tables-from-pdf.pdf`) in the project directory.
2. Run the script:
   ```bash
   python app.py
   ```
3. The script will print the total Economics marks for the specified criteria and save detailed results to `economics_analysis_results.txt`.

## Output
- **Console:**
  - Total Economics marks (>=79) in groups 1-30
  - Number of students with Economics >=79
  - Average score
- **File:**
  - `economics_analysis_results.txt` with detailed scores and summary

## Customization
- To analyze other subjects or mark ranges, modify the filtering logic in `app.py`.
- To export results to CSV/Excel, use pandas DataFrame and its export functions.

## License
This project is for educational and analytical purposes. 