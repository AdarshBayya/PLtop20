# Premier League Analysis (2000-2022)

This project performs data analysis on Premier League football seasons from 2000 to 2022. It generates various visualizations to explore trends in team performances, including points, wins, losses, goal differences, and league positions. The analysis is performed using Python libraries like pandas, matplotlib, and seaborn.

# Table of Contents

Project Overview
Installation
Usage
Visualizations and Analysis
Correlation Matrix
Points per Season
Top Teams Analysis
Goal Differences
Goals For & Against
Wins, Draws, and Losses
Final Positions
Data Source
License

# Project Overview
The goal of this project is to analyze and visualize team performances in the English Premier League across 20 seasons (2000–2022). This includes identifying trends in points, wins, losses, goal differences, goals scored, and positions achieved by the teams. The analysis identifies the most successful teams over time and provides insights into which teams have consistently performed well or struggled in the league.

# Visualizations and Analysis

# Correlation Matrix
The correlation matrix highlights the relationships between various numerical metrics (e.g., points, goals, wins, losses). It provides insights into how these metrics influence each other.

# Heatmap
A heatmap is used to visualize the correlation matrix, where each cell shows the strength of correlation between metrics.

# Points per Season
A line plot visualizes the points accumulated by teams across different seasons, allowing you to track trends over time.
X-axis: Season
Y-axis: Points

# Top Teams Analysis
This section identifies and visualizes the top teams based on their finishing positions in the league.
First Place Teams: Teams that finished 1st in each season.
Top 5 Teams with Most Wins: A bar chart showing the teams with the most 1st-place finishes.
Second and Third Most Successful Teams: An analysis of the teams that finished 2nd and 3rd most often.

# Goal Difference
Analyzes goal differences for each season and team, which is a strong indicator of overall performance.
Goal Difference per Season: A bar chart showing the goal difference for each team in each season.
Goal Difference per Team: A horizontal bar chart showing the goal difference per team across seasons.

# Goals For & Goals Against
A comparison of goals scored and conceded by each team.
Goals For and Against per Season: A bar chart comparing goals scored (GF) and conceded (GA) in each season.
Goals For and Against per Team: A similar comparison for individual teams.

# Wins, Draws, and Losses
Bar charts show the number of wins, draws, and losses for each team and season.
Wins, Draws, and Losses per Season: A stacked bar chart that compares wins, draws, and losses for all teams in each season.
Top 5 Teams with Most Wins, Losses, and Draws: Separate visualizations for the teams with the most wins, losses, and draws.

# Final Positions
This section examines the final positions achieved by teams over the seasons.
Final Positions for Top 5 Teams: A bar chart showing the average final position of the top 5 teams in the Premier League.
Box Plot of Final Positions: A box plot to observe the distribution of final positions across all teams over the seasons.

# Data Source
The dataset 20seasons.csv contains team performance metrics from Premier League seasons between 2000 and 2022. Each row in the dataset represents a team's performance in a particular season, with columns such as:

Season: The season year (e.g., 2000-2001)
Team: The name of the team
Pos: Final league position
Pts: Total points
W: Wins
D: Draws
L: Losses
GF: Goals For
GA: Goals Against
GD: Goal Difference

# License
This project is licensed under the MIT License - see the LICENSE file for details.

