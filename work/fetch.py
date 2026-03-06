import requests
import pandas as pd
import json

def fetch_countries_data():
    response = requests.get('https://restcountries.com/v3.1/all?fields=name,unMember,languages').text
    data = json.loads(response)
    data = pd.concat((pd.json_normalize(d) for d in data))
    data = data[['unMember','name.common']]
    data = data.reset_index(drop=True)
    data

    response = requests.get('https://restcountries.com/v3.1/all?fields=languages').text
    lang = json.loads(response)
    lang = pd.concat((pd.json_normalize(d['languages']) for d in lang), axis=0)
    cols = []
    for i in lang.columns:
        cols.append(i)
    for i in cols:
        lang['cat'].fillna(lang[i],inplace=True)
    lang = lang[['cat']]
    lang = lang.reset_index(drop=True)
    lang.rename(columns={'cat': 'languages'}, inplace=True)
    data = pd.merge(data, lang, left_index=True, right_index=True)
    return data