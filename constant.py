from datetime import date
DATE_TODAY = date.today().strftime("%Y_%m_%d")

COMMERCIAL_BANK = [
    'NMB',
    'SBL',
    'NCCB',
    'KBL',
    'LBL',
    'MBL',
    'EBL',
    'NBB',
    'SBI',
    'HBL',
    'SCB',
    'NIB',
    'NABIL',
    'CZBIL',
    'PCBL',
    'SRBL',
    'ADBL',
    'SANIMA',
    'MEGA',
    'CBL',
]

DEVELOPMENT_BANK = [
    'MDB',
    'GBBL',
    'JBBL',
    'KRBL',
    'NABBC',
    'EDBL',
    'SADBL',
    'MNBBL',
    'CORBL',
    'SINDU',
    'SHBL',
    'SHINE',
    'GRDBL',
    'MLBL',
    'KSBBL',
    'LBBL',
    'SAPDBL',
]

FINANCE = [
    'NFS',
    'BFC',
    'LFC',
    'GFCL',
    'PFL',
    'UFL',
    'SIFC',
    'CFCL',
    'JFL',
    'SFCL',
    'CMB',
    'SFFIL',
    'GMFIL',
    'ICFC',
    'CFL',
    'MPFL',
    'PROFL',
    'MFIL',
    'RLFL',
    'GUFL',
]

HOTEL_AND_TOURISIM = [
    'SHL',
    'TRH',
    'OHL',
    'CGH',
]

HYDROPOWER = [
    'NHPC',
    'BPCL',
    'CHCL',
    'AHPC',
    'SJCL',
    'SHPC',
    'RHPC',
    'RHPL',
    'BARUN',
    'UPPER',
    'AKPL',
    'CHDC',
    'API',
    'DHPL',
    'NGPL',
    'RADHI',
    'KKHC',
    'GHL',
    'HURJA',
    'UMHL',
]

INVESTMENT = [
    'CIT',
    'HIDCL',
    'NIFRA',
    'NRN',
]

LIFE_INSURANCE = [
    'NLICL',
    'NLIC',
    'LICN',
    'ALICL',
    'PLIC',
    'SLICL',
    'GLICL',
    'JLI',
    'PLI',
    'RLI',
]

MANUFACTURE_AND_PRODUCT = [
    'BNL',
    'NLO',
    'BNT',
    'UNL',
    'SRS',
    'HDL',
    'SHIVM',
]

MICROFINANCE = [
    'NUBL',
    'CBBL',
    'DDBL',
    'SWBBL',
    'NLBBL',
    'MMFDB',
    'FMDBL',
    'SMFDB',
    'RMDC',
    'SKBBL',
    'SLBBL',
    'KMCDB',
    'JSLBB',
    'MLBBL',
    'WOMI',
    'LLBS',
    'CLBSL',
    'VLBS',
    'FOWAD',
    'MERO',
]

NON_LIFE_INSURANCE = [
    'NICL',
    'HGI',
    'UIC',
    'EIC',
    'PIC',
    'NIL',
    'SIC',
    'IGI',
    'PICL',
    'LGIL',
    'SICL',
    'SIL',
    'NLG',
    'RBCL',
    'PRIN',
    'GIC',
    'SGI',
    'AIL',
]

OTHER = [
    'NFD',
    'NTC',
    'NRIC',
]

TRADING = [
    'STC',
    'BBC',
]

WATCH_LIST_STOCK = COMMERCIAL_BANK+DEVELOPMENT_BANK+FINANCE+HOTEL_AND_TOURISIM+HYDROPOWER+INVESTMENT+LIFE_INSURANCE+MANUFACTURE_AND_PRODUCT+MICROFINANCE+NON_LIFE_INSURANCE+OTHER+TRADING

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
    'Change(%)',
    'Stock',
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


# datataken = {"draw":1,"recordsTotal":2,"recordsFiltered":2,"data":[{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/stc'>STC<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/stc'>Salt Trading Corporation Limited<\/a>","shares":"1,918,646.00","paidup":"100.00","operationdate":"","paidupcap":"191,864,600.00","marketcap":"20,725,214,092.00","ltp":"10,802.00","date":"2021-06-10","DT_Row_Index":1},{"symbol":"<a href='https:\/\/www.sharesansar.com\/company\/bbc'>BBC<\/a>","companyname":"<a href='https:\/\/www.sharesansar.com\/company\/bbc'>Bishal Bazar Company Limited<\/a>","shares":"500,000.00","paidup":"100.00","operationdate":"","paidupcap":"50,000,000.00","marketcap":"3,311,500,000.00","ltp":"6,623.00","date":"2021-06-10","DT_Row_Index":2}]}

# for x  in datataken['data']:
#     import re

#     s = x['symbol']
#     result = re.search('>(.*)<', s).group(1)
#     print(f"'{result}',")