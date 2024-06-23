# https://docs.ruby-lang.org/en/2.0.0/Open3.html
require 'open3'
require 'json'

stdout_stderr, status = Open3.capture2e('python 8b-ruby-python-interop.py', stdin_data: [
  {id: 123, text: 'some article'},
  {id: 456, text: 'some other article'},
].to_json)

print("output: #{stdout_stderr}")
print("status: #{status}")