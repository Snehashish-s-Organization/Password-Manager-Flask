class Password:

    def __init__(self, sitename=None, password=None, email=None, username=None):
        self.sitename = sitename
        self.password = password
        self.email = email
        self.username = username

    def return_data(self):
        mydata = {
            "site_name":self.sitename,
            "site_password":self.password,
            "site_email":self.email,
            "site_username":self.username,
        
        }
        return mydata

