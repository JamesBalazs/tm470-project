from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Article title: article description; taken from various RSS feeds
feeds = {
    "sky_news": [
        "Greece shuts schools and Acropolis as heatwave hits: Greece has shuttered tourist hotspots and schools across Athens as the first heatwave of the summer strikes.",
        "'These are impossible conditions': Mother of freed hostage feared the worst for son held by Hamas: Evgeniia Kozlova was at home in St Petersburg last weekend when she got the call from her Israeli liaison officers.",
        "Post Office campaigner Alan Bates given knighthood - but insists there's still 'work to do': The campaigner has insisted the honour won't change his life, while his wife Suzanne told Sky News she is \"very proud\" of her \"very deserving\" husband.",
    ],
    "bbc_news": [
        "Greek schools close because of 'historic' heatwave: Lots of schools in Greece have shut as the country experiences its first heatwave of the summer.",
    ],
    "reuters": [
        "Freed hostage from Gaza needs 'time to heal', loved ones say: The mother of Andrey Kozlov, a hostage freed from Gaza, says she's the 'happiest' she's ever been",
        "Pentagon ran secret anti-vax campaign to undermine China during pandemic: The U.S. military launched a clandestine program amid the COVID crisis to discredit China’s Sinovac inoculation – payback for Beijing’s efforts to blame Washington for the pandemic. One target: the Filipino public. Health experts say the gambit was indefensible and put innocent lives at risk.",
    ],
    "japan_times": [
        "U.S. ran secret anti-vaccine campaign to undermine China during pandemic: At the height of the COVID-19 pandemic, the U.S. military launched a secret campaign to counter what it perceived as China’s growing influence in the Philippines, a nation hit especially hard by the deadly virus.",
    ],
}

embeddings = {}
for group, articles in feeds.items():
    embeddings[group] = [ model.encode(article) for article in articles ]

similarities = {}
for group1, embeddings1 in embeddings.items():
    for group2, embeddings2 in embeddings.items():
        if group1 == group2:
            continue

        if f"{group2},{group1}" in similarities:
            continue

        # cosine similarity
        similarities[f"{group1},{group2}"] = model.similarity(embeddings1, embeddings2)

for groups, scores in similarities.items():
    group1, group2 = groups.split(',')

    for idx_i, sentence1 in enumerate(feeds[group1]):
        print(f"{group1} {idx_i}:")
        for idx_j, sentence2 in enumerate(feeds[group2]):
            print(f" - {group2} {idx_j: <30}: {scores[idx_i][idx_j]:.4f}")
