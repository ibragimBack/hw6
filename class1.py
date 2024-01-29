from art import tprint
class Hello:
    def __init__(self, string):
        self.string = string

class Bie(Hello):
    def art(self):
        tprint('bie bie ' + self.string)

obj = Bie('teacher')
