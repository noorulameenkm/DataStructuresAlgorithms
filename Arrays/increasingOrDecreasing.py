def identify_titles(scores):
    increasing = decreasing = True

    for i in range(len(scores) - 1):
        if scores[i] > scores[i + 1]:
            increasing = False
        if scores[i] < scores[i + 1]:
            decreasing = False

    return increasing or decreasing


# Driver code
movie_ratings = [
    [1, 2, 2, 3],
    [4, 5, 6, 3, 4],
    [8, 8, 7, 6, 5, 4, 4, 1]
]

for movie_rating in movie_ratings:
    if identify_titles(movie_rating):
        print("Title Identified and Separated")
    else:
        print("Title Score Fluctuating")
