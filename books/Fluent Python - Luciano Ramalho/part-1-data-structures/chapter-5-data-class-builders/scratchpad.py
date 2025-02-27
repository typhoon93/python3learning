# class Coordinate:
#     def __init__(self, lat, lon):
#         self.lat = lat
#         self.lon = lon
#
#
# moscow = Coordinate(55.4, 12.0)
# location_2 = Coordinate(55.4, 12.0)
# print(moscow)
# print(moscow==location_2)

#### useful eq and repr provided with namedtuple

# from collections import namedtuple
#
# Coordinate = namedtuple('Coordinate', 'lat lon')
# moscow = Coordinate(55.756, 37.617)
# print(issubclass(Coordinate, tuple))
# print(moscow == Coordinate(55.756, 37.617))

#
# #### typehints available with typing.NamedTuple)
#
#
# import typing
#
# # Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
# Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)
# print(typing.get_type_hints(Coordinate))
#
# #### can be used with inheritance, with a custom __str__
#
# from typing import NamedTuple
# class Coordinate(NamedTuple):
#     lat: float
#     lon: float
#     def __str__(self):
#         ns = 'N' if self.lat >= 0 else 'S'
#         we = 'E' if self.lon >= 0 else 'W'
#         return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
#
# ### dataclass, similar code to above, but we use a decorator, so no messing with inheritance here
#
# from dataclasses import dataclass
# @dataclass(frozen=True)
# class Coordinate:
#     lat: float
#     lon: float
#     def __str__(self):
#         ns = 'N' if self.lat >= 0 else 'S'
#         we = 'E' if self.lon >= 0 else 'W'
#         return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
#

### collcections.namedtuple - factory builds subclasses of tuple enhanced with field names, a class name, and an informative __repr__.
import code
from collections import namedtuple

City = namedtuple(
    'City', 'name country population coordinates'
)   # split a " "
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
code.interact(local=locals())
print(tokyo)
print(tokyo.population)
