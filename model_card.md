# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder Lite**

---

## 2. Intended Use

This recommender suggests 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is designed for classroom exploration and demonstration, not for production use.

The model assumes a user can be represented by a few taste preferences and that songs can be compared using metadata like genre, mood, and energy.

---

## 3. How the Model Works

Each song is scored by comparing it to the user's preferences. The model adds points for matching genre and mood, then adds a larger score for how close the song's energy is to the user's preferred energy.

That means songs with the right vibe and similar intensity will rise to the top. The model explains recommendations with simple reasons like "genre match" and "energy similarity."

---

## 4. Data

The dataset contains 18 songs in `data/songs.csv`. It includes genres such as pop, lofi, rock, ambient, jazz, synthwave, indie pop, electronic, classical, country, reggae, hip-hop, metal, and funk.

Moods include happy, chill, intense, relaxed, moody, focused, sad, romantic, and upbeat. I added eight new songs to broaden the range of styles and to support more diverse profile testing.

The dataset is still tiny and missing many real music factors like lyrics, artist popularity, user listening history, and contextual signals such as time of day.

---

## 5. Strengths

The recommender works well for clear profiles where genre and mood match strongly. For example, the Chill Lofi profile correctly surfaces lofi songs with chill mood and low energy.

It is easy to understand because each score is built from a few weighted rules, so the output feels transparent rather than mysterious.

---

## 6. Limitations and Bias

The system can still over-prioritize energy and genre because those features are weighted heavily. When a profile has conflicting preferences, like high energy with sad mood, the model often prefers energetic pop songs over lower-energy sad songs.

The catalog is small and skewed toward recognizable styles, so there is a filter bubble effect: the same few songs may appear in many top lists. The model also ignores important music preferences like tempo and lyrical content.

---

## 7. Evaluation

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflict profile that asked for pop genre with sad mood.

I looked for whether the top results matched the requested vibe. The Chill Lofi profile behaved as expected, but the conflict profile showed a clear weakness: genre and energy still pushed pop songs to the top even though the mood was sad.

I also ran an experiment by shifting the weights so energy similarity became twice as important and genre weight was halved. This made energy have more influence, but it did not fully fix edge cases because the dataset is small and genre still matters.

---

## 8. Future Work

I would add tempo, valence, and acoustic preference as additional score features. I would also add more songs and incorporate user behavior data like skips or playlist adds.

A next step would be to introduce diversity penalties so the top recommendations include more distinct genres instead of repeating the same strong match.

---

## 9. Personal Reflection

I learned that even a simple recommender can feel reasonable for obvious profiles, but it is easy to mislead with conflicting preferences. The exercise showed that small catalogs and weighted rules create predictable biases, and that real systems need more signals than just genre, mood, and energy.
