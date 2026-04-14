"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from pathlib import Path
from src.recommender import load_songs, recommend_songs

def main():
    print("Initializing PawPal Recommender System...")
    
    # 1. Load the data
    filepath = Path(__file__).resolve().parents[1] / "data" / "songs.csv"
    songs = load_songs(str(filepath))
    print(f"Loaded songs: {len(songs)}\n")

    # 2. Define a default user profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_acousticness": 0.20
    }

    print(f"Target Profile: {user_prefs['favorite_genre'].upper()} | {user_prefs['favorite_mood'].upper()}\n")
    print("-" * 50)

    # 3. Get recommendations
    top_k = 3
    recommendations = recommend_songs(user_prefs, songs, k=top_k)

    # 4. Print results neatly
    for i, rec in enumerate(recommendations, 1):
        song = rec['song']
        print(f"#{i} | {song['title']} by {song['artist']}")
        print(f"   Score: {rec['score']:.2f}/5.00")
        print(f"   Why: {', '.join(rec['reasons'])}")
        print("-" * 50)

if __name__ == "__main__":
    main()