import pandas as pd

# load dataset once
destinations = pd.read_csv("data/CLEAN_Destinations.csv")


def get_instagram_links(place):
    hashtag = place.replace(" ", "").lower()
    return f"https://www.instagram.com/explore/tags/{hashtag}/"


def get_youtube_videos(place):
    query = place.replace(" ", "+") + "+travel"
    return f"https://www.youtube.com/results?search_query={query}"


def get_youtube_shorts(place):
    query = place.replace(" ", "+") + "+travel+shorts"
    return f"https://www.youtube.com/results?search_query={query}&sp=EgIYAQ%253D%253D"


# ================================
# RAG CHATBOT
# ================================
def rag_chatbot(query):

    place = query.strip().lower()

    match = destinations[
        destinations["destination"].str.lower() == place
    ]

    if match.empty:
        return f"Sorry, {query} is not present in the tourism dataset."

    row = match.iloc[0]

    destination = row["destination"]
    state = row["state"]

    # Nearby places in same state
    nearby = destinations[
        (destinations["state"] == state) &
        (destinations["destination"] != destination)
    ].head(4)

    nearby_list = ""

    for _, r in nearby.iterrows():

        place_name = r["destination"]

        map_link = f"https://www.google.com/maps/search/{place_name.replace(' ','+')}+near+{destination.replace(' ','+')}"

        nearby_list += f"""
• {place_name}  
<a href="{map_link}" target="_blank">Check Distance</a><br>
"""

    ticket_link = f"https://www.google.com/search?q={destination.replace(' ','+')}+entry+ticket"

    response = f"""
<h3>🧭 Travel Guide for {destination}</h3>

📍 <b>Nearby Attractions</b><br>
{nearby_list}

<br>

🚆 <b>How to Reach</b><br>
• Nearest airport in {state}<br>
• Railway stations connect major cities<br>
• Easily reachable by road and taxis<br>

<br>

🎟 <b>Entry Ticket Information</b><br>
<a href="{ticket_link}" target="_blank">Check Latest Ticket Prices</a>

<br><br>

📸 <b>Best Photo Spots</b><br>
• Main entrance viewpoint<br>
• Scenic garden areas<br>
• Sunset viewpoints nearby<br>

<br>

🍛 <b>Local Food to Try</b><br>
• Regional street food<br>
• Traditional sweets<br>
• Local restaurant specialties<br>

<br>

💡 <b>Travel Tips</b><br>
• Visit early morning to avoid crowds<br>
• Carry water and comfortable shoes<br>
• Weekdays are less crowded
"""

    return response


# ================================
# SIMPLE AI RESPONSE (for multilingual pipeline)
# ================================
def generate_ai_response(query):

    place = query.strip().lower()

    match = destinations[
        destinations["destination"].str.lower() == place
    ]

    if match.empty:
        return f"Sorry, {query} is not present in the tourism dataset."

    row = match.iloc[0]

    destination = row["destination"]
    state = row["state"]

    return f"Top tourist destination: {destination} located in {state}. It is a popular travel spot with scenic views and local attractions."


# ================================
# SOCIAL MEDIA PROMOTION
# ================================
def generate_promo_links(place):

    insta = get_instagram_links(place)
    yt_videos = get_youtube_videos(place)
    yt_shorts = get_youtube_shorts(place)

    return f"""
<h3>📱 Social Media Content for {place}</h3>

📸 <b>Instagram Travel Posts</b><br>
<a href="{insta}" target="_blank">View Instagram Posts</a>

<br><br>

▶️ <b>YouTube Travel Videos</b><br>
<a href="{yt_videos}" target="_blank">Watch YouTube Videos</a>

<br><br>

🎬 <b>YouTube Shorts</b><br>
<a href="{yt_shorts}" target="_blank">Watch YouTube Shorts</a>
"""