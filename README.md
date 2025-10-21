# Sentiment-Analysis
A Machine learning project that analyzes text sentiments(positive, negative, neutral) using NLP Techniques  and python

## 🔍 Project Overview

This project collects customer reviews from Yelp (Tesla showroom page), cleans and preprocesses the text, and performs basic sentiment analysis using **TextBlob**. The goal is to understand customer sentiment (polarity and subjectivity) and provide simple visual and tabular summaries of review sentiment trends.

> **Note:** The reviews were obtained by scraping the public Yelp page for a Tesla showroom. See the *Ethics & Legal* section below.

## 📁 Repository Contents

- `Tesla_Sentiment.ipynb` — Jupyter notebook with the entire pipeline:
  - Web scraping (requests + BeautifulSoup)
  - Data cleaning (regex, stopword removal)
  - Lemmatization (TextBlob Word)
  - Sentiment extraction (TextBlob polarity & subjectivity)
  - Basic data analysis and visualizations

## 🛠️ Technologies & Libraries

- Python 3.8+
- `pandas`, `numpy`
- `requests`, `beautifulsoup4`
- `nltk`
- `textblob`
- `matplotlib`, `seaborn`
- (optional) `wordcloud` for visualizing frequent words

## 🧭 Methodology

1. **Scrape** Yelp showroom page using `requests` and parse HTML with `BeautifulSoup`.
2. **Extract** the text of each review into a pandas DataFrame.
3. **Clean** text:
   - Lowercase, remove punctuation and extra whitespace
   - Remove stopwords (NLTK)
   - Lemmatize tokens using `TextBlob.Word`
4. **Analyze sentiment** per review using `TextBlob`:
   - `polarity` (range `[-1.0, 1.0]`): negative → positive
   - `subjectivity` (range `[0.0, 1.0]`)
5. **Summarize & visualize**:
   - Distribution of polarity and subjectivity
   - Top positive/negative reviews
   - Basic statistics (counts, avg polarity)
