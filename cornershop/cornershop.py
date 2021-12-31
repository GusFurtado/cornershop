"""Cornershop class.

"""

from typing import Union

import pandas as pd
import requests

from .models import (
    Aisle,
    Country,
    Product,
    Search,
    Store
)



class Cornershop:
    """Object to access Cornershop's API.

    Parameters
    ----------
    locality : str | int
        ZIP Code.
    country : str
        Two-letter code for a country.
    
    """

    def __init__(
            self,
            locality: Union[str,int],
            country: str
        ):

        self.locality = locality
        self.country = country


    def __repr__(self) -> str:
        return f'<cornershop.Cornershop: {self.locality}>'


    def __str__(self) -> str:
        return self.locality


    def search_branches(self, query:str) -> pd.DataFrame:
        URL = f'https://cornershopapp.com/api/v2/branches/search?query={query}&locality={self.locality}&country={self.country}'
        json_file = requests.get(URL).json()['results']
        df = pd.DataFrame(json_file)
        df.store = df.store.map(Store)
        df.search_result = df.search_result.map(Search)
        return df


    def search_branch(self, branch_id:Union[str,int], query:str) -> pd.DataFrame:
        URL = f'https://cornershopapp.com/api/v2/branches/{branch_id}/search?query={query}'
        df = pd.read_json(URL)
        df.aisles = df.aisles.map(Aisle)
        return df


    def search_branch_groups(self) -> pd.DataFrame:
        URL = f'https://cornershopapp.com/api/v3/branch_groups?locality={self.locality}&country={self.country}'
        json_file = requests.get(URL).json()
        df = pd.DataFrame(json_file)
        return df


    def search_countries(self):
        URL = r'https://cornershopapp.com/api/v1/countries'
        df = pd.read_json(URL)
        df.countries = df.countries.map(Country)
        return df
    