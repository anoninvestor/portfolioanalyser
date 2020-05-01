# scripts are blocked by some websites. This will let you through posing you as a browser
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

# Files have to be stored at ?
destination = "/home/user/Desktop/mf"

# figi api key
figi_api_key = ""

# stick to the following format or might encounter errors
master_data = \
    {"AxisLongTermEquity": {"download_url": "http://tiny.cc/MonthlyPortfolioMar20",
                            "file_name": "AXIS_MF.xlsb",
                            "sheet_name": "AXISTSF",
                            "nav_url": "https://api.mfapi.in/mf/120503",
                            "units": 100},

     "AxisSmallCap": {"download_url": "http://tiny.cc/MonthlyPortfolioMar20",
                      "file_name": "AXIS_MF.xlsb",
                      "sheet_name": "AXISSCF",
                      "nav_url": "https://api.mfapi.in/mf/125354",
                      "units":100},

     "MiraeAssetEmergingBlueChip": {
         "download_url": "https://www.miraeassetmf.co.in/docs/default-source/portfolios/mirae-asset-full-portfolio---march-2020.xlsx",
         "file_name": "mirae.xlsx",
         "sheet_name": "MAEBF",
         "nav_url": "https://api.mfapi.in/mf/118834",
         "units": 100},

     "MiraeAssetTaxSaver": {
         "download_url": "https://www.miraeassetmf.co.in/docs/default-source/portfolios/mirae-asset-full-portfolio---march-2020.xlsx",
         "file_name": "mirae.xlsx",
         "sheet_name": "MATSF",
         "nav_url": "https://api.mfapi.in/mf/135784",
         "units": 100},

     "InvescoIndiaContra": {
         "download_url": "https://invescomutualfund.com/docs/default-source/default-document-library/contracaf5e407eee8616aaa28ff00007d74af.xls?sfvrsn=d51d85c2_0",
         "file_name": "invesco.xls",
         "sheet_name": "Contra",
         "nav_url": " https://api.mfapi.in/mf/105460",
         "units": 100},

     "JMMulticap": {
         "download_url": "https://jmfinancialmf.com/CMT/Upload/ArticleAttachments/A49C5853-C27A-42C5-9703-699AFEACE164/Portfolio%20Disclosure%20as%20on%20March%2013%202020.xls",
         "file_name": "jm.xls",
         "sheet_name": "JMMSF",
         "nav_url": "https://api.mfapi.in/mf/109522",
         "units":100}
     }
