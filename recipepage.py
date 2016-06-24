from recipe import Recipe
from review import Review
import lxml.html
import urllib2
import re

class RecipePage:

    ENDPOINT = 'http://allrecipes.com'
    REVIEWS_ENDPOINT = 'http://allrecipes.com/recipe/getreviews/?recipeid='
    LINK_REGEX = '/recipe/([0-9]+)/.*'
    REVIEWS_TAG = './/div[@itemprop="review"]'

    def __init__(self, link):
        data = urllib2.urlopen(self.ENDPOINT + link).read()
        self.lxml_data = lxml.html.fromstring(data).xpath('//body')[0]
        self.id = re.match(self.LINK_REGEX, link).group(1)

    def getRecipe(self):
        recipe = Recipe()
        recipe.parsePage(self.lxml_data, self.id)
        return recipe

    def getReviews(self):
        reviews_array = []
        i = 1
        data = urllib2.urlopen(self.REVIEWS_ENDPOINT + self.id + '&pagenumber=' + str(i) + '&pagesize=50&recipeType=Recipe&sortBy=MostHelpful').read()
        lxml_data = lxml.html.fromstring(data)
        reviews = lxml_data.xpath(self.REVIEWS_TAG)
        while len(reviews) != 0:
            for review in reviews:
                r = Review()
                r.parseReview(review, self.id)
                reviews_array.append(r)
            i += 1
            try:
                data = urllib2.urlopen(self.REVIEWS_ENDPOINT + self.id + '&pagenumber=' + str(i) + '&pagesize=50&recipeType=Recipe&sortBy=MostHelpful').read()
                lxml_data = lxml.html.fromstring(data)
                reviews = lxml_data.xpath(self.REVIEWS_TAG)
            except:
                # Assume if we cannot get the next page of the reviews, then there are no more reviews
                reviews = {}
        return reviews_array
