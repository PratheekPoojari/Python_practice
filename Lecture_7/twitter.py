import re

url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "") # Simple find and replace
# username = url.removeprefix("https://twitter.com/") # Removes anything before the specified phrase.
# print(f"Username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) # re.sub(pattern, repl, string, count = 0, flags = 0)
# print(f"Username: {username}")

#if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#    print(f"Username: ", matches.group(2))

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([\w]+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))

# re.split(pattern, string, maxsplit = 0, flags = 0) # Splits the string at the specific pattern
# re.findall(pattern, string, flags = 0) # Finds all the copies of the pattern
