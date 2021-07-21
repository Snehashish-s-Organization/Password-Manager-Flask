
class Password:
    def __init__(self, site, used, password):
        self.site = site
        self.used = used
        self.password = password

    def getSite(self):
        return self.site
    
    def getUsed(self):
        return self.used

    def getPassword(self):
        return self.password