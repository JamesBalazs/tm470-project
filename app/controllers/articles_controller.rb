class ArticlesController < ApplicationController
  # GET /articles or /articles.json
  def index
    @articles = Article.all
  end

  def fetch

  end

  private

  # Only allow a list of trusted parameters through.
    def article_params
      params.require(:article).permit(:title, :body, :sentiment, :RssFeed_id, :Group_id)
    end
end
