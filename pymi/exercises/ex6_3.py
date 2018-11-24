#!/usr/bin/env python3

import csv
import os
import time


def find_max_price(datafile):
    f = open(datafile)
    dr = csv.DictReader(f, ['time', 'price', 'UNKNOWN']) # NOQA
    result = None
    try:
        price_BTC_highest = 0
        time_BTC_highest = 0
        for row in dr:
            price = float(row['price'])
            if price > price_BTC_highest:
                price_BTC_highest = price
                time_BTC_highest = time.gmtime(int(row['time']))
        time_BTC_highest = time.strftime("%Y-%m-%d", time_BTC_highest)
        result = (time_BTC_highest, price_BTC_highest)
        return result

    finally:
        f.close()

    return


def solve():
    '''Tìm ngày giá BTC lên cao nht. Tr v Tuple cha ngày  đnh dng
    YYYY-mm-dd (VD: 2017-06-19) và giá VND ca 1 BTC
    '''
    # http://api.bitcoincharts.com/v1/csv/
    datafile = 'localbtcVND.csv'
    exdir = os.path.dirname(__file__)
    datapath = os.path.join(exdir, datafile)
    result = find_max_price(datapath)
    return result


def main():
    now = time.gmtime(int(time.time()))
    print(now.tm_year, now.tm_mon, now.tm_mday)
    print(solve())


if __name__ == "__main__":
    main()
