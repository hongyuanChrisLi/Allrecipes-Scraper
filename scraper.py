from recipelinks import RecipeLinks
from recipepage import RecipePage
import threading

class Scraper:

    def __init__(self, recipe_path='D:/recipes.txt', review_path='D:/reviews.txt', log_path='D:/log.txt', num_threads=1):
        self.recipe_path = recipe_path
        self.review_path = review_path
        self.log_path = log_path
        self.num_threads = num_threads
        self.file_writer = Scraper.FileThread()

    def execute(self):
        thread_tracker = {}
        for i in xrange(self.num_threads):
            thread_tracker[i] = Scraper.WorkerThread()

        recipe_iter = RecipeLinks()
        while not recipe_iter.isLastPage():
            recipe_links = recipe_iter.nextRecipeLinks()

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

test = Scraper(num_threads=8)
