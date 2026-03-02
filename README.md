# TV Background Analyzer

An interactive web application that analyzes 250+ top-rated TV shows to identify the best content for background viewing while working or studying.

🔗 **Live Demo:** [https://nikhil-thamma-tv-background-analyzer.streamlit.app/](https://nikhil-thamma-tv-background-analyzer.streamlit.app/)

## Overview

This project uses data science and natural language processing to score TV shows based on their "background-ability" - how suitable they are for playing in the background while doing other tasks. The analysis considers multiple factors including genre, plot complexity, episodic structure, cultural familiarity, and community sentiment.

## Features

- **Multi-dimensional Analysis:** Evaluates 250 shows across 5 scoring dimensions
- **Interactive Filtering:** Filter by genre, score range, number of seasons, and data availability
- **Data Visualizations:** Score distributions, scatter plots, heatmaps, and genre breakdowns
- **Individual Show Analysis:** Detailed component score breakdowns with radar charts
- **Exportable Results:** Download filtered datasets as CSV

## Scoring Methodology

The background-ability score (0-100) is calculated using weighted components:

- **Genre Score (30%)** - Sitcoms and family shows rank higher than thrillers and dramas
- **Description Score (25%)** - Analyzes plot descriptions for complexity indicators
- **Episodic Score (20%)** - Episodic shows (20+ episodes/season) score higher than serialized content
- **Popularity Score (15%)** - Cultural familiarity proxy for easier casual viewing
- **Reddit Sentiment (10%)** - Community discussion analysis for background/comfort mentions

## Tech Stack

- **Python** - Data collection, processing, and analysis
- **Streamlit** - Interactive web dashboard
- **Plotly** - Data visualizations
- **TMDb API** - Show metadata, ratings, and popularity data
- **Reddit API** - Community sentiment and discussion analysis
- **Pandas & NumPy** - Data manipulation and analysis

## Data Pipeline

1. **Data Collection**
   - Fetched metadata for 250 shows via TMDb API
   - Scraped Reddit discussions from r/television and show-specific subreddits
   
2. **Feature Engineering**
   - Calculated genre weights based on background suitability
   - Analyzed description complexity using NLP keyword detection
   - Computed episodic scores from episodes-per-season ratios
   - Normalized popularity metrics
   
3. **Sentiment Analysis**
   - Keyword extraction from Reddit posts and comments
   - Positive/negative sentiment scoring for background-watching indicators
   
4. **Score Aggregation**
   - Weighted combination of all components
   - Normalization to 0-100 scale

## Key Insights

- **Top Background Shows:** The Office (93.5), Frasier (92.9), Friends (91.5)
- **Least Suitable:** True Detective (25.5), Dexter: Resurrection (25.5), The Queen's Gambit (26.5)
- **Comedy dominates:** Shows in the Comedy genre average 72.3/100 background score
- **Serialization matters:** Shows with 20+ episodes/season score 15-20 points higher on average

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/nikhilthamma00/tv-background-analyzer.git

# Install dependencies
pip install -r requirements.txt

# Run the dashboard locally
streamlit run dashboard.py
```

## Project Structure
```
tv-background-analyzer/
├── dashboard.py                          # Streamlit web application
├── requirements.txt                      # Python dependencies
├── data/
│   └── processed/
│       └── final_scores_all_shows.csv   # Processed dataset with scores
└── README.md
```

## Future Enhancements

- [ ] Expand dataset to 500+ shows
- [ ] Add subtitle analysis for dialogue density metrics
- [ ] Incorporate IMDb episode rating variance
- [ ] User personalization based on preferences
- [ ] Recommendation engine for similar background-friendly shows

## Author

**Nikhil Thamma**  
Data Scientist & Analyst  
[Portfolio](https://nikhilthamma.replit.app/) | [GitHub](https://github.com/nikhilthamma00) | [LinkedIn](https://www.linkedin.com/in/nikhilthamma/)

## License

This project is open source and available under the MIT License.
