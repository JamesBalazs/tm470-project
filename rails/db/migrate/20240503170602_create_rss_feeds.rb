class CreateRssFeeds < ActiveRecord::Migration[7.1]
  def change
    create_table :rss_feeds do |t|
      t.string :title, null: false
      t.string :url, null: false

      t.timestamps
    end
  end
end
