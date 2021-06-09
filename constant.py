from datetime import date
DATE_TODAY = date.today().strftime("%Y_%m_%d")

WATCH_LIST_STOCK = [
    "ADBL",
    "AHPC",
    "AIL",
    "AKJCL",
    "AKPL",
    "API",
    "BARUN",
    "BFC",
    "BOKL",
    "BPCL"
]

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
