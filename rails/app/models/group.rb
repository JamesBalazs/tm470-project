class Group < ApplicationRecord
  has_many :articles, -> { order('rss_feed_id ASC') }
end
