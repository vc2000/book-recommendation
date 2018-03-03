import csv
from math import sqrt
books_file = csv.reader(open("BX-Books.csv",'r'))
ratings_file = csv.reader(open("BX-Book-Ratings.csv",'r'))


book_key=[]
for i


def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
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

def computeNearestNeighbor(username, users):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
            distance = pearson(users[user], users[username])
            distances.append((distance, user))
            distances.sort(reverse=True)


def recommend(username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, users)[0][1]

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))


    # using the fn sorted for variety - sort is more efficient

    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)


######################################################
name = str(input("Enter Name : "))

result= recommend(r,name,movie)
print("Recommendations using Pearson:")

count = 0
for i in result:
    if count < 20:
        print(i[0],i[1])
        count +=1
