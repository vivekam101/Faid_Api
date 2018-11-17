from flask.json import JSONEncoder

class myJSONEncoder(JSONEncoder):
    def default(self, value):
        return JSONEncoder.default(self, value)