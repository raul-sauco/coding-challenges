# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict, deque
import timeit
from typing import List

# Visualize the problem as a directed graph. Store the number of each recipe's
# dependencies as the outdegree and process the available ingredients.
# For each ingredient, remove the dependency form its dependents.
#
# Runtime: 1547 ms, faster than 36.02% of Python3 online submissions for
# Find All Possible Recipes from Given Supplies.
# Memory Usage: 17.1 MB, less than 70.55 % of Python3 online submissions for
# Find All Possible Recipes from Given Supplies.


class TopologicalSort:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        outdegree = defaultdict(int)
        dependencies_graph = defaultdict(list)
        # Use zip to iterate through recipes with their ingredients
        for recipe, ing in zip(recipes, ingredients):
            # The distance is the number of ingredients we need to compute the recipe
            # If we see it as a graph, it is the number of outgoing edges from this vertex
            # and it represents the recipe's dependencies. They can be supplies or recipes.
            outdegree[recipe] = len(ing)
            # Dictionary with the recipes that depend on each ingredient keyed by ingredient
            # { 'ingredient': ['dependent1', 'dependent2'...]}
            for ingredient in ing:
                dependencies_graph[ingredient].append(recipe)

        result = []
        # deque allows push/pop from both ends in O(1)
        # queue stores supplies, later will push recipes that can be computed
        queue = deque(supplies)
        # Converting to a set allows to check for recipe existence in O(1)
        recipes = set(recipes)
        while queue:
            # Obtain the oldest element that is available
            elem = queue.popleft()
            # If it is a recipe, add it to the result set (it can be computed)
            if elem in recipes:
                result.append(elem)
            # Iterate over this supply / recipe dependencies
            for dependent in dependencies_graph[elem]:
                # Since this ingredient is available, remove it from the outdegree count
                outdegree[dependent] -= 1
                # Once the outdegree reaches 0, we can compute this recipe
                if outdegree[dependent] == 0:
                    # Add the computable recipe to the queue
                    # Recipes that depend on it will be able to use it later
                    queue.append(dependent)
        return result


# Following the recursive failure because of cyclic dependencies between the recipes:
# We can iterate over the recipes and keep a flag to check if we have added any
# recipe to the result set in the latest iteration. If we add some recipes, the
# next iteration may use them. If we fail to add any recipes, we will not be able
# to add any more, and we can exit.
# This solution, as expected, runs very slow with bigger inputs.
#
# Runtime: 2317 ms, faster than 9.82% of Python3 online submissions for Find All Possible
# Recipes from Given Supplies.
# Memory Usage: 16.9 MB, less than 96.65 % of Python3 online submissions for Find All
# Possible Recipes from Given Supplies.


class Iterative:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Check in O(1) if something is currently available
        available = set(supplies)
        result = []
        # Flag whether we added any recipes to the result set in the current iteration
        added = True
        # Only keep iterating if we added any recipes in the previous iteration
        while added:
            added = False
            # Iterate over the recipes together with their ingredients
            for recipe, igr in zip(recipes, ingredients):
                if recipe in available:
                    continue
                # Iterate over the ingredients, if one of the ingredients is missing
                # break out of both loops, ingredients and current recipe
                for ingredient in igr:
                    if ingredient not in available:
                        break
                # If the ingredients loop completed without breaking, add the recipe to the result set
                # and check the next recipe (continue)
                else:
                    available.add(recipe)
                    result.append(recipe)
                    added = True
                    continue
                # If the nested ingredient loop completed with break, move to the next recipe
        return result


# Runtime error too much recursion
class Recursive:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = {supply: True for supply in supplies}

        def canCook(idx: int):
            recipe_name = recipes[idx]
            # If we have already computed this recipe, return the computed value
            if recipe_name in available:
                return available[recipe_name]

            # Iterate over all the ingredients needed to elaborate the recipe
            for ingredient in ingredients[idx]:
                if ingredient not in available:
                    if ingredient not in recipes:
                        available[recipes[idx]] = False
                        return False
                    # Ingredient is in recipes but has not been computed yet
                    # This elif can be merged with the if above but it would be less readable
                    elif not canCook(recipes.index(ingredient)):
                        available[recipes[idx]] = False
                        return False
                # Ingredient is in available
                elif not available[ingredient]:
                    available[recipes[idx]] = False
                    return False

            # All the ingredients are available or can be computed
            available[recipes[idx]] = True
            return True

        # Iterate over the recipes and check if we can cook them
        for idx in range(len(recipes)):
            canCook(idx)

        return [recipe for recipe in recipes if available[recipe]]


def test():
    executor = [
        {'executor': TopologicalSort, 'title': 'TopologicalSort', },
        {'executor': Iterative, 'title': 'Iterative', },
    ]
    tests = [
        [
            ["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
            [
                ["d"],
                ["hveml", "f", "cpivl"],
                ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
                ["cpivl", "hveml", "zpmcz", "ju", "h"],
                ["h", "fzjnm", "e", "q", "x"],
                ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"],
                ["f", "hveml", "cpivl"],
            ],
            ["f", "hveml", "cpivl", "d"],
            ["ju", "fzjnm", "q"],
        ],
        [
            ["bread"], [["yeast", "flour"]],
            ["yeast", "flour", "corn"], ["bread"],
        ],
        [
            ["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"], ["bread", "sandwich"],
        ],
        [
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
            ["yeast", "flour", "meat"], ["bread", "sandwich", "burger"],
        ],
        [
            ["burger", "sandwich", "bread"],
            [["sandwich", "meat", "bread"], ["bread", "meat"], ["yeast", "flour"]],
            ["yeast", "flour", "meat"], ["burger", "sandwich", "bread"],
        ],
        [
            ["burger", "sandwich", "bread", "quesadilla"],
            [
                ["sandwich", "meat", "bread"],
                ["bread", "meat"],
                ["yeast", "flour"],
                ["meat", "flour", "yeast", "cheese"],
            ],
            ["yeast", "flour", "meat"], ["burger", "sandwich", "bread"],
        ],
        [
            ["burger", "sandwich", "bread", "quesadilla"],
            [
                ["sandwich", "meat", "bread"],
                ["bread", "meat"],
                ["yeast", "flour"],
                ["meat", "flour", "yeast", "cheese"],
            ],
            ["yeast", "cheese", "flour", "meat"],
            ["burger", "sandwich", "bread", "quesadilla"],
        ],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = set(sol.findAllRecipes(t[0], t[1], t[2]))
                expected = set(t[3])
                assert result == expected, f'{result} != {expected} for {t[0]}:{t[1]}:{t[2]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
