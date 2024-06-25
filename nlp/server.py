import json
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

MODEL = 'KernAI/stock-news-distilbert'
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
tokenizer = AutoTokenizer.from_pretrained(MODEL)
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

app = Flask(__name__)

class ArticleSchema(Schema):
    id = fields.Integer(required=True)
    rss_feed_id = fields.Integer(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)

class ArticlesByFeedSchema(Schema):
    id = fields.Integer(required=True)
    articles = fields.Nested(ArticleSchema, many=True)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    request_data = request.json
    articles_by_feed_schema = ArticlesByFeedSchema(many=True)
    try:
        articles_by_feed = articles_by_feed_schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for feed, articles in articles_by_feed.items():
        for i, article in enumerate(articles):
            text = f"#{article['title']}: #{article['body']}"

            # merge article with label, score from classifier
            articles_by_feed[feed][i] = { **articles_by_feed[feed][i], **(classifier(text)[0]) }

    print(json.dumps(articles_by_feed, indent=2))

    return jsonify(articles_by_feed)
