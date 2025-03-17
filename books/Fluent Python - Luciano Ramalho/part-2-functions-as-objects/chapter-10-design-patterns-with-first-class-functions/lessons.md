
# 'Hackish' way of finding all promos
prerequisites: -> enforce that promos end in "_promo"
```python

from decimal import Decimal
from strategy import Order
from strategy import (
fidelity_promo, bulk_item_promo, large_order_promo
)

promos = [promo for name, promo in globals().items()
if name.endswith('_promo') and
name != 'best_promo'
]

```


# Using introspection to get promos
- prerequisits: keep all promos in the same module

```python
from decimal import Decimal
import inspect
from strategy import Order
import promotions
promos = [func for _, func in inspect.getmembers(promotions, inspect.isfunction)]
```

# Using decorators

@promotion decorator simply adds all decorated itesm into a promos list.
very elegant solution, I love it!! 
Definitely use in the future
```python

Promotion = Callable[[Order], Decimal]
promos: list[Promotion] = []

def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)

@promotion
def fidelity(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)

```