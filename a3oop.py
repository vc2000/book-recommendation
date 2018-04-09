import csv
from math import sqrt

def open_file(file_name):
    data= csv.reader(open("BX-" + file_name + ".csv",'r',encoding='utf-8', errors='ignore'))
    return data

isbn_book={}
for lis in open_file("Books"):
    sep = lis[0].split(';')
    isbn = sep[0].replace("'",'')
    bkName = sep[1].replace("'",'')
    isbn_book[isbn] = bkName


###########################################

Ratings={}
count = 0
for line in open_file("Book-Ratings"):
    if count > 0 :
        sep = line[0].split(';')
        try:
            user = sep[0]
            isbn = sep[1].replace('"','')
            rate = float(sep[2].replace('"',''))
        except:
            i = 0
        dic = {}
        dic[isbn] = rate

        if user in Ratings:
            Ratings[user].update(dic)
        else:
            Ratings[user] = dic

    count += 1

#print(Ratings['171118'])


#################################################################
class Recommendations:
    def __init__(self,r,rating1,rating2):
        self.r = r
        self.rating1 = rating1
        self.rating2 = rating2

    def minkoski(self):

        distance = 0
        commonRatings = False
        for key in self.rating1:
            if key in self.rating2:
                distance += (abs(self.rating1[key] - self.rating2[key]) ** r)
                commonRatings = True
        if commonRatings:

            if self.r == 2:
                new = round(distance ** (1/r),2)
                return new
            else:
                return distance
        else:
            return -1 #Indicates no ratings in common
    def pearson(self,rate1,rate2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rate1:
            if key in rate2:
                n += 1
                x = rate1[key]
                y = rate2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0
        # now compute denominator
        denominator = (sqrt(sum_x2 - pow(sum_x, 2) / n)
                       * sqrt(sum_y2 - pow(sum_y, 2) / n))
        if denominator == 0:
            return 0
        else:
            ok =(sum_xy - (sum_x * sum_y) / n) / denominator
            return round(ok,2)

    def computeNearestNeighbor(self):

        distances = []
        for user in self.rating2:
            if user != self.rating1:
                if self.r == 1:
                    distance = self.minkoski(self.r ,self.rating2[user], self.rating2[self.rating1])
                    distances.append((distance, user))
                    distances.sort()
                elif self.r==2:
                    distance = self.minkoski(self.r,self.rating2[user], self.rating2[self.rating1])
                    distances.append((distance, user))
                    distances.sort()
                else:
                    distance = self.pearson(self.rating2[user], self.rating2[self.rating1])
                    distances.append((distance, user))
                    distances.sort(reverse=True)


        # sort based on distance -- closest first

        return distances

    def recommend(self):

        # first find nearest neighbor
        nearest = self.computeNearestNeighbor()[0][1]

        recommendations = []
        # now find bands neighbor rated that user didn't
        neighborRatings = self.rating2[nearest]
        userRatings = self.rating2[self.rating1]
        for artist in neighborRatings:
            if not artist in userRatings:
                recommendations.append((artist, neighborRatings[artist]))


        # using the fn sorted for variety - sort is more efficient

        return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)




######################################################3
userId = str(input("User ID : "))
r = 3
Recommendations(r,userId,Ratings).computeNearestNeighbor
result=Recommendations(r,userId,Ratings).recommend
print("Recommendations using Pearson:")

num = 0

for i in result():
    try:
        print(i[0],isbn_book[i[0]],i[1])
    except:
        print(str(i[0]) + "   No name   " + str(i[1]))
    num += 1
    if num ==20:
        break
