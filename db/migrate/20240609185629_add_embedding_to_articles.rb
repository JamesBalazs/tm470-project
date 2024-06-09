class AddEmbeddingToArticles < ActiveRecord::Migration[7.1]
  def change
    add_column :articles, :embedding, :vector
  end
end
