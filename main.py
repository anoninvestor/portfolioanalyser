from Downloader import *
from AssetCalculator import fetch_total_value
from StockCalculator import *
from isindecoder import decode_isin
import collections


def run():

    # uncomment the following line if you need to download as well
    # bulk_download(master_data, destination)

    asset = fetch_total_value(master_data)
    stock_info = cumulate_stocks(asset, destination, master_data)
    sorted_stock_info = sorted(stock_info.items(), key=lambda kv: kv[1], reverse=True)
    stock_info = collections.OrderedDict(sorted_stock_info)

    for key in stock_info.keys():
        try:
            print(decode_isin(key) + " " + str(stock_info[key]))
        except KeyError:
             print("Probably openfigi api is not set.Retry with correct api key")




    print(stock_info)


run()