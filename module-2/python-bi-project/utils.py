import pandas as pd
import math
from pymongo import MongoClient


import matplotlib.pyplot as plt
import seaborn as sns


def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
    * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return abs(d)



def top_cities(df):
    cities = [str(c['city'])+", "+str(c['country_code']) for i,e in df.iterrows() for c in e.offices if c['city'] != '' and c['country_code'] != '']
    s = pd.Series(cities).value_counts()
    return {k:v for k,v in s.to_dict().items() if v >= 10}



def get_dist_param(df):
    distances_metric = []

    for i,r in df.iterrows():
        for e in r['offices']:
            for k,v in major_cities.items():
                if e['latitude'] and e['longitude'] and e['city']:
                    if distance(v, (e['latitude'], e['longitude']) ) <= 1000:
                        d_n = 1 - distance( v, (e['latitude'], e['longitude']))/1000
                        distances_metric.append({k: d_n})
                        
                        
    dist_scores = []
    for k in major_cities.keys():
        if len([d.get(k) for d in distances_metric if k in d.keys()]) >= 100:
            dist_scores.append({k:sum([d.get(k) for d in distances_metric if k in d.keys()])/len([d.get(k) for d in distances_metric if k in d.keys()])})
        else:
            dist_scores.append({k:0.1})
    
    return {k:v for e in dist_scores for k,v in e.items()}



def metric_score(df):
    n = df['local_comp']
    c = df['dist_param']
    cost = df['cost_param']
    
    score = 10000*math.log(n, 100)*math.log10(n)*(c**6)/(cost**0.2*math.log10(cost)**6)
    
    return score



major_cities = {'New York': (40.7128, -74.0060), 'San Francisco': (37.7749, -122.4194), 'London': (51.5074, 0.1278), 
                'Chicago': (41.8781, -87.6298), 'San Jose': (37.3382, -121.8863), 'Tokyo': (35.6762, 139.6503),
               'Paris': (48.8566, 2.3522), 'Seattle': (47.6062, -122.3321), 'Beijing': (39.9042, 116.4074), 
                'Austin': (30.2672, -97.7431), 'Los Angeles': (34.0522, -118.2437), 'San Mateo': (37.5630, -122.3255),
               'Singapore': (1.3667, 103.8198), 'Shanghai': (31.2222195, 121.4580612), 'Mountain View': (37.3861, -122.0839), 
                'Cambridge': (42.3736, -71.1097), 'Palo Alto': (37.4419, -122.1430), 'San Diego': (32.7157, -117.1611), 
                'Santa Clara': (37.3541, -121.9552), 'Sunnyvale': (37.3688, -122.0363), 'Bangalore': (12.9716, 77.5946), 
                'Madrid': (40.4168, 3.7038), 'Berlin': (52.5200, 13.4050), 'Chennai': (13.0827, 80.2707), 
                'Boston': (42.3601, -71.0589), 'Toronto': (43.6532, -79.3832), 'Fremont': (37.5485, -121.9886), 
                'Santa Monica': (34.0195, -118.4912), 'Mumbai': (19.0760, 72.8777), 'Irvine': (33.6846, -117.8265), 
                'Amsterdam': (52.3667, 4.8945), 'Atlanta': (33.7490, -84.3880), 'Scottsdale': (33.4942, -111.9261), 
                'Reston': (38.9586, -77.3570)}



cost_cities = {'New York': 187.2, 'San Francisco': 269.3, 'London': 187.2*0.75, 'Chicago': 106.9, 
               'San Jose': 214.5, 'Tokyo': 187.2*2/3, 'Paris': 187.2*5/6, 'Seattle': 172.3, 
               'Beijing': 187.2/2, 'Austin': 119.3, 'Los Angeles': 173.3, 'San Mateo': 270.6,
               'Singapore': 187.2*3/2, 'Shanghai': 187.2*0.634, 'Mountain View': 315.4, 'Cambridge': 181.8, 
               'Palo Alto': 471.0, 'San Diego': 160.1, 'Santa Clara': 250.0, 'Sunnyvale': 300.1, 
               'Bangalore': 187.2/10, 'Madrid': 187.2/2, 'Berlin': 187.2/2, 'Chennai': 187.2/15, 
               'Boston': 162.4, 'Toronto': 187.2*0.89, 'Fremont': 227.3, 'Santa Monica': 304.5, 
               'Mumbai': 187.2/4, 'Irvine': 187.1, 'Amsterdam': 187.2*0.54, 'Atlanta': 107.5, 
               'Scottsdale': 133.2, 'Reston': 138.9}
