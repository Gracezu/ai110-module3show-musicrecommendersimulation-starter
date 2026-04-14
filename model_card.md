# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0** ---

## 2. Intended Use  

This recommender is designed to suggest songs based on a user's specific acoustic preferences and mood. It assumes the user knows exactly what they want in terms of energy level, acousticness, and genre. This model is built for classroom exploration and simulation to understand content-based filtering. It is **not** intended for commercial use or for replacing real dynamic recommenders (like Spotify), as it relies on a tiny, static dataset and explicit manual inputs rather than learning from user listening habits.


## 3. How the Model Works  

VibeFinder 1.0 uses a "Content-Based Filtering" approach. It compares the features of every song (genre, mood, energy, and acousticness) against the user's ideal taste profile. 

The model acts like a judge scoring a routine out of 5.0 points:
- It awards points for exact text matches (e.g., +1.0 for the right genre, +1.0 for the right mood).
- It calculates "distance" for numbers. If a user wants 0.8 energy and the song is 0.7, it deducts a small amount of points for being slightly off. 
- During testing, I changed the starter logic to cut the genre weight in half and double the energy weight. This ensures the system prioritizes the actual "sound" of the music over the text label.


## 4. Data  

The dataset uses a highly simplified catalog of only 10 songs stored in a `songs.csv` file. It features a very basic spread of genres (Pop, Lofi, Rock) and moods (Happy, Chill, Sad). Because the dataset is so small, it is missing massive parts of musical taste, including hip-hop, classical, EDM, and global music. It also lacks temporal data (like release year) which is a huge factor in real musical taste.

## 5. Strengths  

The system works incredibly well for straightforward user profiles. If a user wants "high-energy pop" or "low-energy acoustic lofi," the math beautifully pushes the exact right songs to the top of the list. The linear distance calculation handles opposite preferences perfectly, ensuring that a user looking for a relaxing acoustic track is never accidentally recommended a loud digital dance track. 


## 6. Limitations and Bias 

The current scoring logic exhibits a strict "filter bubble" bias regarding categorical data. Because the system relies heavily on exact string matching for genre and mood, it unfairly penalizes tracks that are functionally identical but tagged slightly differently (e.g., scoring 0 points for an "indie pop" track when the user wants "pop"). Furthermore, calculating the energy gap via linear absolute distance assumes perfectly symmetrical preferences. In reality, a user looking for a high-intensity workout song (0.80 energy) might be perfectly happy being recommended a 0.95 energy song, but absolutely hate a 0.65 energy song, even though both are mathematically separated by exactly 0.15 points from their target.


## 7. Evaluation  

I tested the system using a CLI simulation with three distinct user profiles: "High-Energy Pop", "Chill Lofi", and an adversarial "Deep Intense Rock" profile. 

What surprised me the most was how the adversarial profile (which wanted a "sad" mood but exceptionally high energy) exposed a major flaw in my original logic. Because the system initially weighted genre matches so heavily (+2.0 points), it kept recommending slow, sad rock songs to this profile, completely ignoring the user's demand for high energy. It taught me that strict category matching (like genre) can easily overpower the actual "vibe" or mathematical sound of the music, leading to bad recommendations for users with unique or conflicting tastes.


## 8. Future Work  

If I were to keep developing this project, I would:
1. **Fuzzy Text Matching:** Allow the system to recognize that "indie rock" and "rock" are similar and award partial points, rather than a hard zero.
2. **Expand the Dataset:** Connect the system to the real Spotify API to test it against millions of songs rather than just 10.
3. **Hybrid Filtering:** Add a "Collaborative Filtering" element so the system can recommend songs based on what *other* similar users are listening to, rather than just relying on math.


## 9. Personal Reflection  

My biggest learning moment during this project was realizing how easily a rigid algorithm can fail when faced with conflicting human preferences (like wanting "sad" but "high energy" music). It was surprising to see how just a few lines of basic math (addition and absolute distance) could actually "feel" like a personalized recommendation engine when the data aligned perfectly. 

Using AI tools like Copilot was incredibly helpful for generating edge-case testing profiles and writing the boilerplate Python code. However, I had to double-check the AI heavily during the weight-shifting experiment. The AI suggested the syntax, but *I* had to evaluate the actual output to determine if the math was producing recommendations that made logical sense to a human ear. This project totally changed how I view apps like Spotify; I now realize their "magic" is just thousands of weighted data points battling it out behind the scenes.