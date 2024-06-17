# Pin npm packages by running ./bin/importmap

pin "application"
pin "@hotwired/turbo-rails", to: "turbo.min.js"
pin "bootstrap", to: 'bootstrap.min.js', preload: true # @5.3.3
pin "popper", to: 'popper.js', preload: true # @2.11.8
