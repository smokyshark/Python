import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

most_views_rows = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(most_views_rows)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()


clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
)
print(clicks_pivot)
clicks_pivot['percent_clicked'] = round(clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100, 2)
print(clicks_pivot)

count_group = ad_clicks.groupby('experimental_group').user_id.count()
print(count_group)

greater_a_or_b = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
).reset_index()
print(greater_a_or_b)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

#Version A clicks pivot table
a_clicks_pivot = a_clicks\
.groupby(['is_click', 'day'])\
.user_id\
.count()\
.reset_index()\
.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
)\
.reset_index()

a_clicks_pivot['percent_clicked'] = round(a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False]) * 100, 2)

print(a_clicks_pivot)


#Version B clicks pivot table
b_clicks_pivot = b_clicks\
.groupby(['is_click', 'day'])\
.user_id\
.count()\
.reset_index()\
.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
)\
.reset_index()

b_clicks_pivot['percent_clicked'] = round(b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False]) * 100, 2)

print(b_clicks_pivot)