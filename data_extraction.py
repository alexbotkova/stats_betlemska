import pdfplumber
import pandas as pd
import re
from datetime import datetime

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def parse_text_to_df(text):
    rows = text.split("\n")
    data = []
    
    i = 0
    while i < len(rows):
        row = rows[i]
        if re.match(r'^\d{11}', row):
            pattern = r'\d{1,2}\.\s\d{1,2}\.\s2024\s[\d\s]+,\d{2}\sKč\s[\d\s]+,\d{2}\sKč'
            match = re.search(pattern, row)
            if match:
                result = match.group()
                arr = result.split("2024")
                date, profit_tips_str = arr
                date += "2024 " 

                profit_tips_arr = profit_tips_str.split("Kč")[:2]
                profit_tips_arr[0] = profit_tips_arr[0].split(" ")[2]
                for j in range(len(profit_tips_arr)):
                    profit_tips_arr[j] = float(profit_tips_arr[j].replace(",", "."))
                
                i += 1
                next_row = rows[i]
                if re.match(r'^\d{2}:\d{2}:\d{2}$', next_row):
                    date += next_row
                    date= datetime.strptime(date, '%d. %m. %Y %H:%M:%S')
                    data.append({'Date': date, 'Profit': profit_tips_arr[0], 'Tips': profit_tips_arr[1]})
        i += 1
    df = pd.DataFrame(data)
    df['Hour'] = df['Date'].dt.hour

    return df

def categorize_time_of_day(hour):
    if 12 <= hour < 18:
        return 'Day'
    else:
        return 'Night'
    

pdf_path = 'vydelky.pdf'
text = extract_text_from_pdf(pdf_path)

df = parse_text_to_df(text)

df = df[df['Profit'] != 0]
df = df.drop(df.index[0])

df['TimeOfDay'] = df['Hour'].apply(categorize_time_of_day)

print(df.tail())

df.to_pickle("betlemska.pkl")

    
