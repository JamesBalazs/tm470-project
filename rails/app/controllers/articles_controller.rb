require 'rss'
require 'open-uri'
require 'nlp'

class ArticlesController < ApplicationController
  # GET /articles or /articles.json
  def index
    @articles = Article.all
  end

  def refresh
    Article.destroy_all
    Group.destroy_all

    Nlp.fetch_articles
    Nlp.update_sentiment
    Nlp.group_articles
  end

  private

  # Only allow a list of trusted parameters through.
    def article_params
      params.require(:article).permit(:title, :body, :sentiment, :RssFeed_id, :Group_id)
    end
end
