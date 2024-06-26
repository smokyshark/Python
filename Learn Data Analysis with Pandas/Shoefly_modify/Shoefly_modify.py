import pandas as pd

orders = pd.read_csv('shoefly.csv')
shoe_source = lambda source: 'animal' if source == 'leather' else 'vegan'
orders['shoe_source'] = orders.shoe_material.apply(shoe_source)

salutation = lambda row: 'Dear Mr. {}'.format(row.last_name) if row.gender == 'male' else 'Dear Ms. {}'.format(row.last_name)
orders['salutation'] = orders.apply(salutation,axis = 1)
print(orders.head(5))
