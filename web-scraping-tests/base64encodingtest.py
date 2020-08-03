import base64
user = 'sjanardhan'
pw = 'Krisna3227'
joined = f"{user}:{pw}"
print(joined)

encoded = base64.b64encode(bytes(joined, 'utf-8'), altchars=None)
basic_auth_key = f"Basic {encoded.decode('utf-8')}"


print(basic_auth_key)