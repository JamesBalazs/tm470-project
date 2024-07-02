module Nlp

  def self.fetch_articles
    items = []

    RssFeed.all.each do |feed|
      URI.open(feed.url) do |rss|
        parser = RSS::Parser.parse(rss)
        items = parser.items.map { |item| { title: item.title, link: item.link, body: item.description, rss_feed_id: feed.id } }
      end

      Article.create!(items)
    end
  end

  def self.update_sentiment
    to_update = Article.select(:id, :rss_feed_id, :title, :body)

    response = HTTParty.post(URI::HTTP.build(host: 'nlp', path: '/sentiment', port: 5000), body: to_update.to_json, headers: { 'Content-Type' => 'application/json' })

    Article.upsert_all(response.parsed_response)
  end

  def self.group_articles
    feeds = {}

    RssFeed.all.each do |feed|
      articles = {}

      feed.articles.select(:id, :rss_feed_id, :title, :body).each do |article|
        articles[article.id] = article
      end

      feeds[feed.id] = { articles: articles }
    end

    response = HTTParty.post(URI::HTTP.build(host: 'nlp', path: '/group', port: 5000), body: { feeds: feeds }.to_json, headers: { 'Content-Type' => 'application/json' })
    groups = response.parsed_response

    groups.each do |article_ids|
      articles = Article.where(id: article_ids)
      group = Group.create!() # TODO needs a title
      articles.update_all(group_id: group.id)
    end
  end

end