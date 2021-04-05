import urllib.parse
import json
import http.client
message = 'Hi'

conn = http.client.HTTPSConnection("8ball.delegator.com")
question = urllib.parse.quote(message)
conn.request('GET', '/magic/JSON/' + question)
response = conn.getresponse()
result = json.loads(response.read())
answer = result['magic']['answer']
print(result,answer)