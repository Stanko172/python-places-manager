from country_places import CountryPlaces

#GeoDB API KEY
headers = {
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
    'x-rapidapi-key': "8d618c27f8mshd21f05a0a253e04p1dd2e8jsna09b6c2d6ed2"
    }
country_code = "LI"
#First we need to fetch all regions for a country
country_places = CountryPlaces()
country_places.set_headers(headers)
country_places.setup_database_client("localhost", 27017)

regions = country_places.get_regions_by_country(country_code)
cities = country_places.get_cities_by_country(regions, country_code)

country_places.save_to_db(cities, "open_hours2", "country_cities")