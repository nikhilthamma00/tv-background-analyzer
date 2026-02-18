import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import ast

# Page config
st.set_page_config(
    page_title="TV Background Analyzer",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS matching your portfolio's color scheme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .main {
        background-color: #f8f8f8;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e5e5;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2 {
        color: #610099;
        font-weight: 600;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 1.5rem;
    }
    
    /* Header styling */
    h1 {
        color: #333333;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #333333;
        font-weight: 600;
        font-size: 1.8rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #333333;
        font-weight: 600;
        font-size: 1.3rem;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    
    /* Subtitle text */
    .subtitle {
        color: #666666;
        font-size: 1.1rem;
        font-weight: 400;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Metrics styling */
    [data-testid="stMetricValue"] {
        color: #610099;
        font-weight: 600;
    }
    
    [data-testid="stMetricLabel"] {
        color: #666666;
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 0.5px;
    }
    
    /* Card-like containers */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: transparent;
        border-bottom: 1px solid #e5e5e5;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: none;
        color: #666666;
        font-weight: 500;
        padding: 1rem 0;
        font-size: 1rem;
    }
    
    .stTabs [aria-selected="true"] {
        color: #610099;
        border-bottom: 2px solid #610099;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #432656 0%, #640c9c 100%);
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.85rem;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #542d6b 0%, #7a10bd 100%);
        box-shadow: 0 4px 12px rgba(97, 0, 153, 0.3);
        transform: translateY(-1px);
    }
    
    /* Download button */
    .stDownloadButton button {
        background-color: #ffffff;
        color: #610099;
        border: 2px solid #610099;
        border-radius: 6px;
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton button:hover {
        background: linear-gradient(135deg, #432656 0%, #640c9c 100%);
        color: #ffffff;
        transform: translateY(-1px);
    }
    
    /* Selectbox and multiselect */
    .stSelectbox, .stMultiSelect {
        background-color: #ffffff;
    }
    
    /* Slider */
    .stSlider [data-baseweb="slider"] {
        background-color: #e5e5e5;
    }
    
    .stSlider [data-testid="stThumbValue"] {
        color: #610099;
        font-weight: 600;
    }
    
    /* Radio buttons */
    .stRadio [role="radiogroup"] label {
        color: #333333;
        font-weight: 400;
    }
    
    /* Dataframe */
    [data-testid="stDataFrame"] {
        border: 1px solid #e5e5e5;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #666666;
        font-size: 0.85rem;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #e5e5e5;
    }
    
    /* Info box */
    .info-box {
        background-color: #f5f0ff;
        border-left: 3px solid #610099;
        padding: 1rem 1.5rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .info-box p {
        color: #333333;
        margin: 0;
    }
    
    /* Purple accent text */
    .accent-text {
        color: #610099;
        font-weight: 600;
    }
    
    /* Label text */
    label {
        color: #333333 !important;
    }
    
    /* Sidebar text color fix */
    [data-testid="stSidebar"] label {
        color: #333333 !important;
    }
    
    [data-testid="stSidebar"] p {
        color: #666666;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/final_scores_all_shows.csv')
    df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
    return df

df = load_data()

# Header
st.markdown("<h1>TV Background Analyzer</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="subtitle">
Discover the perfect TV show to play in the background while working. 
Our algorithm analyzes 250 top-rated shows across multiple dimensions including genre, 
plot complexity, episodic structure, and cultural familiarity.
</div>
""", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.markdown("<h2>Filters</h2>", unsafe_allow_html=True)

# Score range filter
score_range = st.sidebar.slider(
    "Background Score Range",
    min_value=0,
    max_value=100,
    value=(0, 100),
    help="Filter shows by their background-ability score (0-100)"
)

# Genre filter
all_genres = sorted(list(set([g for genres in df['genres'] for g in genres])))
selected_genres = st.sidebar.multiselect(
    "Genres",
    options=all_genres,
    default=[],
    help="Filter by genre (leave empty for all)"
)

# Season count filter
season_range = st.sidebar.slider(
    "Number of Seasons",
    min_value=int(df['num_seasons'].min()),
    max_value=int(df['num_seasons'].max()),
    value=(int(df['num_seasons'].min()), int(df['num_seasons'].max()))
)

# Has Reddit data filter
reddit_filter = st.sidebar.radio(
    "Reddit Data Availability",
    options=["All Shows", "With Reddit Data", "Without Reddit Data"],
    index=0
)

# Apply filters
filtered_df = df[
    (df['background_score_100'] >= score_range[0]) &
    (df['background_score_100'] <= score_range[1]) &
    (df['num_seasons'] >= season_range[0]) &
    (df['num_seasons'] <= season_range[1])
]

# Genre filter
if selected_genres:
    filtered_df = filtered_df[filtered_df['genres'].apply(
        lambda x: any(genre in x for genre in selected_genres)
    )]

# Reddit data filter
if reddit_filter == "With Reddit Data":
    filtered_df = filtered_df[filtered_df['has_reddit_data'] == True]
elif reddit_filter == "Without Reddit Data":
    filtered_df = filtered_df[filtered_df['has_reddit_data'] == False]

# Results summary in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Results:** {len(filtered_df)} shows")

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs(["Rankings", "Visualizations", "Show Details", "Methodology"])

# Tab 1: Rankings
with tab1:
    st.markdown("<h2>Show Rankings</h2>", unsafe_allow_html=True)
    
    # Sort options
    col1, col2, col3 = st.columns([2, 1, 3])
    with col1:
        sort_by = st.selectbox(
            "Sort by",
            options=['background_score_100', 'vote_average', 'popularity', 'num_seasons', 'num_episodes'],
            format_func=lambda x: {
                'background_score_100': 'Background Score',
                'vote_average': 'IMDb Rating',
                'popularity': 'Popularity',
                'num_seasons': 'Number of Seasons',
                'num_episodes': 'Number of Episodes'
            }[x],
            label_visibility="collapsed"
        )
    with col2:
        sort_order = st.selectbox("Order", options=['Descending', 'Ascending'], label_visibility="collapsed")
    
    # Sort dataframe
    sorted_df = filtered_df.sort_values(
        sort_by, 
        ascending=(sort_order == 'Ascending')
    )
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Shows", len(sorted_df))
    with col2:
        st.metric("Average Score", f"{sorted_df['background_score_100'].mean():.1f}")
    with col3:
        st.metric("Highest Rated", f"{sorted_df['vote_average'].max():.1f}/10")
    with col4:
        st.metric("Total Episodes", f"{sorted_df['num_episodes'].sum():,}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display table
    display_df = sorted_df[[
        'name', 'background_score_100', 'vote_average', 'num_seasons', 
        'num_episodes', 'genres'
    ]].copy()
    
    # Rename columns for display
    display_df.columns = [
        'Show', 'Background Score', 'IMDb Rating', 'Seasons', 
        'Episodes', 'Genres'
    ]
    
    # Format scores
    display_df['Background Score'] = display_df['Background Score'].round(1)
    display_df['Genres'] = display_df['Genres'].apply(lambda x: ', '.join(x[:3]))
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=600,
        hide_index=True
    )
    
    # Download button
    st.markdown("<br>", unsafe_allow_html=True)
    csv = sorted_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="tv_background_scores.csv",
        mime="text/csv"
    )

# Tab 2: Visualizations
with tab2:
    st.markdown("<h2>Data Visualizations</h2>", unsafe_allow_html=True)
    
    # Visualization 1: Score distribution
    st.markdown("<h3>Background Score Distribution</h3>", unsafe_allow_html=True)
    fig_hist = px.histogram(
        filtered_df,
        x='background_score_100',
        nbins=30,
        labels={'background_score_100': 'Background Score'},
        color_discrete_sequence=['#610099']
    )
    fig_hist.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Background Score",
        yaxis_title="Number of Shows",
        showlegend=False,
        font=dict(family="Inter, sans-serif", color="#333333"),
        xaxis=dict(gridcolor='#e5e5e5'),
        yaxis=dict(gridcolor='#e5e5e5'),
        margin=dict(t=20, b=0)
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Visualization 2: Scatter plot
    st.markdown("<h3>Background Score vs IMDb Rating</h3>", unsafe_allow_html=True)
    fig_scatter = px.scatter(
        filtered_df,
        x='vote_average',
        y='background_score_100',
        hover_data=['name', 'num_seasons'],
        labels={
            'vote_average': 'IMDb Rating',
            'background_score_100': 'Background Score',
            'name': 'Show'
        },
        color='genre_score',
        color_continuous_scale=['#e5e5e5', '#432656', '#640c9c'],
        size='popularity',
        size_max=15
    )
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="IMDb Rating",
        yaxis_title="Background Score",
        font=dict(family="Inter, sans-serif", color="#333333"),
        xaxis=dict(gridcolor='#e5e5e5'),
        yaxis=dict(gridcolor='#e5e5e5'),
        coloraxis_colorbar=dict(title="Genre Score"),
        margin=dict(t=20, b=0)
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
# Visualization 3: Component scores heatmap for top shows
    st.markdown("<h3>Top 20 Shows - Component Analysis</h3>", unsafe_allow_html=True)
    top_20 = filtered_df.nlargest(20, 'background_score_100')
    
    heatmap_data = top_20[['name', 'genre_score', 'description_score', 
                            'episodic_score', 'popularity_score', 'reddit_score_normalized']].copy()
    heatmap_data.columns = ['Show', 'Genre', 'Description', 'Episodic', 'Popularity', 'Reddit']
    heatmap_data = heatmap_data.set_index('Show')
    
    # Create discrete color scale with balanced steps
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=heatmap_data.values.T,
        x=heatmap_data.index,
        y=heatmap_data.columns,
        colorscale=[
            [0.0, '#f5f5f5'],    # 0.0-0.2: Very low - lightest gray
            [0.2, '#d9d9d9'],    # 0.2-0.4: Low - light gray
            [0.4, '#c9b3e0'],    # 0.4-0.6: Medium - light purple
            [0.6, '#a580cc'],    # 0.6-0.8: Medium-high - medium purple
            [0.8, '#7a3db8'],    # 0.8-1.0: High - darker purple
            [1.0, '#610099']     # 1.0: Highest - your accent purple
        ],
        zmid=0.5,
        colorbar=dict(
            title="Score",
            tickmode='array',
            tickvals=[0.1, 0.3, 0.5, 0.7, 0.9],
            ticktext=['0.0-0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8-1.0'],
            tickfont=dict(color="#333333")
        )
    ))
    
    # Update text color based on background - white for darker, dark for lighter
    annotations = []
    for i, row in enumerate(heatmap_data.values.T):
        for j, value in enumerate(row):
            text_color = '#ffffff' if value > 0.6 else '#333333'
            annotations.append(
                dict(
                    x=heatmap_data.index[j],
                    y=heatmap_data.columns[i],
                    text=f'{value:.2f}',
                    showarrow=False,
                    font=dict(color=text_color, size=10, family="Inter, sans-serif")
                )
            )
    
    fig_heatmap.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="",
        yaxis_title="",
        font=dict(family="Inter, sans-serif", color="#333333"),
        height=400,
        margin=dict(t=20, b=0),
        annotations=annotations
    )
    
    st.plotly_chart(fig_heatmap, use_container_width=True)
    # Visualization 4: Genre breakdown
    st.markdown("<h3>Average Background Score by Genre</h3>", unsafe_allow_html=True)
    
    genre_scores = []
    for genre in all_genres:
        genre_df = df[df['genres'].apply(lambda x: genre in x)]
        if len(genre_df) > 0:
            genre_scores.append({
                'Genre': genre,
                'Avg Score': genre_df['background_score_100'].mean(),
                'Count': len(genre_df)
            })
    
    genre_df_plot = pd.DataFrame(genre_scores).sort_values('Avg Score', ascending=False)
    
    fig_genre = px.bar(
        genre_df_plot,
        x='Genre',
        y='Avg Score',
        hover_data=['Count'],
        labels={'Avg Score': 'Average Background Score'},
        color='Avg Score',
        color_continuous_scale=[[0, '#e5e5e5'], [0.5, '#8e52c7'], [1, '#610099']]
    )
    fig_genre.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Genre",
        yaxis_title="Average Background Score",
        xaxis_tickangle=-45,
        font=dict(family="Inter, sans-serif", color="#333333"),
        xaxis=dict(gridcolor='#e5e5e5'),
        yaxis=dict(gridcolor='#e5e5e5'),
        showlegend=False,
        margin=dict(t=20, b=0)
    )
    st.plotly_chart(fig_genre, use_container_width=True)

# Tab 3: Show Details
with tab3:
    st.markdown("<h2>Individual Show Analysis</h2>", unsafe_allow_html=True)
    
    selected_show = st.selectbox(
        "Select a show to analyze",
        options=sorted(df['name'].unique()),
        label_visibility="collapsed"
    )
    
    show_data = df[df['name'] == selected_show].iloc[0]
    
    st.markdown(f"<h3>{selected_show}</h3>", unsafe_allow_html=True)
    
    # Display show info
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Background Score", f"{show_data['background_score_100']:.1f}")
    with col2:
        st.metric("IMDb Rating", f"{show_data['vote_average']:.1f}/10")
    with col3:
        st.metric("Seasons", int(show_data['num_seasons']))
    with col4:
        st.metric("Episodes", int(show_data['num_episodes']))
    with col5:
        reddit_status = "Available" if show_data['has_reddit_data'] else "N/A"
        st.metric("Reddit Data", reddit_status)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Show overview
    st.markdown("<h3>Overview</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #666666; line-height: 1.6;'>{show_data['overview']}</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Two columns: radar chart and details
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<h3>Component Scores</h3>", unsafe_allow_html=True)
        
        categories = ['Genre', 'Description', 'Episodic', 'Popularity', 'Reddit']
        values = [
            show_data['genre_score'],
            show_data['description_score'],
            show_data['episodic_score'],
            show_data['popularity_score'],
            show_data['reddit_score_normalized']
        ]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor='rgba(97, 0, 153, 0.3)',
            line=dict(color='#610099', width=2),
            name=selected_show
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True, 
                    range=[0, 1],
                    gridcolor='#e5e5e5',
                    tickfont=dict(color='#333333')
                ),
                angularaxis=dict(
                    gridcolor='#e5e5e5',
                    tickfont=dict(color='#333333')
                ),
                bgcolor='rgba(0,0,0,0)'
            ),
            showlegend=False,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Inter, sans-serif", color="#333333"),
            margin=dict(t=20, b=20)
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with col2:
        st.markdown("<h3>Details</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5;'>
            <p style='margin: 0.5rem 0; color: #666666;'><strong style='color: #610099;'>Genres:</strong> {', '.join(show_data['genres'])}</p>
            <p style='margin: 0.5rem 0; color: #666666;'><strong style='color: #610099;'>First Aired:</strong> {show_data['first_air_date']}</p>
            <p style='margin: 0.5rem 0; color: #666666;'><strong style='color: #610099;'>Status:</strong> {show_data['status']}</p>
            <p style='margin: 0.5rem 0; color: #666666;'><strong style='color: #610099;'>Type:</strong> {show_data['type']}</p>
            <p style='margin: 0.5rem 0; color: #666666;'><strong style='color: #610099;'>Popularity:</strong> {show_data['popularity']:.0f}</p>
            <p style='margin: 0.5rem 0; color: #666666;'><strong style='color: #610099;'>Episodes/Season:</strong> {show_data['avg_episodes_per_season']:.1f}</p>
        </div>
        """, unsafe_allow_html=True)

# Tab 4: Methodology
with tab4:
    st.markdown("<h2>Methodology</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p><strong>This tool analyzes TV shows across five key dimensions to determine their suitability as background content while working or doing other activities.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>Scoring Components</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5; margin-bottom: 1rem;'>
            <h4 style='color: #610099; margin-top: 0;'>Genre Score (30%)</h4>
            <p style='color: #666666; line-height: 1.6;'>
            Evaluates genre suitability for background viewing. Comedies and family shows score higher, 
            while thrillers and crime dramas score lower.
            </p>
        </div>
        
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5; margin-bottom: 1rem;'>
            <h4 style='color: #610099; margin-top: 0;'>Description Score (25%)</h4>
            <p style='color: #666666; line-height: 1.6;'>
            Analyzes show descriptions for complexity indicators. Shows with simpler, comfort-oriented 
            descriptions receive higher scores.
            </p>
        </div>
        
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5;'>
            <h4 style='color: #610099; margin-top: 0;'>Episodic Score (20%)</h4>
            <p style='color: #666666; line-height: 1.6;'>
            Based on episodes per season. More episodic shows (20+ episodes/season) score higher 
            than heavily serialized shows (8-13 episodes/season).
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5; margin-bottom: 1rem;'>
            <h4 style='color: #610099; margin-top: 0;'>Popularity Score (15%)</h4>
            <p style='color: #666666; line-height: 1.6;'>
            Cultural familiarity proxy. More popular shows are easier to follow casually since 
            viewers may already know the premise and characters.
            </p>
        </div>
        
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5; margin-bottom: 1rem;'>
            <h4 style='color: #610099; margin-top: 0;'>Reddit Sentiment (10%)</h4>
            <p style='color: #666666; line-height: 1.6;'>
            Analyzes Reddit discussions for mentions of "background," "comfort," "rewatch," and related 
            keywords. Lower weight due to limited data availability.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3>Data Sources</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e5e5e5;'>
        <p style='color: #666666; margin: 0.5rem 0;'><strong style='color: #610099;'>TMDb API:</strong> Show metadata, ratings, popularity, episode counts, and descriptions</p>
        <p style='color: #666666; margin: 0.5rem 0;'><strong style='color: #610099;'>Reddit:</strong> User discussions and sentiment from relevant subreddits</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3>Score Interpretation</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #e8f5e9; padding: 1.5rem; border-radius: 8px; border-left: 3px solid #4caf50;'>
            <h4 style='color: #2e7d32; margin-top: 0;'>80 - 100</h4>
            <p style='color: #1b5e20; margin: 0;'>Excellent background content. Episodic, lighthearted, doesn't require constant attention.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #fff3e0; padding: 1.5rem; border-radius: 8px; border-left: 3px solid #ff9800;'>
            <h4 style='color: #e65100; margin-top: 0;'>50 - 79</h4>
            <p style='color: #bf360c; margin: 0;'>Moderate background potential. May require occasional attention but generally suitable.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #ffebee; padding: 1.5rem; border-radius: 8px; border-left: 3px solid #f44336;'>
            <h4 style='color: #c62828; margin-top: 0;'>0 - 49</h4>
            <p style='color: #b71c1c; margin: 0;'>Not recommended for background. Complex plots, intense themes, or heavy serialization.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    Data collected February 2026 | Analyzed 250 top-rated TV shows | Built with Streamlit & Plotly
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    Created by Nikhil Thamma | Data Scientist & Analyst<br>
    Python • Streamlit • Plotly • TMDb API • NLP Sentiment Analysis
</div>
""", unsafe_allow_html=True)