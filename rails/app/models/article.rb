class Article < ApplicationRecord
  belongs_to :rss_feed
  belongs_to :group, required: false

  validates_presence_of :title, :body
  validates_length_of :title, maximum: 65_536
  validates_inclusion_of :label, in: ['positive', 'negative', 'neutral'], allow_nil: true

  has_neighbors :embedding
end
