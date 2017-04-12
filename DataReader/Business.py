class Business:
    def __init__(self, id = None, reviews = None, name = None, stars = None):
        if id is None:
            self.businessID = ""
        else:
            self.businessID = id
        if reviews is None:
            self.reviews = []
        else:
            self.reviews = reviews
        if name is None:
            self.name = ""
        else:
            self.name = name
        if stars is None:
            self.stars = 0
        else:
            self.stars = stars

    def addReviews(self, revs):
        self.reviews = revs

    def addOneReview(self, rev):
        self.reviews.append(rev)

    def getName(self):
        return self.name

    def getID(self):
        return self.businessID

    def addStars(self, add):
         self.stars +=add

    def getRanking(self):
        return self.stars/len(self.reviews)

    def __repr__(self):
        #return self.name +" "+ self.businessID +" "+ str(self.stars)+" "+ str(len(self.reviews))
        return self.name +" "+ str(self.getRanking())
