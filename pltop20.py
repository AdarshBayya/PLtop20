# -*- coding: utf-8 -*-
"""PLtop20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fTQEMPcNYF40tVm5L3ryPISFjqfMboqv
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('20seasons.csv')

data.head(10)

print(data.describe())

# Exclude non-numeric columns (like 'Season' and 'Team') from the correlation matrix
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Now calculate the correlation matrix on numeric data
correlation_matrix = numeric_data.corr()

# Plot the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

"""###Points Per Season  """

plt.figure(figsize=(12, 6))
sns.lineplot(x='Season', y='Pts', data=data, marker='o', color='b')
plt.title('Points per Season in the Premier League')
plt.xlabel('Season')
plt.ylabel('Points')
plt.show()

first_place_teams = data[data['Pos'] == 1]

print("Teams that finished 1st in each season:")
for season, team in first_place_teams.groupby('Season')['Team']:
    print(f"{season}: {team.values[0]}")

import pandas as pd

# Assuming you have a DataFrame named 'data' with the Premier League data

# Count the number of times each team finished 1st
team_wins = data[data['Pos'] == 1]['Team'].value_counts()

# Find the team with the most 1st place finishes
most_successful_team = team_wins.idxmax()
most_wins_count = team_wins.max()

print(f"The team with the most 1st place finishes is {most_successful_team} with {most_wins_count} wins.")

# Remove the most successful team from consideration
remaining_teams = data[data['Team'] != most_successful_team]

# Count the number of times each team finished 2nd
team_2nd_place = remaining_teams[remaining_teams['Pos'] == 2]['Team'].value_counts()
second_most_successful_team = team_2nd_place.idxmax()
second_most_wins_count = team_2nd_place.max()

print(f"The team with the 2nd most 1st place finishes is {second_most_successful_team} with {second_most_wins_count} wins.")

# Remove the 2nd most successful team from consideration
remaining_teams = remaining_teams[remaining_teams['Team'] != second_most_successful_team]

# Count the number of times each team finished 3rd
team_3rd_place = remaining_teams[remaining_teams['Pos'] == 3]['Team'].value_counts()
third_most_successful_team = team_3rd_place.idxmax()
third_most_wins_count = team_3rd_place.max()

print(f"The team with the 3rd most 1st place finishes is {third_most_successful_team} with {third_most_wins_count} wins.")

team_wins = data[data['Pos'] == 1]['Team'].value_counts()

# Get the top 5 teams with the most 1st place finishes
top_5_teams = team_wins.head(5)

# Plotting
plt.figure(figsize=(10, 6))
top_5_teams.plot(kind='bar', color='skyblue')
plt.title('Top 5 Teams with Most Premier League From 2000-2022')
plt.xticks(rotation=45, ha='right')
plt.show()

"""###Goal Difference"""

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for Goal Difference per Season
sns.barplot(x='Season', y='GD', data=data, palette='coolwarm')

plt.title('Goal Difference per Season in the Premier League')
plt.xlabel('Season')
plt.ylabel('Goal Difference')

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

# Plotting
plt.figure(figsize=(12, 6))

# Horizontal bar chart for Goal Difference per Team
sns.barplot(x='GD', y='Team', data=data, palette='coolwarm')

plt.title('Goal Difference per Team in the Premier League')
plt.xlabel('Goal Difference')
plt.ylabel('Team')
plt.show()

"""###Goals for & Goals Against"""

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for Goals For and Goals Against per Season
sns.barplot(x='Season', y='GF', data=data, color='green', label='Goals For')
sns.barplot(x='Season', y='GA', data=data, color='red', label='Goals Against')

plt.title('Goals For and Goals Against per Season in the Premier League')
plt.xlabel('Season')
plt.ylabel('Goals')
plt.legend()

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a DataFrame named 'data' with the Premier League data

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for Goals For and Goals Against per Team
sns.barplot(x='Team', y='GF', data=data, color='green', label='Goals For')
sns.barplot(x='Team', y='GA', data=data, color='red', label='Goals Against')

plt.title('Goals For and Goals Against per Team in the Premier League')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.legend()

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

# Get the top 5 teams based on total Goals For
top_5_teams = data.groupby('Team')['GF'].sum().nlargest(5).index

# Filter the data for the top 5 teams
top_5_data = data[data['Team'].isin(top_5_teams)]

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for Goals For and Goals Against per Team (Top 5)
sns.barplot(x='Team', y='GF', data=top_5_data, color='green', label='Goals For')
sns.barplot(x='Team', y='GA', data=top_5_data, color='red', label='Goals Against')

plt.title('Goals For and Goals Against per Team (Top 5) in the Premier League')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.legend()

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

"""###Postition"""

# Bar chart for Wins, Draws, and Losses per Season
plt.figure(figsize=(12, 6))
sns.barplot(x='Season', y='W', data=data, color='green', label='Wins')
sns.barplot(x='Season', y='D', data=data, color='yellow', label='Draws')
sns.barplot(x='Season', y='L', data=data, color='red', label='Losses')
plt.title('Wins, Draws, and Losses per Season in the Premier League')
plt.xlabel('Season')
plt.ylabel('Count')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a DataFrame named 'data' with the Premier League data

# Find the teams that finished 1st in each season
first_place_teams = data[data['Pos'] == 1]

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for Wins, Draws, and Losses for the team that finished 1st in each season
sns.barplot(x='Season', y='W', data=first_place_teams, color='green', label='Wins')
sns.barplot(x='Season', y='D', data=first_place_teams, color='orange', label='Draws')
sns.barplot(x='Season', y='L', data=first_place_teams, color='red', label='Losses')

plt.title('Wins, Draws, and Losses for the Team that Finished 1st in Each Season')
plt.xlabel('Season')
plt.ylabel('Number of Matches')
plt.legend()

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

# Group by team and sum the number of wins
team_wins = data.groupby('Team')['W'].sum().nlargest(5)

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for the total number of wins for the top 5 teams
sns.barplot(x=team_wins.index, y=team_wins.values, color='green')

# Add labels and title
plt.title('Total Wins for the Top 5 Teams in the Premier League')
plt.xlabel('Team')
plt.ylabel('Total Wins')

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

# Group by team and sum the number of losses
team_losses = data.groupby('Team')['L'].sum().nlargest(5)

# Group by team and sum the number of draws
team_draws = data.groupby('Team')['D'].sum().nlargest(5)

# Plotting
fig, axes = plt.subplots(2, 1, figsize=(12, 12))

# Bar chart for the total number of losses for the top 5 teams
sns.barplot(x=team_losses.index, y=team_losses.values, color='red', ax=axes[0])
axes[0].set_title('Total Losses for the Top 5 Teams in the Premier League')
axes[0].set_xlabel('Team')
axes[0].set_ylabel('Total Losses')
axes[0].tick_params(axis='x', labelrotation=45, labelsize=8)

# Bar chart for the total number of draws for the top 5 teams
sns.barplot(x=team_draws.index, y=team_draws.values, color='orange', ax=axes[1])
axes[1].set_title('Total Draws for the Top 5 Teams in the Premier League')
axes[1].set_xlabel('Team')
axes[1].set_ylabel('Total Draws')
axes[1].tick_params(axis='x', labelrotation=45, labelsize=8)

plt.tight_layout()
plt.show()

"""###Pos"""

# Get the top 5 teams based on their average final position
top_5_teams = data.groupby('Team')['Pos'].mean().nsmallest(5)

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart for the final positions of the top 5 teams
sns.barplot(x=top_5_teams.index, y=top_5_teams.values, color='blue')

# Add labels and title
plt.title('Final Positions for the Top 5 Teams (Average) in the Premier League')
plt.xlabel('Team')
plt.ylabel('Average Final Position')

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

# Plotting
plt.figure(figsize=(12, 6))

# Box plot for the distribution of final positions
sns.boxplot(x='Season', y='Pos', data=data, palette='Set3')

# Add labels and title
plt.title('Distribution of Final Positions in the Premier League Over Seasons')
plt.xlabel('Season')
plt.ylabel('Final Position')

# Adjust x-axis label size
plt.xticks(fontsize=8, rotation=45, ha='right')

plt.show()

import pandas as pd

# Assuming you have a DataFrame named 'data' with the Premier League data

# Group by team and count the occurrences in position 1
team_pos1_counts = data[data['Pos'] == 1].groupby('Team')['Pos'].count()

# Find the team with the maximum occurrences in position 1
team_with_most_pos1 = team_pos1_counts.idxmax()
most_pos1_count = team_pos1_counts.max()

print(f"The team that stayed in position 1 for the longest time is '{team_with_most_pos1}' with {most_pos1_count} occurrences.")