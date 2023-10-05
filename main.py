import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
from bs4 import BeautifulSoup
from collections import Counter

# Define a function to remove HTML tags from a text string
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text()
    return cleaned_text

# Define a function to remove latitude and longitude data from a list
def remove_lat_lon(data_list):
    cleaned_list = [item for item in data_list if '°' not in item]
    return cleaned_list

# Load the sasquatch dataset
squatchdata = pd.read_csv('datasets/_Bigfoot_Sightings.csv')

# Convert the 'Descr' column to a list
description = list(squatchdata['Descr'])

# Convert list to string and join with space
squatchDescriptionPlusSpace = ' '.join(str(e) for e in description)

# Remove HTML tags from squatchDescriptionPlusSpace
cleaned_data = remove_html_tags(squatchDescriptionPlusSpace)

# Remove latitude and longitude data from cleaned_data
cleaned_data = remove_lat_lon(cleaned_data.split())

# Convert text data to lowercase
cleaned_data_lower = [word.lower() for word in cleaned_data]

# Count the occurrences of each word
word_counts = Counter(cleaned_data_lower)

# Get the top 50 most common words
top_words = word_counts.most_common(100)

# Create a dictionary with the top words and their frequencies
word_freq = dict(top_words)

# Custom stopwords
custom_stopwords = set(["nan", "in", "sighting", "by", "encounter", "encounters", "near", "possible", "report", "the", "of", 'out', "let's", 'we', 'was', 'how', 'myself', 'for', 'could', 'they', "when's", 'about', "hasn't", 'then', 'both', "i'd", 'since', 'so', 'as', 'any', 'after', 'you', 'why', 'been', 'where', 'by', "isn't", 'get', 'hence', 'k', "that's", 'yourself', 'a', "haven't", 'did', "there's", "hadn't", 'www', "he'll", 'their', "they'd", 'doing', 'be', 'further', 'ours', "can't", 'am', 'her', "you'll", 'yourselves', 'that', 'my', 'what', 'to', 'not', "won't", "he's", "couldn't", 'own', 'there', 'this', 'each', "we're", 'all', "we've", 'more', 'else', 'me', "who's", "how's", 'which', 'himself', 'nor', 'other', "shouldn't", 'who', "here's", "i'm", 'same', 'at', 'such', 'up', "she'd", 'com', 'than', 'can', 'too', "you've", 'these', "wasn't", 'while', 'before', "didn't", 'he', 'i', 'ourselves', 'our', 'r', 'its', 'but', 'with', "wouldn't", 'because', 'those', 'the', 'it', 'hers', 'just', 'between', 'over', 'had', 'ever', 'does', 'have', 'and', "we'd", "mustn't", 'or', 'some', "we'll", 'only', 'when', "i've", 'like', 'also', 'below', 'in', 'if', 'theirs', "aren't", 'again', "she'll", 'his', "what's", 'whom', 'above', 'should', 'itself', 'themselves', 'until', 'are', 'she', 'no', 'from', 'into', "they'll", "where's", "they're", 'your', 'few', 'herself', "i'll", 'however', 'has', 'of', 'ought', 'down', 'were', 'once', 'having', 'them', "why's", 'under', 'him', 'do', 'on', 'an', "you'd", 'yours', 'being', 'off', 'would', 'very', 'http', 'shall', "they've", "weren't", 'through', "you're", 'most', 'against', 'cannot', "doesn't", "it's", 'otherwise', 'here', 'is', "don't", "shan't", 'therefore', "he'd", 'during', "she's", "hears", "sees", "south", "told", "describes", "area", "east", "north"])

# Exclude stopwords from the word frequency dictionary
word_freq = {word: freq for word, freq in word_freq.items() if word not in custom_stopwords}

# Create a WordCloud object
sqatchWordcloud = WordCloud(
    background_color='white',
    stopwords=STOPWORDS.union(custom_stopwords),  # Use combined stopwords
    height=600,
    width=400,
)

# Generate the word cloud from the word frequencies
sqatchWordcloud.generate_from_frequencies(word_freq)

# Save the word cloud as a PNG file
sqatchWordcloud.to_file("wordcloud.png")

# Display the word cloud
plt.imshow(sqatchWordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
