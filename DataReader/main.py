import Business as Bus
import fileReader as fr

def make_business_dictionary():
    business_class = []
    b = fr.Business_Maker()
    businesses = b.make("Business_Subset.txt")
    r = fr.Review_Maker()
    reviews = r.make("Reviews.txt")
    # print(bus)
    ID = 0
    TEXT = 2
    NAME = 0
    RATING = 1
    for review in reviews:
        count = 0
        found = False
        text = []
        if not business_class:  # if the business_class list is empty add one review
            text.append(reviews[review][TEXT].replace("_", " "))
            business_class.append(
                Bus.Business(reviews[review][ID], text, businesses[reviews[review][NAME]],
                             int(reviews[review][RATING])))
            continue
        for business in business_class:
            count += 1
            text.append(reviews[review][TEXT].replace("_", " "))
            if business.getID() == reviews[review][ID]:
                found = True
            if found:
                business.addStars(int(reviews[review][RATING]))
                business.addOneReview(text)
                break
            if found == False and count == len(business_class):
                business_class.append(Bus.Business(reviews[review][ID], text, businesses[reviews[review][NAME]],
                                                   int(reviews[review][RATING])))
                break


    return business_class

def query(restaraunt, business_class):
    temp = []
    for business in business_class:
        if business.getName() == restaraunt:
            temp.append(business)
    print(temp)
    return temp

def main(args):
    business_class = make_business_dictionary()
    print(business_class)
    done = True
    while done:
        prompt = input("find a restaurant: ")
        if prompt == "done":
            done = False
            break
        else:
            query(prompt, business_class)



if __name__ == "__main__":
    import sys
    main(sys.argv)