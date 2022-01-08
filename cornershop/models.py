"""Cornershop Models.

"""

class Aisle:
    """Model for an aisle.
    
    """

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])
        self.products = [Product(p) for p in self.products]

    def __repr__(self) -> str:
        return f'<cornershop.models.Aisle: {self.aisle_id} - {self.aisle_name}>'

    def __str__(self) -> str:
        return self.aisle_id



class Branch:
    """Model for a branch.
    
    """

    def __init__(self, data:dict):
        self.ad_campaign = data['ad_campaign']
        self.aisles = [Aisle(a) for a in data['aisles']]

    def __str__(self) -> str:
        return 'Branch'

    def __repr__(self) -> str:
        return f'<cornershop.models.Branch>'



class Country:
    """Model for a country.
    
    """

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self) -> str:
        return f'<cornershop.models.Country: {self.name}>'

    def __str__(self) -> str:
        return self.name



class Group:
    """Model for a group.
    
    """

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])
        self.items = [GroupItem(item) for item in data['items']]

    def __repr__(self) -> str:
        return f'<cornershop.model.Group: {self.name}>'

    def __str__(self) -> str:
        return self.name



class GroupItem:
    """Model for a group item.
    
    """

    def __init__(self, data:dict):
        self.type = data['type']
        self.badges = data['badges']
        for key in data['content']:
            setattr(self, key, data['content'][key])

    def __repr__(self) -> str:
        return f'<cornershop.model.GroupItem: {self.name}>'

    def __str__(self) -> str:
        return self.name



class Product:
    """Model for a product.
    
    """

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self) -> str:
        return f'<cornershop.models.Product: {self.id} - {self.name}>'

    def __str__(self) -> str:
        return self.name



class Result:
    """Model for branch search results.
    
    """

    def __init__(self, data:dict):
        self.store = Store(data['store'])
        self.search_result = SearchResult(data['search_result'])

    def __str__(self) -> str:
        return self.store.name

    def __repr__(self) -> str:
        return f'<cornershop.models.Result: "{self.search_result.search_term}" on {self.store.name}>'



class SearchResult:
    """Model for the search result query.
    
    """

    def __init__(self, data:dict):
        self.search_term = data['search_term']
        self.aisles = [Aisle(aisle_data) for aisle_data in data['aisles']]

    def __repr__(self) -> str:
        return f'<cornershop.models.SearchResult: {self.search_term}>'



class Store:
    """Model for a store.
    
    """
    
    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<cornershop.models.Store: {self.name}>'
