import json

class Review:
    def __init__(self):
        self.properties = {}

    def parsePage(self, lxml_data):
        self.parseAttributes(lxml_data)

    def parseAttributes(self, lxml_data):
        return None

    def toJSON(self):
        return json.dumps(self.properties)