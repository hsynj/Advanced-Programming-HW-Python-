import pandas as pd
import sqlite3
import re

# Step 1: Read La Liga table from BBC website
url = 'https://www.bbc.com/sport/football/spanish-la-liga/table'
tables = pd.read_html(url)
laliga_table = tables[0]

# Clean team names (remove ranking numbers like '1 Barcelona' -> 'Barcelona')
team_column = 'Team' if 'Team' in laliga_table.columns else laliga_table.columns[0]
laliga_table[team_column] = laliga_table[team_column].astype(str).apply(lambda x: re.sub(r'^\d+\s*', '', x))

# Save to SQLite database
conn = sqlite3.connect('laliga.db')
laliga_table.to_sql('laliga_table', conn, if_exists='replace', index=False)
conn.close()

print("La Liga table saved to database successfully.")

# Print team(s) with highest goal difference
max_gd = laliga_table['Goal Difference'].max()
top_gd_teams = laliga_table[laliga_table['Goal Difference'] == max_gd][team_column].tolist()
print(f"Team(s) with the highest goal difference ({max_gd}): {', '.join(top_gd_teams)}")

# Print team(s) with most draws
max_draws = laliga_table['Drawn'].max()
top_draw_teams = laliga_table[laliga_table['Drawn'] == max_draws][team_column].tolist()
print(f"Team(s) with the most draws ({max_draws}): {', '.join(top_draw_teams)}")
