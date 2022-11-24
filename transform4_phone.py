import pandas as pd

bsdf = pd.read_csv('c:/xampp/htdocs/python/bsTestETLDQLabLagi/dqthon-participants.csv')

bsdf['cleaned_phone_number'] = bsdf['phone_number'].str.replace(r'\+62|62', '0')

bsdf['cleaned_phone_number'] = bsdf['cleaned_phone_number'].str.replace(r'[()-]', '')

bsdf['cleaned_phone_number'] = bsdf['cleaned_phone_number'].str.replace(r'\s+', '')
bsdf.to_csv('c:/xampp/htdocs/python/bsTestETLDQLabLagi/dqthon-participants.csv', index=False)

print(bsdf.head(20))