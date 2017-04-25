import math


class Business:
    def __init__(self, id = None, reviews = None, name = None, stars = None):
        self.adjusted_rating = 0
        self.error_list = []

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
            self.stars = []
        else:
            self.stars = stars

    def addReviews(self, revs):
        self.reviews = revs

    def addOneReview(self, rev):
        self.reviews.append(rev)

    def addOneError(self,error):
        self.error_list.append(error)

    def addOneStar(self,star):
        self.stars.append(star)

    def getReviews(self):
        return self.reviews

    def getName(self):
        return self.name

    def getID(self):
        return self.businessID

    def addStars(self, add):
         self.stars +=add

    def getRanking(self):
        total = 0
        for star in self.stars:
            total += star
        return total/len(self.reviews)

    def getAdjustedRating(self):
        total = 0
        #temp = 0
        error_total = 0
        for i in range(len(self.stars)):
            temp = 1/math.log10(10+self.error_list[i])
            error_total+=temp
            total += self.stars[i]*temp
        self.adjusted_rating = total/error_total

    def __repr__(self):
        return self.name +" Ranking:"+ str(self.getRanking())+" Adjusted Rating:"+str(self.adjusted_rating)
        #return str((self.stars, self.error_list))
        #return self.name +" "+ str(self.getRanking())
