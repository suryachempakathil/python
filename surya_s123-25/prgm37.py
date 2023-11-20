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
        self.no_of_pages=no
        Book.__init__(self,title1,author1,name1)
    def show(self):
        print('Book title:',self.title)
        print('author:',self.author)
        print('publisher:',self.name)
        print('price:Rs.',self.price)
        print('no of pages:',self.no_of_pages)
P1=Python(700,300,'Programming with Python','GV Rossum','ABC Books')
P1.show()
