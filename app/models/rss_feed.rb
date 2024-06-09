class RssFeed < ApplicationRecord
  validates_presence_of :title, :url
  validates_length_of :title, maximum: 32
end
bundle exec rails g scaffold Article title:string body:text sentiment:float