from recipelinks import RecipeLinks
from recipepage import RecipePage

class Scraper:
    def __init__(self, recipe_path, review_path, log_path):
        self.recipe_path = recipe_path
        self.review_path = review_path
        self.log_path = log_path

    def writeIteration(self, recipes, review_blocks, page_num):
        recipe_file = open(self.recipe_path, 'a')
        for recipe in recipes:
            recipe_file.write(recipe.toJSON() + "\n")
        recipe_file.close()

        review_file = open(self.review_path, 'a')
        for block in review_blocks:
            for review in block:
                review_file.write(review.toJSON() + "\n")
        review_file.close()

        log_file = open(self.log_path, 'a')
        log_file.write(str(page_num) + "\n")
        log_file.close()

    def parseRecipeLinks(self, recipe_links):
        recipes = []
        reviews = []
        for link in recipe_links:
            print link
            page = RecipePage(link)
            recipe = page.getRecipe()
            recipes.append(recipe)
            reviews_array = page.getReviews()
            reviews.append(reviews_array)
        return recipes, reviews

    def scrape(self, page_num=1, step_size=1):
        recipe_iter = RecipeLinks(page_num, step_size)
        while not recipe_iter.isLastPage():
            recipe_links = recipe_iter.nextRecipeLinks()
            recipes, reviews = self.parseRecipeLinks(recipe_links)
            self.writeIteration(recipes, reviews, recipe_iter.getPage())
        print("Done Scraping.")

test = Scraper('recipes1.data', 'reviews1.data', 'log1.log')
test.scrape(1, 1)
