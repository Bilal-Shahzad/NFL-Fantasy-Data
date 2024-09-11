# Update the charts to make it clearer which players belong to the opponent by adding team labels in the title and colors

# Create a bar chart for projections vs actuals by player, distinguishing between teams
plt.figure(figsize=(10, 6))
plt.bar(df[df['Team'] == 'Your Team']['Player'], df[df['Team'] == 'Your Team']['Projected'], alpha=0.7, label='Your Team Projected', color='blue')
plt.bar(df[df['Team'] == 'Your Team']['Player'], df[df['Team'] == 'Your Team']['Actual'], alpha=0.7, label='Your Team Actual', color='green')
plt.bar(df[df['Team'] == 'Opponent']['Player'], df[df['Team'] == 'Opponent']['Projected'], alpha=0.7, label='Opponent Projected', color='gray')
plt.bar(df[df['Team'] == 'Opponent']['Player'], df[df['Team'] == 'Opponent']['Actual'], alpha=0.7, label='Opponent Actual', color='red')
plt.xlabel('Player')
plt.ylabel('Points')
plt.title('Projected vs Actual Points by Player (Your Team vs Opponent)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show chart
plt.show()

# Display the variance by player, distinguishing between teams
plt.figure(figsize=(10, 6))
plt.bar(df[df['Team'] == 'Your Team']['Player'], df[df['Team'] == 'Your Team']['Variance'], alpha=0.7, color='green', label='Your Team')
plt.bar(df[df['Team'] == 'Opponent']['Player'], df[df['Team'] == 'Opponent']['Variance'], alpha=0.7, color='red', label='Opponent')
plt.xlabel('Player')
plt.ylabel('Variance (Actual - Projected)')
plt.title('Variance by Player (Your Team vs Opponent)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show chart
plt.show()

# Prepare cumulative chart for team performance, making it clear which players belong to which team
plt.figure(figsize=(10, 6))
plt.plot(df[df['Team'] == 'Your Team']['Player'], df[df['Team'] == 'Your Team']['Actual'], marker='o', color='blue', label='Your Team')
plt.plot(df[df['Team'] == 'Opponent']['Player'], df[df['Team'] == 'Opponent']['Actual'], marker='x', color='red', label='Opponent')
plt.xlabel('Player')
plt.ylabel('Actual Points')
plt.title('Cumulative Performance: Your Team vs Opponent')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show chart
plt.show()
