# Portfolio Analyser

[There might be a fair bit of tweaks needed as I have written this only for like 3-4 funds. There could be spreadsheet file format issues edge cases I might have missed while retrieving data. Take this with a pinch of salt. Write back to me and I will try to help if I can]



This is a simple python based portfolio analyser that determines how much of your money is invested in each company with following inputs from you :
  - Portfolio disclosure documents (or) portfolio document download urls[wouldn't recommend this though]
  - Units invested in each fund
  - MF api url for each fund
  - Sheet name in each file

# How to run it?

  - cd to the downloaded folder
  - Install the dependecies with:
   ```sh
$ pip install -r requirements.txt
```
  - Just fill in the details in Config.py
    - leave the user agent as is
    - destination is the folder where you have the portfolio disclosure documents
    - For figi api key visit https://www.openfigi.com/about/figi; Get one.
    - vist mf api for nav url
    - Filename should include file format as well for each files
    - sheet name would be the sheet name in respective files
    - download url is needed only if you need to download as well
    - units : units you hold
  - (Only if you need to download portfolio disclore documents as well) uncomment 'bulk_download(master_data, destination)' in main.py
  - run main.py

# Assumptions for retrieving the data :
  - Isin column is named "ISIN" [case ignored]
  - Weighntage column has a '%' or 'percent' as column name
  - Data lies between row that has a column that says "Listed" and the row that has a column that says "Total"
  