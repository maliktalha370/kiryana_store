# Kiryana Store

This repository contains an implementation of Sales Entry System for Kiryana Stores.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies for this project.
Preferably install requirements using:

```bash
pip install -r requirements.txt
```

## Usage
After installation of all libraries, run this application using this command:

```python
streamlit run login_page.py
```
This will run a streamlit page with login text bars. These bars need to be filled with credentials.

## Pages
- `login_page.py`: This page will handle login session for the user.
- `register_page.py`: This page will be used for registering new user.
- `Add_Product.py`: This page will add new products in the catalogue.
- `sales_entry.py`: This page will be the main front of the application where for every customer sales entry will be added and credit will be logged (If there's is any).
- `search_panel.py`: This page will return last 10 sales of the User and returns Credit / Udhar against that queried person. 


## Tools and Technologies:
- Streamlit
- Python
- PyCharm
- Google Cloud API. 