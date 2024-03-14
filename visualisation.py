import matplotlib.pyplot as plt

def plot_sentiment(sentiment):
    labels = ['Positive', 'Neutral', 'Negative']
    values = [sentiment['pos'], sentiment['neu'], sentiment['neg']]
    colors = ['green', 'gray', 'red']

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=colors)
    plt.xlabel('Sentiment')
    plt.ylabel('Probability')
    plt.title('Sentiment Analysis of Survey Responses')
    plt.ylim(0, 1)
    plt.show()

# Example usage
sample_sentiment = {'pos': 0.5, 'neu': 0.3, 'neg': 0.2}
plot_sentiment(sample_sentiment)
