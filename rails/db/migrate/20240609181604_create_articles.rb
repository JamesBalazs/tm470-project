class CreateArticles < ActiveRecord::Migration[7.1]
  def change
    create_table :articles do |t|
      t.string :title
      t.text :body
      t.float :sentiment
      t.references :rss_feeds, null: false, foreign_key: true
      t.references :groups, null: false, foreign_key: true

      t.timestamps
    end
  end
end
