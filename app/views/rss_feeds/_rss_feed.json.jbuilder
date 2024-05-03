json.extract! rss_feed, :id, :title, :url, :created_at, :updated_at
json.url rss_feed_url(rss_feed, format: :json)
