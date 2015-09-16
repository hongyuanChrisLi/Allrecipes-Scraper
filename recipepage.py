from recipe import Recipe
from review import Review
import lxml.html
import urllib2

class RecipePage:

    ENDPOINT = 'http://allrecipes.com'

    def __init__(self, link):
        print 'Getting ' + link
        data = urllib2.urlopen(self.ENDPOINT + link).read()
        print 'Page retrieved'
        self.lxml_data = lxml.html.fromstring(data)

    def getRecipeReview(self):
        print 'Processing'
        recipe = Recipe()
        recipe.parsePage(self.lxml_data)
        review = Review()
        review.parsePage(self.lxml_data)
        print 'Recipe and reviews parsed'
        return recipe.toJSON(), review.toJSON()

test = RecipePage('/recipe/24002/famous-butter-chicken/')
print test.getRecipeReview()
