import json


class ScenarioLoader:

    def __init__(self, path):

        with open(path, encoding="utf-8") as f:

            self.data = json.load(f)

    def get_turn(self, turn):

        return self.data["turns"][turn - 1]
