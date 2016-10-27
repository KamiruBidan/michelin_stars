import json
import requests
import config

MICHELIN_REQUEST_URL = 'https://vmrest.viamichelin.com/apir/2/FindPOIByCriteria.json2/RESTAURANT/eng'
PAGE_SIZE = 100
query_params = {
    'filter': 'michelin_stars gt 0',
    'field': ';'.join(['name', 'address', 'michelin_stars']),
    'obfuscation': 'false',
    'authKey': config.API_KEY,
    'nb': PAGE_SIZE,
    'sidx': 0
}

def get_restaurants():
    ''' Get all Michelin-starred restaurants '''
    all_restaurants = []
    while True:
        resp = requests.get(MICHELIN_REQUEST_URL, params=query_params)
        data = json.loads(resp.text)

        if not data['poiList']:
            break

        for restaurant in data['poiList']:
            # Each restaurant can have multiple "data sheets" describing it
            # Some of them are missing Michelin star count
            for sheet in restaurant['datasheets']:
                if 'michelin_stars' in sheet:
                    all_restaurants.append(sheet)
                    break
        query_params['sidx'] = query_params['sidx'] + PAGE_SIZE

    return all_restaurants
