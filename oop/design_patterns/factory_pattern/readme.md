# Factory Pattern

encapsulate all code that instantiates concrete classes into one place/ another class/object

# Principle of Dependency Inversion

## def:

Products = Classes that are supplied by the Factory Class
Consumers = Classes that require/use the Products

## Dependency Inversion

- the Consumers aren't dependend of concrete Products. Instead they only know the "Base" Product, that all Products inherit from
- All the dependencies are kept inside the Factory instead

## Furthermore

- In case of multiple Factories & Ingredients/Parts:
- the Factory itself can be dependend of another Factory e.g. the Product can be made out of several Ingredients/Parts that each have their own Implementations. The Factory can then be reliant of another Factory for the Ingredients & Parts.
