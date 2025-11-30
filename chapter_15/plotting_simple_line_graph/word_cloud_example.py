from wordcloud import WordCloud
from pathlib import Path
import matplotlib.pyplot as plt

# Your text data
text = Path("TimFarleyCV3.txt").read_text()


# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated image:
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off the axis
plt.title("Resume Word Cloud")
plt.savefig("resume_word_cloud.png")
plt.show()