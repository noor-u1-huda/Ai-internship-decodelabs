# Noor Ul Huda
# DecodeLabs Internship Project 3
# Content-Based Recommendation System using Python

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


print("==========================================")
print(" DecodeLabs - AI Internship Project 3")
print(" Content-Based Recommendation System")
print(" Submitted by: Noor Ul Huda")
print("==========================================\n")

#Creating Dataset
data = {
    "movie_id": [1, 2, 3, 4, 5, 6],
    
    "title": [
        "The Matrix",
        "Inception",
        "Toy Story",
        "Finding Nemo",
        "The Godfather",
        "Interstellar"
    ],

    "genres": [
        "sci-fi action futuristic virtual-reality",
        "sci-fi thriller dream psychological",
        "animation children comedy family",
        "animation adventure ocean family",
        "crime drama mafia thriller",
        "sci-fi space adventure emotional"
    ]
}

# creating dataframe
df = pd.DataFrame(data)

print("Movie Dataset:\n")
print(df)


# STEP 2 : Checking Missing Values
print("\nChecking Missing Values:\n")
print(df.isnull().sum())

#Feature Engineering / Vectorization
tfidf = TfidfVectorizer()

feature_matrix = tfidf.fit_transform(df["genres"])

print("\nTF-IDF Feature Matrix Created Successfully")

#Similarity Calculation
similarity_matrix = cosine_similarity(feature_matrix)

print("\nSimilarity Matrix Generated Successfully")

# STEP 5 : Recommendation Function
def recommend_movies(movie_name, top_n=3):

    # checking movie existence
    if movie_name not in df["title"].values:
        print("\nMovie not found in dataset")
        return

    # getting movie index
    movie_index = df[df["title"] == movie_name].index[0]

    # similarity scores
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    # sorting scores in descending order
    sorted_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sorted_scores = sorted_scores[1:top_n + 1]

    print("\n===================================")
    print(" Recommended Movies")
    print("===================================")

    recommendations = []

    for movie, score in sorted_scores:

        recommendations.append({
            "Movie": df.iloc[movie]["title"],
            "Similarity Score": round(score, 3),
            "Genres": df.iloc[movie]["genres"]
        })

    result_df = pd.DataFrame(recommendations)

    print(result_df)

    return result_df

#Testing Recommendation System
recommend_movies("The Matrix")

recommend_movies("Toy Story")


#Similarity Visualization
def plot_similarity(movie_name):

    if movie_name not in df["title"].values:
        print("Movie not found")
        return

    movie_index = df[df["title"] == movie_name].index[0]

    scores = similarity_matrix[movie_index]

    plt.figure(figsize=(8, 5))

    plt.bar(df["title"], scores)

    plt.xlabel("Movies")
    plt.ylabel("Similarity Score")

    plt.title(f"Similarity with {movie_name}")

    plt.xticks(rotation=20)

    plt.show()


# visualization
plot_similarity("The Matrix")