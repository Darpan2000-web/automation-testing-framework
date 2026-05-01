# 🚀 Automation Testing Framework (Python + Selenium)

## 📌 Overview

This project is a scalable test automation framework built using Python, Selenium, and PyTest. It automates login functionality of a web application and validates expected outcomes.

## 🧠 Features

- Page Object Model (POM) design pattern
- Automated login testing (valid & invalid scenarios)
- PyTest framework for execution
- HTML report generation
- Screenshot capture on failure
- Modular and maintainable structure

## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- PyTest

## ▶️ How to Run

```bash
python -m pytest --html=reports/report.html
```

## 📊 Output

- Reports → `reports/report.html`
- Screenshots → `screenshots/` (on failure)

## 📁 Project Structure

- tests/ → test cases
- pages/ → page objects
- utils/ → reusable utilities
- data/ → test data

## 🎯 Future Enhancements

- Data-driven testing (Excel/CSV)
- CI/CD integration
- Advanced reporting
- Cross-browser testing
