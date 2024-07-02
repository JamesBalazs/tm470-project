from sentence_transformers import SentenceTransformer

grouping_model = SentenceTransformer("all-MiniLM-L6-v2")

GROUPING_THRESHOLD = 0.6

def calculate_embeddings(feeds):
    for idx, feed in feeds.items():
        texts = [ f"{article['title']}: {article['body']}" for idy, article in feed['articles'].items() ]
        feeds[idx]['embeddings'] = grouping_model.encode(texts)

    return feeds

def calculate_similarities(feeds):
    similarities = {}

    for idx, feed1 in feeds.items():
        for idy, feed2 in feeds.items():
            if idx == idy:
                continue

            if f"{idy},{idx}" in similarities:
                continue

            # cosine similarity
            similarities[f"{idx},{idy}"] = grouping_model.similarity(feed1['embeddings'], feed2['embeddings'])

    return similarities

def any_group_contains_either(groups, article1, article2):
    for group_id, group in enumerate(groups):
        if article1['id'] in group or article2['id'] in group:
            return group_id

    return -1

def add_to_group_unless_present(groups, group_id, article1, article2):
    existing_group = groups[group_id]

    if article1 not in existing_group:
        groups[group_id] = groups[group_id] + [article1['id']]

    if article2 not in existing_group:
        groups[group_id] = groups[group_id] + [article2['id']]

    return groups

def group_by_similarity(feeds, similarities):
    groups = []

    for feed_ids, scores in similarities.items():
        feed1, feed2 = feed_ids.split(',')

        for idx, article1 in feeds[feed1]['articles'].items():
            for idy, article2 in feeds[feed2]['articles'].items():
                ilocx = list(feeds[feed1]['articles'].values()).index(article1) # for retrieving from similarities by location
                ilocy = list(feeds[feed2]['articles'].values()).index(article2) # for retrieving from similarities by location

                if scores[ilocx][ilocy] >= GROUPING_THRESHOLD:
                    found_group = any_group_contains_either(groups, article1, article2)
                    if found_group > -1:
                        groups = add_to_group_unless_present(groups, found_group, article1, article2)
                    else:
                        groups = groups + [[article1['id'], article2['id']]]

    return groups