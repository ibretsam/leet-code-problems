"""
2115. Find All Possible Recipes from Given Supplies
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. 
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, 
and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

Example 1:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

Constraints:
n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
"""

def findAllRecipes(recipes, ingredients, supplies):
    """
    Iterative with Progress Flag
    Time Complexitiy: O(R^2 * I) where R is the number of recipes and I is the number of ingredients
    Space Complexity: O(R + I)
    """
    available = set(supplies)
    result = []

    added = set()

    made_progress = True
    while made_progress:
        made_progress = False

        for i in range(len(recipes)):
            if recipes[i] in added:
                continue

            can_make = True
            for ingredient in ingredients[i]:
                if ingredient not in available:
                    can_make = False
                    break
            
            if can_make:
                result.append(recipes[i])
                available.add(recipes[i])
                added.add(recipes[i])
                made_progress = True
    return result


from collections import deque
def findAllRecipes(recipes, ingredients, supplies):
    """
    Topological Sort with BFS
    Time Complexity: O(R * I) where R is the number of recipes and I is the number of ingredients
    Space Complexity: O(S + R * I) where S is the number of supplies and R * I is the space for the graph
    """
    supplies_set = set(supplies)
    recipe_set = set(recipes)    

    graph = {recipe: [] for recipe in recipes}
    missing_count = {recipe: 0 for recipe in recipes}

    for i, recipe in enumerate(recipes):
        for ingredient in ingredients[i]:
            if ingredient not in supplies_set:
                missing_count[recipe] += 1
                if ingredient in recipe_set:
                    graph[ingredient].append(recipe)

    q = deque([recipe for recipe in recipes if missing_count[recipe] == 0])
    res = []

    while q:
        recipe = q.popleft()
        res.append(recipe)

        for dependent in graph[recipe]:
            missing_count[dependent] -= 1
            if missing_count[dependent] == 0:
                q.append(dependent)

    return res

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(findAllRecipes(recipes, ingredients, supplies))