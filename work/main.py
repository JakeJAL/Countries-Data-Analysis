import fetch
import draw


data = fetch.fetch_countries_data()
draw.draw_languages(data)
draw.draw_un_members(data)
data.to_csv('data', index=False)