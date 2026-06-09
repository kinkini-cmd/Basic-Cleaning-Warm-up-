import re

text = "Breaking News!!! Sri Lanka wins the match @2026 https://news.com"
print("Orginal Text:",text)
print()

# Lowercase
text = text.lower()

# Remove url
text = re.sub(r"http\S+","",text)

# Remove special characters and numbers
text = re.sub(r"[^a-zA-Z\s]","",text)

# Remove extra sppaces
text = re.sub(r"\s+","",text).strip()

print("Cleaned Text:",text)
