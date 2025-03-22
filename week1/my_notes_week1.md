# Week 1 Notes
```bash
curl -X 'POST'  'http://localhost:11434/api/chat'  \
-H 'accept: application/json'  \
-H 'Content-Type: application/json'  \
-d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "Briefly tell me about Pakistan major issues in 3 sentences as markdown"
    }
  ],
  "stream": false
}'|jq
```