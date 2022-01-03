# The Unofficial Python wrapper for Cornershop by Uber's API

Cornershop is a grocery delivery service owned by Uber.

This API allows the user to search for all available stores near a given zip code.

Please, check their official website at: https://cornershopapp.com/

## Instalation

- Soon

## Dependencies

- Python 3.6 or higher
- requests

## License

- [MIT](LICENSE)

Even though this is just a wrapper, use it with caution, since the data fetched is Uber's property.

## Getting Started

First, import and instanciate the Cornershop API model using your zip code as locality.

```python
>>> from cornershop import Cornershop

>>> cs = Cornershop(
...     locality = '00000000',
...     country = 'BR'
... )
```

Then, call the following methods to fetch data from branches near your locality.

```python
>>> cs.search_branches(query='...')
>>> cs.search_branch(branch_id='00000', query='...')
>>> cs.search_branch_group()
>>> cs.search_countries()
```

Set the `json_format` argument as `True` to return a json-style dictionaty instead of a `cornershop` model.

```python
>>> cs = Cornershop(
...     locality = '00000000',
...     country = 'BR',
...     json_format = True
... )
```

Check the [examples notebook](examples.ipynb) for more details.
