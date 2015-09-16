import lxml.html
import urllib2

n = 1
recipes = []
while n == 1 or len(recipes) != 0:
    data = urllib2.urlopen("http://allrecipes.com/recipes/?grouping=all&page=" + str(n) + "#" + str(n)).read()
    lxml_data = lxml.html.fromstring(data)
    recipes = lxml_data.xpath('//article[@class="grid-col--fixed-tiles"]')
    for recipe in recipes:
        link = recipe.xpath('.//a')[0]
        print link.get("href")
    print n
    n += 1