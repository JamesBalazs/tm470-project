import json, sys, os

input = sys.stdin.read()
articles = json.loads(input)

data = json.dumps({
    'groups': [
        [ article['id'] for article in articles ]
    ]
})

print(data)
sys.exit(7)