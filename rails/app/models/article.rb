class Article < ApplicationRecord
  belongs_to :rss_feed
  belongs_to :group, required: false

  validates_presence_of :title, :body
  validates_length_of :title, maximum: 65_536
  validates_inclusion_of :label, in: ['positive', 'negative', 'neutral'], allow_nil: true

  has_neighbors :embedding

  def pretty_sentiment
    prefix = ''
    if sentiment <= 0.3
      prefix = 'Slightly '
    elsif sentiment > 0.7
      prefix = 'Very '
    end

    prefix + label.titlecase
  end

  def emoji
    lookup = {
      'Slightly Negative' => 'emoji-astonished',
      'Slightly Neutral' => 'emoji-neutral',
      'Slightly Positive' => 'emoji-smile',
      'Negative' => 'emoji-frown',
      'Neutral' => 'emoji-neutral',
      'Positive' => 'emoji-sunglasses',
      'Very Negative' => 'emoji-angry',
      'Very Neutral' => 'emoji-neutral',
      'Very Positive' => 'emoji-laughing',
    }

    lookup[pretty_sentiment]
  end
end
