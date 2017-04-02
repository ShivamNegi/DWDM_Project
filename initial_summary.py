import pandas as pd

df = pd.read_csv('en.openfoodfacts.org.products.tsv', sep='\t', header=None)

print "The attributes are: "
for attribute in df.iloc[0]:
    print attribute
