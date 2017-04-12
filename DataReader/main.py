import Business as Bus
import fileReader as fr
import Review as Rev

def main(args):
    business_class = []
    b = fr.Business_Maker()
    businesses = b.make("Business_Subset.txt")
    r = fr.Review_Maker()
    reviews = r.make("Reviews.txt")
    #print(bus)
    ID = 0
    TEXT = 2
    NAME = 0
    RATING = 1
    for review in reviews:
        count = 0
        found = False
        text = []
        if not business_class:#if the business_class list is empty add one review
            text.append(reviews[review][TEXT].split("_"))
            business_class.append(
                Bus.Business(reviews[review][ID], text, businesses[reviews[review][NAME]],
                             int(reviews[review][RATING])))
            continue
        for business in business_class:
            count +=1
            text.append(reviews[review][TEXT].split("_"))
            if business.getID() == reviews[review][ID]:
                found = True
            if found:
                business.addStars(int(reviews[review][RATING]))
                business.addOneReview(text)
                break
            if found == False and count == len(business_class):
                business_class.append(Bus.Business(reviews[review][ID],text,businesses[reviews[review][NAME]], int(reviews[review][RATING])))
                break

    print(business_class)


if __name__ == "__main__":
    import sys
    main(sys.argv)