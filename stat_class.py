class Stat:
    def __init__(self, new_name):
        self.char_name = new_name
        self.rolls = {
            "str": [],
            "spd": [],
            "int": [],
            "cbt": [],
            "sanity": [],
            "fear": [],
            "body": []
        }

    def __str__(self):
        stat_str = [f"Name: {self.char_name}",
                    f"str: {self.rolls['str']}",
                    f"spd: {self.rolls['spd']}",
                    f"int: {self.rolls['int']}",
                    f"cbt: {self.rolls['cbt']}",
                    f"sanity: {self.rolls['sanity']}",
                    f"fear: {self.rolls['fear']}",
                    f"body: {self.rolls['body']}"]

        return "\n".join(stat_str)
