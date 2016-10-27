from collections import Counter
from pprint import pprint
from get_restaurants import get_restaurants

restaurants = get_restaurants()

print("Count restaurants by star rating")
restaurants_by_rating = Counter([r['michelin_stars'] for r in restaurants])
pprint(dict(restaurants_by_rating))

print("Count restaurants by country")
restaurants_by_country = Counter([r['country'] for r in restaurants])
pprint(dict(restaurants_by_country))

for stars in range(1, 4):
    print("Count {}-star restaurants by country".format(stars))
    star_restaurants_by_country = Counter([
        r['country'] for r in restaurants
        if r['michelin_stars'] == str(stars)
    ])
    pprint(dict(star_restaurants_by_country))
