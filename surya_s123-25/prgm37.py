class Publisher:
    def __init__(self,name1):
        self.name=name1
    def show(self):
        pass
class Book(Publisher):
    def __init__(self,title1,author1,name1):
        self.title=title1
        self.author=author1
        publisher.__init__(self,name1)
    def show(self):
        pass
class python(Book):
    def __init__(self,p,no,title1,author1,name1):
        self.price=p
