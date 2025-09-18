import re

text = "Attack from 185.33.22.11"
text2 = "Contact..abdalrahman@mail.com, mahdi@gmail.com"
secret = "this is the secret APIKEY=5d41402abc4b2a7x6b9719d911017c592 go"
url = "Visit https://evil.com/login"
card = "Possible CC numbers : 4111111111111111 or 5500000000000004"
text_s = "MD5=5d41402abc4b2a76b9719d911017c592 " \
        "SHA1=aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"

date = "Logins on 2025-09-16 and 2025/09/15"

result = re.findall(r'\d+', text)
result_email = re.findall(r"\w+@\w+\.\w+", text2)
base_search = re.findall(r"[^a-z0-9]{32}", secret)
find_url = re.findall(r"https?://\S+", url)
find_words = re.findall(r"\w+\s", secret)
find_card = re.findall(r'\b\d{16}\b', card)
find_sha = re.findall(r'[a-f0-9]{32}', text_s)


print(base_search)