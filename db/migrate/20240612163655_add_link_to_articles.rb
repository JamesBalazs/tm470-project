class AddLinkToArticles < ActiveRecord::Migration[7.1]
  def change
    add_column :articles, :link, :string
  end
end
