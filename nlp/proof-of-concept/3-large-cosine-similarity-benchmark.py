from sentence_transformers import SentenceTransformer
import timeit, random
from urllib.request import urlopen

model = SentenceTransformer("all-MiniLM-L6-v2")

# get dictionary

mit_wordlist = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urlopen(mit_wordlist).read()
DICTIONARY = [ word.decode('utf8') for word in response.splitlines() ]

# Randomly generate 100 titles, 30 words long, from MIT word list

feeds_10x100 = {
    "1": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "2": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "3": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "4": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "5": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "6": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "7": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "8": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "9": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
    "10": [ ''.join(random.choices(DICTIONARY, k=30)) for i in range(100) ],
}

def calculate_embeddings(feeds):
    embeddings = {}
    for group, articles in feeds.items():
        embeddings[group] = model.encode(articles)

    return embeddings

def calculate_similarities(embeddings):
    similarities = {}
    for group1, embeddings1 in embeddings.items():
        for group2, embeddings2 in embeddings.items():
            if group1 == group2:
                continue

            if f"{group2},{group1}" in similarities:
                continue

            # cosine similarity
            similarities[f"{group1},{group2}"] = model.similarity(embeddings1, embeddings2)

    return similarities

BENCHMARK_REPETITIONS = 100

print('10x100 random embeddings: ', timeit.timeit("calculate_embeddings(feeds_10x100)", globals=globals(), number=BENCHMARK_REPETITIONS))

embeddings_10x100 = calculate_embeddings(feeds_10x100)
print('10x100 random similarities: ', timeit.timeit("calculate_similarities(embeddings_10x100)", globals=globals(), number=BENCHMARK_REPETITIONS))
