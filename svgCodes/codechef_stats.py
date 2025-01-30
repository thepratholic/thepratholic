import requests
from bs4 import BeautifulSoup
import json

# Replace with your CodeChef username
CODECHEF_USERNAME = "the_pratholic"

# URL of CodeChef profile
URL = f"https://www.codechef.com/users/{CODECHEF_USERNAME}"

# Fetch profile data
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract rating and global rank
rating = soup.find("div", class_="rating-number").text.strip()
global_rank = soup.find("a", class_="rating-ranks").text.strip()

# Extract solved problems
solved_problems = soup.find("section", class_="rating-data-section problems-solved").text.strip().split("\n")[1]

# Generate SVG File
svg_template = f"""<svg width="500" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="#1E1E1E" rx="15"/>
    <text x="50%" y="40" fill="white" font-size="22" text-anchor="middle" font-family="Arial">🍽️ CodeChef Stats</text>
    <text x="50%" y="80" fill="white" font-size="18" text-anchor="middle" font-family="Arial">Rating: {rating}</text>
    <text x="50%" y="110" fill="white" font-size="18" text-anchor="middle" font-family="Arial">Global Rank: {global_rank}</text>
    <text x="50%" y="140" fill="white" font-size="18" text-anchor="middle" font-family="Arial">Problems Solved: {solved_problems}</text>
</svg>"""

# Save to file
with open("codechef_stats.svg", "w") as file:
    file.write(svg_template)

print("✅ CodeChef stats SVG generated successfully!")