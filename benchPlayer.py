# Based on the updated image data, let's manually set the projected and actual points for each bench player correctly.

# Manually extracted data for bench players 
bench_data_updated = {
    'Player': ['J. Simmons', 'T. Johnson', 'B. Fiske', 'T. Edmunds', 'K. Murray', 'W. Gay', 'C. DeJean', 
               'A. Rodgers (Bench)', 'J. Mixon (Bench)', 'D. Singletary (Bench)', 
               'J. Bosa', 'J. Jewell', 'J. Sweat', 'T. Tuipulotu', 'J. Greenard', 'K. Paye', 'H. Reddick', 
               'J. McMillan', 'L. McConkey', 'S. Darnold (Bench)', 'D. Cook (Bench)', 'C. Edwards-Helaire (Bench)'],
    'Team': ['Your Team', 'Your Team', 'Your Team', 'Your Team', 'Your Team', 'Your Team', 'Your Team', 
             'Your Team', 'Your Team', 'Your Team', 
             'Opponent', 'Opponent', 'Opponent', 'Opponent', 'Opponent', 'Opponent', 'Opponent', 
             'Opponent', 'Opponent', 'Opponent', 'Opponent'],
    'Projected': [2.74, 2.74, 2.69, 2.94, 2.79, 2.39, 1.11, 
                  22.38, 13.83, 11.61, 
                  2.92, 2.83, 2.97, 3.22, 2.86, 2.87, 1.11, 
                  7.72, 9.83, 21.73, 2.99, 3.17],
    'Actual': [2.50, 0.20, 1.20, 1.00, 1.50, 0.00, 0.00, 
               14.04, 30.60, 9.60, 
               8.40, 1.90, 2.50, 0.00, 0.20, 4.90, 0.00, 
               10.20, 15.10, 23.17, 0.00, 0.00]

}

# Create a DataFrame for the corrected bench players
df_bench_updated = pd.DataFrame(bench_data_updated)

# Recalculate the variance (difference between projected and actual points)
df_bench_updated['Variance'] = df_bench_updated['Actual'] - df_bench_updated['Projected']

# Plot corrected Bench Players: Projected vs Actual points
plt.figure(figsize=(10, 6))
plt.bar(df_bench_updated['Player'], df_bench_updated['Projected'], alpha=0.7, label='Projected', color='gray', width=0.4, align='center')
plt.bar(df_bench_updated['Player'], df_bench_updated['Actual'], alpha=0.7, label='Actual', color='blue', width=0.4, align='edge')
plt.xlabel('Bench Player')
plt.ylabel('Points')
plt.title('Bench Players: Projected vs Actual Points (Fully Corrected)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show the chart
plt.show()

# Correct the variance chart as well for accurate points missed analysis
plt.figure(figsize=(10, 6))
variance_colors_updated = ['green' if var > 0 else 'red' for var in df_bench_updated['Variance']]
plt.barh(df_bench_updated['Player'], df_bench_updated['Variance'], color=variance_colors_updated)
plt.xlabel('Variance (Actual - Projected)')
plt.ylabel('Bench Player')
plt.title('Bench Players: Points Missed (Variance) - Corrected')
plt.tight_layout()

# Show the chart
plt.show()
