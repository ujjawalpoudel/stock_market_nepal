import re, requests, os
import pandas as pd
from bs4 import BeautifulSoup
from constant import (
    COLUMN,
    FLOAT_COLUMN,
    PERCENTAGE_COLUMN,
    QUATER_REPORT_COLUMN,
    WATCH_LIST_STOCK,
    DATE_TODAY,
    RENAME_COL,
    ARRANGE_COL,
)

from path import parent_folder_path

stock_data = []
for stock_name in WATCH_LIST_STOCK:
    url = f"http://merolagani.com/CompanyDetail.aspx?symbol={stock_name}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    data = {}
    table_element = soup.find(
        "table",
        attrs={
            "class": "table table-striped table-hover table-zeromargin",
            "id": "accordion",
        },
    )
    table_bodies = table_element.find_all("tbody")

    for table_body in table_bodies:
        rows = table_body.find_all("tr")
        for row in rows:
            try:
                header = row.find("th")
                if header.string is not None:
                    header_string = header.string
                    cols = row.find("td").text
                else:
                    header_string = header.find("a").string
                    cols = row.find("td").text
                cols = "" if cols is None else cols
                if header_string is not None:
                    header_col = header_string.strip()
                    if header_col in COLUMN:
                        data["Stock URL"] = url
                        data["Stock"] = stock_name
                        trimmed_cols = re.sub("\n|\r", " ", cols.strip())
                        value = re.sub(" +", " ", trimmed_cols)
                        if header_col == "52 Weeks Low - High":
                            high_low_val = value.split("-")
                            data["High"] = float(high_low_val[0].replace(",", ""))
                            data["Low"] = float(high_low_val[1].replace(",", ""))
                        elif header_col in PERCENTAGE_COLUMN:
                            data[header_col] = float(
                                value.split("%")[0].strip().replace(",", "")
                            )
                        elif header_col in FLOAT_COLUMN:
                            if value != "":
                                data[header_col] = float(value.replace(",", ""))
                            else:
                                data[header_col] = 0
                        elif header_col in QUATER_REPORT_COLUMN:
                            if value != "":
                                data[header_col] = float(
                                    value.split("(")[0].replace(",", "")
                                )
                            else:
                                data[header_col] = 0
                        elif header_col == "Right Share":
                            data[header_col] = value.split("(")[0].strip()
                        else:
                            data[header_col] = value
            except AttributeError as e:
                pass
    url = f"https://www.sharesansar.com/company/{stock_name}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    table_element = soup.find(
        "table",
        attrs={
            "class": "table table-bordered table-striped table-hover text-center company-table"
        },
    )
    table_bodies = table_element.find_all("tbody")

    for table_body in table_bodies:
        rows = table_body.find_all("tr")
        for row in rows:
            try:
                header = row.find_all("td")
                sharesansar_data = {"name": header[0].text, "value": header[1].text}
                if sharesansar_data["name"] == "Bonus Share":
                    data["% Bonus"] = float(sharesansar_data["value"].split("\n")[0])
                if sharesansar_data["name"] == "Cash Dividend":
                    data["% Dividend"] = float(sharesansar_data["value"].split("\n")[0])
            except Exception as e:
                pass

    stock_data.append(data)

stock_df = pd.DataFrame(stock_data)

filename = f"stock_market_data_{DATE_TODAY}.xlsx"

filename = os.path.join(parent_folder_path, filename)
writer = pd.ExcelWriter(filename, engine="xlsxwriter")

for group_name, dataframe_data in stock_df.groupby("Sector"):
    # exclude columns you don't want
    dataframe = dataframe_data[
        dataframe_data.columns[~dataframe_data.columns.isin(["Sector", "Stock URL"])]
    ]
    dataframe = dataframe.rename(columns=RENAME_COL)
    sum_column = dataframe["Dividend"] + dataframe["Bonus"]
    dataframe["Total"] = sum_column

    dataframe = dataframe[dataframe.columns[~dataframe.columns.isin(["Right Share"])]]

    dataframe = dataframe.reindex(columns=ARRANGE_COL)

    dataframe.to_excel(writer, sheet_name=group_name, index=False)
    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets[group_name]
    (max_row, max_col) = dataframe.shape
    # Adding an autofilter
    worksheet.autofilter(0, 0, max_row, max_col - 1)
    worksheet.freeze_panes(1, 1)

    col_idx = dataframe.columns.get_loc("Stock")
    writer.sheets[group_name].set_column(col_idx, col_idx, 9.57)
    col_idx = dataframe.columns.get_loc("MP")
    writer.sheets[group_name].set_column(col_idx, col_idx, 7.86)
    col_idx = dataframe.columns.get_loc("Change(%)")
    writer.sheets[group_name].set_column(col_idx, col_idx, 14.43)
    col_idx = dataframe.columns.get_loc("High")
    writer.sheets[group_name].set_column(col_idx, col_idx, 8.86)
    col_idx = dataframe.columns.get_loc("Low")
    writer.sheets[group_name].set_column(col_idx, col_idx, 8.43)
    col_idx = dataframe.columns.get_loc("120(AVG)")
    writer.sheets[group_name].set_column(col_idx, col_idx, 13.29)
    col_idx = dataframe.columns.get_loc("180(AVG)")
    writer.sheets[group_name].set_column(col_idx, col_idx, 13.29)
    col_idx = dataframe.columns.get_loc("1 Year(%)")
    writer.sheets[group_name].set_column(col_idx, col_idx, 13.29)
    col_idx = dataframe.columns.get_loc("EPS")
    writer.sheets[group_name].set_column(col_idx, col_idx, 8)
    col_idx = dataframe.columns.get_loc("P/E Ratio")
    writer.sheets[group_name].set_column(col_idx, col_idx, 12.86)
    col_idx = dataframe.columns.get_loc("Book Value")
    writer.sheets[group_name].set_column(col_idx, col_idx, 14.86)
    col_idx = dataframe.columns.get_loc("PBV")
    writer.sheets[group_name].set_column(col_idx, col_idx, 8.43)
    col_idx = dataframe.columns.get_loc("Dividend")
    writer.sheets[group_name].set_column(col_idx, col_idx, 12.86)
    col_idx = dataframe.columns.get_loc("Bonus")
    writer.sheets[group_name].set_column(col_idx, col_idx, 10.29)
    col_idx = dataframe.columns.get_loc("Total")
    writer.sheets[group_name].set_column(col_idx, col_idx, 9.29)
    # col_idx = dataframe.columns.get_loc('Right Share')
    # writer.sheets[group_name].set_column(col_idx, col_idx, 14.86)

    count = 2
    for index, row in dataframe_data.iterrows():
        # Write a URL(hyperlink)
        row_number = f"A{count}"
        worksheet.write_url(row_number, row["Stock URL"], string=row["Stock"])
        count += 1
writer.save()
