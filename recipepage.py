from recipe import Recipe
from review import Review
import lxml.html
import urllib2
import re

class RecipePage:

    ENDPOINT = 'http://allrecipes.com'
    LINK_REGEX = '/recipe/([0-9]+)/*'

    def __init__(self, link):
        data = urllib2.urlopen(self.ENDPOINT + link).read()
        self.lxml_data = lxml.html.fromstring(data).xpath('//body')[0]
        self.id = re.match(self.LINK_REGEX, link).group(1)

    def getRecipeReview(self):
        recipe = Recipe()
        recipe.parsePage(self.lxml_data, self.id)
        # review = Review()
        # review.parsePage(self.lxml_data)
        print recipe.toJSON() #, review.toJSON()

test = RecipePage('/recipe/24002/famous-butter-chicken/')
test.getRecipeReview()
