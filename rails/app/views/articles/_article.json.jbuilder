json.extract! article, :id, :title, :body, :sentiment, :RssFeed_id, :Group_id, :created_at, :updated_at
json.url article_url(article, format: :json)
