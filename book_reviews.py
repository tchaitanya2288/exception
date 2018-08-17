class Book:
    def __init__(self,id,name,author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.id,self.name,self.author,self.reviews))

    def add_review(self,review):
        self.reviews.append(review)


class Review:
    def __init__(self,id ,description,rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id,self.description,self.rating))

book = Book(123,'Python','Guido Ran vassum')
book.add_review(Review(100, 'good', 4))
book.add_review(Review(100,'Awesome',5))
print(book)
print(Review(100, 'good', 4))
