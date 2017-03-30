import json

fin = open("yelp_dataset_challenge_round9.002", "r", encoding = "utf8")
#count = 0
finalData = []
formated = []
for line in fin:
    temp = ""
    for letter in line:
        if letter.isalnum():
            temp+=letter
        else:
            if letter ==",":
                temp+=' '
            if letter == "_":
                temp+='_'
            if letter == "-":
                temp+='-'
            if letter == ":":
                temp+=':'
    #if(count < 100):
        #print(temp)
    #count+=1
    formated.append(temp)

compressed_data = []
count = 0
for business in formated:
   compress = business.split()
   for word in compress:
        temp = word.split(':')
        for w in temp:
            if w == 'business_id':
                finalData.append(temp)
            if w == 'state':
                finalData.append(temp)
        #if count < 100:
            #print(temp)
            #count +=1

print(finalData)
#print(formated)

