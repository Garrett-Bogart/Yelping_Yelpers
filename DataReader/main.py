import Business as Bus
import fileReader as fr
import language_check
from tkinter import *

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
            stars = []
            text.append(reviews[review][TEXT].replace("_", " "))
            stars.append(int(reviews[review][RATING]))
            business_class.append(
                Bus.Business(reviews[review][ID], text, businesses[reviews[review][NAME]],
                             stars))
            continue
        for business in business_class:
            count += 1
            text.append(reviews[review][TEXT].replace("_", " "))
            if business.getID() == reviews[review][ID]:
                found = True
            if found:
                business.addOneStar(int(reviews[review][RATING]))
                business.addOneReview(text)
                break
            if found == False and count == len(business_class):
                temp = []
                temp.append(int(reviews[review][RATING]))
                business_class.append(Bus.Business(reviews[review][ID], text, businesses[reviews[review][NAME]],
                                                   temp))
                break
    return business_class


def grammarCheck(business_class):
    tool = language_check.LanguageTool('en-US')
    for business in business_class:
        reviews = business.getReviews()
        for review in reviews:
            temp = str(review)
            mistakes=tool.check(temp)
            business.addOneError((len(mistakes)))
        #print(business)
        business.getAdjustedRating()
    return


def query(restaraunt, business_class):
    temp = []
    for business in business_class:
        if business.getName() == restaraunt:
            temp.append(business)
    print(temp)
    return temp


def main(args):
    business_index = make_business_dictionary()
    print(business_index)
    return make_business_dictionary()
    #print(business_class)
    #done = True
    #while done:
        #prompt = input("find a restaurant: ")
        #if args == "done":
            #done = False
            #break
        #else:
            #return query(args, business_class)

def print_output():
    search = search_query.get()
    results = query(search,index)
    label2 = Label(top, text = results).place(x = 0, y = 30)

def make_index():
    global index
    index = []
    index = main('blank')


top = Tk()
search_query = StringVar()

top.geometry('450x450')
top.title("Yelping Yelpers")

Button1 = Button(top,text = 'search', command = print_output).place(x = 0, y = 0,width = 120, height = 25)
Button2 = Button(top,text = 'make index',command = make_index).pack(side =BOTTOM)
Entry1 = Entry(top,textvariable = search_query).place(x = 130, y = 0,width = 120, height = 25)
top.mainloop()

