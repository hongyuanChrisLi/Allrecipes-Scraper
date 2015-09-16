import json
from lxml import etree

class Recipe:

    NUTRIENT_TAG = '//ul[@class="nutrientLine"]'

    def __init__(self):
        self.properties = {}

    def parsePage(self, lxml_data):
        self.parseAttributes(lxml_data)
        self.parseNutrition(lxml_data)
        self.parseIngredients(lxml_data)
        self.parseInstructions(lxml_data)

    def parseNutrition(self, lxml_data):
        nutrients = lxml_data.xpath(self.NUTRIENT_TAG)
        for nutrient in nutrients:
            values = nutrient.xpath('.//li')
            key = values[0].text.split(':', 1)[0]
            print key
            value = values[1].text_content()
            print value
            self.properties[key] = value

    def parseIngredients(self, lxml_data):
        return None

    def parseAttributes(self, lxml_data):
        return None

    def parseInstructions(self, lxml_data):
        return None

    def toJSON(self):
        return json.dumps(self.properties)
