#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  #If we do not have all the ingredients, FAIL
  if recipe.keys() != ingredients.keys():
    return 0
  # For each key in recipe, divide that from the number of ingredients with the same key
  for i in recipe:
    batches.append(ingredients[i]//recipe[i])

  return min(batches) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))