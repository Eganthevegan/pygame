pasta_ingredients = {"tomato","garlic","olive oil","chilli","pasta","garlic"}
pizza_ingredients = {"pepperoni","cheese","bread","olive oil","tomato"}
all_ingredients = pasta_ingredients.union(pizza_ingredients)
common = pasta_ingredients.intersection(pizza_ingredients)
print("All ingredients:", all_ingredients)
print("Common:", common)
print(pasta_ingredients)
print(len(pasta_ingredients))