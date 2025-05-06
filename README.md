Here’s a detailed explanation you can use for your GitHub README that describes your project **"Google's CacheSack - Cache Admission Simulator"**, the theme, the code structure, and its relevance in real-world **Information-Centric Networking (ICN)** applications.

---

## 📦 Google's CacheSack - Cache Admission Simulator

### 🌐 Project Theme

**Google's CacheSack** is a simulation tool that models **cache admission control** using the **Least Frequently Used (LFU)** strategy. It is built using Python and Streamlit, enabling users to interactively request movie data and see how content is stored or evicted in a simulated edge cache.

This simulator demonstrates how intelligent caching mechanisms—particularly **LFU-based admission**—optimize content delivery in **Information-Centric Networking (ICN)**, an emerging internet architecture that emphasizes content rather than location (IP addresses).

---

### 🚀 Key Objectives

* To visualize the working of LFU cache management.
* To simulate cache hits and misses during user content requests.
* To relate cache simulation to **ICN edge caching strategies** for efficient content delivery.

---

### 🧠 ICN Architecture Relevance

In **ICN**, data is cached at intermediate nodes (like edge routers or servers), allowing content to be served more efficiently. Instead of always routing to a central origin server, ICN nodes serve frequently requested data locally.

**LFU admission control** plays a key role in:

* Reducing latency by increasing cache hit ratios.
* Efficiently managing limited edge cache capacity.
* Prioritizing content based on access frequency.

This project mimics this behavior using a movie dataset, allowing real-time interaction and visualization of cache operations.

---

### 🧩 Code Walkthrough

#### 1. **Libraries & Setup**

```python
import streamlit as st
import pandas as pd
from collections import defaultdict, OrderedDict
import os
```

* **Streamlit** for web UI
* **Pandas** for data handling
* **defaultdict & OrderedDict** to manage LFU cache state

#### 2. **Data Loading**

```python
@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    ...
```

Loads and prepares movie data (from TMDB dataset), with lowercase titles for easy matching.

#### 3. **LFU Cache Implementation**

```python
class LFUCache:
    ...
```

Core component implementing LFU logic:

* `freq`: tracks request count per item
* `cache`: holds currently admitted items (with capacity constraint)
* Eviction: when capacity is full, the least frequently used item is evicted.

#### 4. **Streamlit UI**

```python
st.title("📦 Google's CacheSack - Cache Admission Simulator")
...
```

* Allows users to search movie titles.
* Clicking "Request" simulates fetching content.
* If the movie is in cache → cache hit.
* Else → fetched from origin and added to cache.


Expands to show currently cached movie titles and their ratings.

---

### 🛠️ How to Use

1. **Clone the Repository:**

```bash
git clone https://github.com/Jsujanchowdary/-Google-s-CacheSack---Cache-Admission-Simulator
cd -Google-s-CacheSack---Cache-Admission-Simulator
```

2. **Run the App:**

```bash
streamlit run app.py
```

4. **Search and Request Movies:**
   Enter keywords like `war`, `spider`, or `love` to simulate a user request.

---

### 📘 Real-World Applications in ICN

This simulator reflects real-world ICN scenarios:

* **Edge Routers** and **CDNs** use LFU/other policies for content admission.
* Enhances **QoS** by reducing redundant fetches from origin servers.
* Supports **bandwidth efficiency** and **reduced latency** in 5G and IoT contexts.

---

### 📂 Dataset Source

Uses the publicly available [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

### 📢 Future Improvements

* Add support for other cache strategies (LRU, ARC, etc.)
* Simulate distributed caching across multiple nodes.
* Integrate visualization graphs for hit/miss statistics.

---

Would you like help formatting this into Markdown and adding it to your GitHub repo?
