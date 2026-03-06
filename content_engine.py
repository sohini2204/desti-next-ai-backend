import pandas as pd

# Load dataset
destinations = pd.read_csv("data/CLEAN_Destinations.csv")


def generate_travel_story(destination):

    place = destinations[
        destinations["destination"].str.lower() == destination.lower()
    ]

    if not place.empty:

        row = place.iloc[0]

        state = row["state"]
        category = row["category"]
        rating = row["rating"]
        best_season = row["best_season"]
        days = row["days"]

        return f"""
A journey to {destination}, located in {state}, offers travelers an unforgettable experience.

This destination is famous for its {category} attractions and has received a rating of {rating}.

Visitors usually spend around {days} days exploring the beauty of {destination}.

The best time to visit {destination} is during the {best_season}.
"""

    return f"{destination} not found in dataset."


def generate_promotional_content(destination):
    return generate_social_media_posts(destination)


def generate_social_media_posts(destination):

    hashtag = destination.replace(" ", "").lower()
    query = destination.replace(" ", "+")

    insta = f"https://www.instagram.com/explore/tags/{hashtag}/"
    yt_videos = f"https://www.youtube.com/results?search_query={query}+travel"
    yt_shorts = f"https://www.youtube.com/results?search_query={query}+travel+shorts&sp=EgIYAQ%253D%253D"

    return f"""
<h3>📱 Social Media Content for {destination}</h3>

📸 Instagram Travel Posts  
<a href="{insta}" target="_blank">View Instagram Posts</a>

<br><br>

▶️ YouTube Travel Videos  
<a href="{yt_videos}" target="_blank">Watch YouTube Videos</a>

<br><br>

🎬 YouTube Shorts  
<a href="{yt_shorts}" target="_blank">Watch YouTube Shorts</a>
"""



def generate_reviews(destination):

    query = destination.replace(" ", "+")

    google_reviews = f"https://www.google.com/search?q={query}+reviews"
    google_maps = f"https://www.google.com/maps/search/{query}"

    return f"""
<h3>⭐ Reviews for {destination.title()}</h3>

You can explore authentic traveler reviews using the links below.

<br><br>

📝 <b>Google Reviews</b><br>
<a href="{google_reviews}" target="_blank">Read Reviews on Google</a>

<br><br>

📍 <b>Google Maps Reviews</b><br>
<a href="{google_maps}" target="_blank">View Reviews on Google Maps</a>
"""