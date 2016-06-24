import urllib2
import lxml.html

class RecipeLinks:

    ENDPOINT = 'http://allrecipes.com/recipes/?grouping=all&page='
    RECIPE_TAG = '//article[@class="grid-col--fixed-tiles"]'

    def __init__(self, page_num=1, step_size=1):
        self.page_num = page_num
        self.step_size = step_size
        self.last_page = False

    def getRecipeLinks(self, page_num):
        print 'Getting page #' + str(page_num)
        data = urllib2.urlopen(self.ENDPOINT + str(page_num) + "#" + str(page_num)).read()
        lxml_data = lxml.html.fromstring(data)
        recipes = lxml_data.xpath(self.RECIPE_TAG)
        recipe_links = []
        for recipe in recipes:
            link = recipe.xpath('.//a')[0]
            recipe_links.append(link.get("href").strip())
        return recipe_links

    def nextRecipeLinks(self):
        if not self.last_page:
            recipe_links = self.getRecipeLinks(self.page_num)
            if len(recipe_links) == 0:
                self.last_page = True
            else:
                self.page_num += self.step_size
            return recipe_links
        else:
            return []

    def isLastPage(self):
        return self.last_page

    def getPage(self):
        return self.page_num
