import requests
import pandas as pd

data = pd.read_csv('')
json = {'stories', 'fireplace', 'sqft', 'PrivatePool',
                 'Year built', 'Remodeled year', 'baths/bed',
                 'Parking', 'school_rating', 'density', 'status', 'propertyType']]}

if __name__=='__main__':
    r = requests.post('http://localhost:5000/add', json={'num': 5})

    print(r.status_code)

    if r.status_code == 200:
        print(r.json()['result'])
    else:
        print(r.text)