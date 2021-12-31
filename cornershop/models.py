class Country:

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self) -> str:
        return f'<cornershop.Country: {self.name}>'

    def __str__(self) -> str:
        return self.name



class Store:
    
    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<cornershop.Store: {self.name}>'



class Product:

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self) -> str:
        return f'<cornershop.Product: {self.id} - {self.name}>'

    def __str__(self) -> str:
        return self.name



class Aisle:

    def __init__(self, data:dict):
        for key in data:
            setattr(self, key, data[key])
        self.products = [Product(p) for p in self.products]

    def __repr__(self) -> str:
        return f'<cornershop.Aisle: {self.aisle_id} - {self.aisle_name}>'

    def __str__(self) -> str:
        return self.aisle_id



class Search:

    def __init__(self, data:dict):
        self.search_term = data['search_term']
        self.aisles = [Aisle(aisle_data) for aisle_data in data['aisles']]

    def __repr__(self) -> str:
        return f'<cornershop.Search: {self.search_term}>'
