require 'rss'
require 'open-uri'

class ArticlesController < ApplicationController
  # GET /articles or /articles.json
  def index
    @articles = Article.all
  end

  def fetch
    items = []

    RssFeed.all.each do |feed|
      URI.open(feed.url) do |rss|
        parser = RSS::Parser.parse(rss)
        items = parser.items.map { |item| { title: item.title, link: item.link, body: item.description, rss_feed_id: feed.id } }
      end
    end

    Article.create!(items)
  end

  def update_sentiment
    to_update = Article.select(:id, :rss_feed_id, :title, :body)

    response = HTTParty.post(URI::HTTP.build(host: 'nlp', path: '/sentiment', port: 5000), body: to_update.to_json, headers: { 'Content-Type' => 'application/json' })

    Article.upsert_all(response.parsed_response)
  end

  def group
    to_update = Article.select(:id, :rss_feed_id, :title, :body).group_by{ |article| article.rss_feed_id }
    to_update = to_update.map{ |id, articles| { id: id, articles: articles } }

    response = HTTParty.post(URI::HTTP.build(host: 'nlp', path: '/sentiment', port: 5000), body: to_update.to_json, headers: { 'Content-Type' => 'application/json' })
    processed_articles = response.parsed_response
    Article.update_all(processed_articles.articles)
  end

  private

  # Only allow a list of trusted parameters through.
    def article_params
      params.require(:article).permit(:title, :body, :sentiment, :RssFeed_id, :Group_id)
    end
end
