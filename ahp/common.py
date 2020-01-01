import re

class Grade:
    def __init__(self):
        pat_str = "([A-Z0-9]+)-([A-Z0-9]+)"
        self.pat=re.compile(pat_str)

    def find(self, name):
        ret = self.pat.findall(name)
        if ret:
            return ret[0]

class Index:
    def __init__(self):
        pat_str = "([.0-9]+)[0-9]"
        self.pat=re.compile(pat_str)

    def find(self, name):
        ret = self.pat.findall(name)
        if ret:
            return ret[0]+'*'