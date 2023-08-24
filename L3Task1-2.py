import pandas as pd
import numpy as np

# Reads the data
data = pd.read_csv("Dataset.csv")

# Gets the length of each review
review_lengths = []
for review in data["Rating text"]:
    review_lengths.append(len(review))

# Calculates the average review length
average_review_length = np.mean(review_lengths)

print("The average review length is", average_review_length)

# Create a list of ratings
ratings = data["Aggregate rating"]

# Calculate the correlation coefficient between review length and rating
correlation = np.corrcoef(review_lengths, ratings)[0, 1]

# Print the correlation coefficient
print("The correlation between review length and rating is:", correlation)
