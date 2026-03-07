# Fileorger

---

manage your files and folders and search them all automatically with AI

- Send request to `terminal`

```bash
curl -X POST http://localhost:8122/terminal \
  -H "Content-Type: application/json" \
  -d '{"query":"what is the content of the file test.txt"}'
```

- Send request to `suggest-folders`

```bash
curl -X POST http://localhost:8122/suggest-folders \
  -H "Content-Type: application/json" \
  -d '{"path": "/Users/harshith/Downloads"}'
```
