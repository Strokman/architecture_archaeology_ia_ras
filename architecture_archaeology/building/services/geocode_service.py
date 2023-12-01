import googlemaps

from architecture_archaeology.settings import GMAPS_API_KEY


def geocode(name):
    gmaps = googlemaps.Client(key=GMAPS_API_KEY)
    location = gmaps.geocode(name)
    long = location[0]['geometry']['location']['lng']
    lat = location[0]['geometry']['location']['lat']
