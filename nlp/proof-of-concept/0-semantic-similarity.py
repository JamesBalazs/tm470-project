from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Article title: article description; taken from various RSS feeds
sky_news_articles = [
    "Greece shuts schools and Acropolis as heatwave hits: Greece has shuttered tourist hotspots and schools across Athens as the first heatwave of the summer strikes.",
    "'These are impossible conditions': Mother of freed hostage feared the worst for son held by Hamas: Evgeniia Kozlova was at home in St Petersburg last weekend when she got the call from her Israeli liaison officers.",
    "Post Office campaigner Alan Bates given knighthood - but insists there's still 'work to do': The campaigner has insisted the honour won't change his life, while his wife Suzanne told Sky News she is \"very proud\" of her \"very deserving\" husband.",
]
reuters_articles = [
    "Freed hostage from Gaza needs 'time to heal', loved ones say: The mother of Andrey Kozlov, a hostage freed from Gaza, says she's the 'happiest' she's ever been",
    "Pentagon ran secret anti-vax campaign to undermine China during pandemic: The U.S. military launched a clandestine program amid the COVID crisis to discredit China’s Sinovac inoculation – payback for Beijing’s efforts to blame Washington for the pandemic. One target: the Filipino public. Health experts say the gambit was indefensible and put innocent lives at risk.",
]

sky_news_embeddings = [ model.encode(sentences) for sentences in sky_news_articles]
reuters_embeddings = [ model.encode(sentences) for sentences in reuters_articles ]

# cosine similarity
similarities = model.similarity(sky_news_embeddings, reuters_embeddings)

for idx_i, sentence1 in enumerate(sky_news_articles):
    print(f"sky {idx_i}:")
    for idx_j, sentence2 in enumerate(reuters_articles):
        print(f" - reuters {idx_j: <30}: {similarities[idx_i][idx_j]:.4f}")
