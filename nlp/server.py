import json
import grouping, schemas
from flask import Flask, jsonify, request
from marshmallow import ValidationError

from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

MODEL = 'KernAI/stock-news-distilbert'
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
tokenizer = AutoTokenizer.from_pretrained(MODEL)
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    request_data = request.json
    articles_schema = schemas.ArticleSchema(many=True)

    try:
        articles = articles_schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for id, article in enumerate(articles):
        text = f"#{article['title']}: #{article['body']}"

        # sanity check for now, remove later
        if articles[id]['id'] != article['id']:
            return jsonify({'error': "article id didn't match"}), 500

        result = classifier(text)[0]
        articles[id] = {
            **article,
            'sentiment': result['score'],
            'label': result['label']
        }

    return jsonify(articles)

@app.route('/group', methods=['POST'])
def group():
    request_data = request.json
    feeds_schema = schemas.FeedsSchema()
    try:
        feeds = feeds_schema.load(request_data)['feeds']
    except ValidationError as err:
        return jsonify(err.messages), 400

    feeds_with_embeddings = grouping.calculate_embeddings(feeds)
    similarities = grouping.calculate_similarities(feeds_with_embeddings)
    groups = grouping.group_by_similarity(feeds_with_embeddings, similarities)

    return jsonify(groups)
