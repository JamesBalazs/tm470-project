class RssFeed < ApplicationRecord
  validates_presence_of :title, :url
  validates_length_of :title, maximum: 32

  has_many :articles
end
