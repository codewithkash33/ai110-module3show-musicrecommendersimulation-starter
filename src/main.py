"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.35}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.92}),
        ("Conflict Case", {"genre": "pop", "mood": "sad", "energy": 0.9}),
    ]

    for profile_name, user_prefs in profiles:
        print(f"\n=== Profile: {profile_name} ===")
        print(f"Preferences: genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}\n")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
