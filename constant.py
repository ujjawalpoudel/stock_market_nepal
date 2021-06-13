from stock_name import *

from datetime import date
DATE_TODAY = date.today().strftime("%Y_%m_%d_%A")

WATCH_LIST_STOCK = COMMERCIAL_BANK +\
                DEVELOPMENT_BANK + \
                FINANCE + \
                HOTEL_AND_TOURISIM + \
                HYDROPOWER + \
                INVESTMENT + \
                LIFE_INSURANCE + \
                MICROFINANCE + \
                NON_LIFE_INSURANCE

COLUMN = [
    'Sector',
    'Market Price',
    '% Change',
    '52 Weeks High - Low',
    '180 Day Average',
    '120 Day Average',
    '1 Year Yield',
    'EPS',
    'P/E Ratio',
    'Book Value',
    'PBV',
    '% Dividend',
    '% Bonus',
    'Right Share'
]

FLOAT_COLUMN = [
    'Market Price',
    '180 Day Average',
    '120 Day Average',
    'P/E Ratio',
    'Book Value',
    'PBV'
]

PERCENTAGE_COLUMN = [
    '1 Year Yield',
    '% Change'
]

QUATER_REPORT_COLUMN = [
    'EPS',
    '% Dividend',
    '% Bonus'
]

RENAME_COL = {
    '% Change' : 'Change(%)',
    '180 Day Average' : '180(AVG)',
    '120 Day Average' : '120(AVG)',
    '% Dividend' : 'Dividend',
    '% Bonus' : 'Bonus',
    'Market Price' : 'MP',
    '1 Year Yield' : '1 Year(%)'
}

ARRANGE_COL = [
    'Stock',
    'Change(%)',
    'High',
    'Low',
    '180(AVG)',
    'MP',
    '120(AVG)',
    '1 Year(%)',
    'EPS',
    'P/E Ratio',
    'Book Value',
    'PBV',
    'Dividend',
    'Bonus',
    'Total',
    'Right Share',
]

# datataken = {"draw":3,"recordsTotal":49,"recordsFiltered":49,"data":[{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/sabsl'>SABSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/sabsl'>Sabaiko Laghubitta Bittiya Sanstha Limited<\/a>","shares":"2,060,273.00","paidup":"100.00","operationdate":"2017-07-14","paidupcap":"206,027,300.00","marketcap":"3,634,321,572.00","ltp":"1,764.00","date":"2021-06-10","DT_Row_Index":41},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/sdlbsl'>SDLBSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/sdlbsl'>Sadhana Laghubitta Bittiya Sanstha Limited<\/a>","shares":"2,569,804.00","paidup":"100.00","operationdate":"2017-10-30","paidupcap":"256,980,400.00","marketcap":"4,674,473,476.00","ltp":"1,819.00","date":"2021-06-10","DT_Row_Index":42},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/niclbsl'>NICLBSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/niclbsl'>NIC Asia Laghubitta Bittiya Sanstha Limited<\/a>","shares":"17,394,400.00","paidup":"100.00","operationdate":"2017-11-21","paidupcap":"1,739,440,000.00","marketcap":"28,126,744,800.00","ltp":"1,617.00","date":"2021-06-10","DT_Row_Index":43},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/mlbsl'>MLBSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/mlbsl'>Mahila Laghubitta Bittiya Sanstha Limited<\/a>","shares":"1,000,000.00","paidup":"100.00","operationdate":"2018-10-18","paidupcap":"100,000,000.00","marketcap":"5,188,000,000.00","ltp":"5,188.00","date":"2021-06-10","DT_Row_Index":44},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/akbsl'>AKBSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/akbsl'>Adhikhola Laghubitta Bittiya Sanstha Limited<\/a>","shares":"1,000,000.00","paidup":"100.00","operationdate":"2017-02-12","paidupcap":"100,000,000.00","marketcap":"465,000,000.00","ltp":"465.00","date":"2019-12-19","DT_Row_Index":45},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/uslb'>USLB<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/uslb'>Unnati Sahakarya Laghubitta Bittiya Sanstha Limited<\/a>","shares":"1,761,698.00","paidup":"100.00","operationdate":"","paidupcap":"176,169,800.00","marketcap":"3,930,348,238.00","ltp":"2,231.00","date":"2021-06-10","DT_Row_Index":46},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/klbsl'>KLBSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/klbsl'>Kisan Laghubitta Bittiya Sanstha Limited(Former NRN Laghubitta Bittiya Sanstha Limited)<\/a>","shares":"3,928,088.00","paidup":"100.00","operationdate":"","paidupcap":"392,808,800.00","marketcap":"6,481,345,200.00","ltp":"1,650.00","date":"2021-06-10","DT_Row_Index":47},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/aclbsl'>ACLBSL<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/aclbsl'>Aarambha Chautari Laghubitta Bittiya Sanstha Limited<\/a>","shares":"2,867,631.00","paidup":"100.00","operationdate":"","paidupcap":"286,763,100.00","marketcap":"4,588,209,600.00","ltp":"1,600.00","date":"2021-06-10","DT_Row_Index":48},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/snlb'>SNLB<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/snlb'>Sarathi Nepal Laghubitta Bittiya Sanstha Limited<\/a>","shares":"2,545,187.00","paidup":"100.00","operationdate":"","paidupcap":"254,518,700.00","marketcap":"4,390,447,575.00","ltp":"1,725.00","date":"2021-06-10","DT_Row_Index":49}]}

# for x  in datataken['data']:
#     import re

#     s = x['symbol']
#     result = re.search('>(.*)<', s).group(1)
#     print(f"'{result}',")

# data_asscending = OTHER
# print(len(data_asscending))
# for x in sorted(data_asscending, reverse=False):
#     print(f"'{x}',")