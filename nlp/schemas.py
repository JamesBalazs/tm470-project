from marshmallow import Schema, fields

class ArticleSchema(Schema):
    id = fields.Integer(required=True)
    rss_feed_id = fields.Integer(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)

class ArticlesByFeedSchema(Schema):
    id = fields.Integer(required=True)
    articles = fields.Nested(ArticleSchema, many=True)

class ArticlesSchema(Schema):
    articles = fields.Dict(keys=fields.String, values=fields.Nested(ArticleSchema()))

class FeedsSchema(Schema):
    feeds = fields.Dict(keys=fields.String, values=fields.Nested(ArticlesSchema()))