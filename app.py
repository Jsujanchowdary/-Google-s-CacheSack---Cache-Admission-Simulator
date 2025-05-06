import streamlit as st
import pandas as pd
from collections import defaultdict, OrderedDict
import os

# Load and prepare dataset
@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df = df.drop_duplicates(subset='id')
    df['title_lower'] = df['title'].str.lower()
    return df

df = load_data()
title_to_id = dict(zip(df['title_lower'], df['id']))

# LFU Cache Class
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq = defaultdict(int)
        self.cache = OrderedDict()

    def request(self, movie_id):
        self.freq[movie_id] += 1

        if movie_id in self.cache:
            self.cache.move_to_end(movie_id)
            return True
        else:
            if len(self.cache) >= self.capacity:
                lfu = min(self.cache, key=lambda k: self.freq[k])
                del self.cache[lfu]
            self.cache[movie_id] = True
            return False

    def get_cache_contents(self):
        return list(self.cache.keys())

# Initialize cache in session state
if "lfu_cache" not in st.session_state:
    st.session_state.lfu_cache = LFUCache(capacity=100)

st.title("📦 Google's CacheSack - Cache Admission Simulator")
st.markdown("Optimizing Edge Cache with LFU Admission Control")
st.subheader("🔍 Search & Request Movies")
movie_input = st.text_input("Enter partial or full movie title (e.g., spider, war, love):").strip().lower()

if movie_input:
    matches = df[df['title_lower'].str.contains(movie_input)]

    if not matches.empty:
        st.write(f"Found {len(matches)} matching movies:")
        for _, row in matches.iterrows():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**🎬 {row['title']}**  \nGenre: {row['genres']}  \n⭐ Rating: {row['vote_average']}")

            with col2:
                if st.button(f"Request", key=row['id']):
                    movie_id = row['id']
                    from_cache = st.session_state.lfu_cache.request(movie_id)

                    if from_cache:
                        st.success(f"{row['title']} - ✅ Served from Cache")
                    else:
                        st.warning(f"{row['title']} - 🔄 Fetched from Origin Server & Cached")
    else:
        st.error("❌ No movies found with that keyword.")


# Show current cache content
with st.expander("📋 View Current Cache Contents"):
    cache_ids = st.session_state.lfu_cache.get_cache_contents()
    cached_movies = df[df['id'].isin(cache_ids)][['title', 'vote_average']]
    st.table(cached_movies.reset_index(drop=True))