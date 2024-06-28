class AddLabelToArticle < ActiveRecord::Migration[7.1]
  def change
    add_column :articles, :label, :string
  end
end
