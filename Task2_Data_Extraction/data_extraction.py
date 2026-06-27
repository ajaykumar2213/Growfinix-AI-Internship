import re
import json

text = """
Customer Name: John Doe
Travel Date: 25 July 2026
Destination: Chennai
"""

data = {
    "name": re.search(r"Customer Name:\s*(.*)", text).group(1),
    "date": re.search(r"Travel Date:\s*(.*)", text).group(1),
    "destination": re.search(r"Destination:\s*(.*)", text).group(1)
}

print(json.dumps(data, indent=4))
