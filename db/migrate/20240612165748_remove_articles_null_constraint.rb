class RemoveArticlesNullConstraint < ActiveRecord::Migration[7.1]
  def up
    rename_column :articles, :groups_id, :group_id
    rename_column :articles, :rss_feeds_id, :rss_feed_id

    change_column_null :articles, :group_id, true
  end

  def down
    rename_column :articles, :group_id, :groups_id
    rename_column :articles, :rss_feed_id, :rss_feeds_id

    change_column_null :articles, :groups_id, false
  end
end
