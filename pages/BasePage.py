import os
class Basepage:
    def __init__(self,page):
        self.page= page
        self.base_url = os.getenv("base_url")
    def navigate(self,relative_url=""):
        self.page.goto(f"{self.base_url}{relative_url}")
