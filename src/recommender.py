from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(filepath: str) -> list:
    """Loads songs from a CSV file and converts numerical columns to floats/ints."""
    songs = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric fields to float/int for math operations
            row['id'] = int(row['id'])
            row['tempo_bpm'] = int(row['tempo_bpm'])
            row['energy'] = float(row['energy'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs


def score_song(user_prefs: dict, song: dict) -> tuple:
    """Calculates a similarity score and generates a list of reasons based on user preferences."""
    score = 0.0
    reasons = []

    # 1. Genre Match (+2.0 points)
    if song.get('genre') == user_prefs.get('favorite_genre'):
        score += 2.0
        reasons.append("Exact genre match (+2.0)")

    # 2. Mood Match (+1.0 point)
    if song.get('mood') == user_prefs.get('favorite_mood'):
        score += 1.0
        reasons.append("Exact mood match (+1.0)")

    # 3. Energy Similarity (Up to +1.0 point)
    if 'energy' in song and 'target_energy' in user_prefs:
        energy_diff = abs(song['energy'] - user_prefs['target_energy'])
        energy_score = max(0.0, 1.0 - energy_diff)
        score += energy_score
        reasons.append(f"Energy match (+{energy_score:.2f})")

    # 4. Acousticness Similarity (Up to +1.0 point)
    if 'acousticness' in song and 'target_acousticness' in user_prefs:
        acoustic_diff = abs(song['acousticness'] - user_prefs['target_acousticness'])
        acoustic_score = max(0.0, 1.0 - acoustic_diff)
        score += acoustic_score
        reasons.append(f"Acousticness match (+{acoustic_score:.2f})")

    return score, reasons


def recommend_songs(user_prefs: dict, songs: list, k: int = 5) -> list:
    """Scores all songs and returns the top k recommendations sorted highest to lowest."""
    scored_songs = []
    
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append({
            'song': song,
            'score': score,
            'reasons': reasons
        })

    top_songs = sorted(scored_songs, key=lambda x: x['score'], reverse=True)
    return top_songs[:k]
