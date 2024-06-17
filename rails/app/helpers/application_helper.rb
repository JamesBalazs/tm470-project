module ApplicationHelper

  def navbar_link_class(active)
    return 'nav-link active' if active

    'nav-link'
  end

end
