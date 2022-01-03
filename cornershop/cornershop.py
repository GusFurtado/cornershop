"""Cornershop class.

"""

from typing import List, Union

import requests

from .models import (
    Branch,
    Country,
    Result
)



class Cornershop:
    """Object to access Cornershop's API.

    Parameters
    ----------
    locality : str | int
        ZIP Code.
    country : str
        Two-letter code for a country.
    json_format : bool, default=False
        If True, all methods will return a json-style dictionary.
    
    Methods
    -------
    search_branch(branch_id:str, query:str) -> cornershop.models.Branch
    search_branch_group() -> dict
    search_branches(query:str) -> list of cornershop.models.Results
    search_country() -> list of cornershop.models.Countries

    """

    def __init__(
            self,
            locality: Union[str,int],
            country: str,
            json_format = False
        ):

        self.locality = locality
        self.country = country
        self.json_format = json_format


    def __repr__(self) -> str:
        return f'<cornershop.Cornershop: {self.locality}/{self.country}>'


    def __str__(self) -> str:
        return self.locality


    def search_branches(
            self,
            query: str
        ) -> Union[dict, List[Result]]:
        """Search for all branches near the locality.

        Parameters
        ----------
        query : str
            Search query.

        Returns
        -------
        list of cornershop.models.Result
            List of models if attribute `json_format` is False.
        dict
            A json-style dictionary if `json_format` is True.
        
        """

        URL = f'https://cornershopapp.com/api/v2/branches/search?query={query}&locality={self.locality}&country={self.country}'
        json_file = requests.get(URL).json()
        if self.json_format:
            return json_file
        return [Result(r) for r in json_file['results']]


    def search_branch(
            self,
            branch_id: Union[str, int],
            query: str
        ) -> Union[dict, Branch]:
        """Search for all branches near the locality.

        Parameters
        ----------
        branch_id : str | int
            ID of the desired branch.
        query : str
            Search query.

        Returns
        -------
        cornershop.models.Branch
            Branch model if attribute `json_format` is False.
        dict
            A json-style dictionary if `json_format` is True.
        
        """

        URL = f'https://cornershopapp.com/api/v2/branches/{branch_id}/search?query={query}'
        json_file = requests.get(URL).json()
        if self.json_format:
            return json_file
        return Branch(json_file)


    def search_branch_groups(self):
        URL = f'https://cornershopapp.com/api/v3/branch_groups?locality={self.locality}&country={self.country}'
        json_file = requests.get(URL).json()
        return json_file


    def search_countries(self) -> Union[dict, List[Country]]:
        """Search for a list of available countries.
        
        Returns
        -------
        list of cornershop.models.Country
            List of models if attribute `json_format` is False.
        dict
            A json-style dictionary if `json_format` is True.

        """

        URL = r'https://cornershopapp.com/api/v1/countries'
        json_file = requests.get(URL).json()
        if self.json_format:
            return json_file
        return [Country(c) for c in json_file['countries']]
    