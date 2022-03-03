import requests
from pymongo import MongoClient
import time

class CountryPlaces:
    def __init__(self):
        self.__headers = None
        self.__db = None

    def set_headers(self, headers):
        self.__headers = headers

    def setup_database_client(self, hostname, port):
        self.__db = MongoClient(hostname, port)

    def get_database(self, name):
        return self.__db[name]

    def execute_request(self, url):
        response = requests.request("GET", url, headers=self.__headers)
        time.sleep(3)
        return response.json()

    def save_to_db(self, data, dbname, collection):
        db = self.get_database(dbname)
        db[collection].insert_many(data)

    def get_regions_by_country(self, country_code):
        regions_url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/countries/{country_code}/regions"
        country_regions = self.execute_request(regions_url)["data"]
        return country_regions

    def get_cities_by_country(self, country_regions, country_code):
        data = []
        for region in country_regions:
            url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/countries/{country_code}/regions/{region['wikiDataId']}/cities"
            data += [city for city in self.execute_request(url)["data"]]
        return data




