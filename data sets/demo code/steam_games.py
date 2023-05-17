import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# wget https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/best_steam_video_games.csv

# Define the dictionary for platform mapping
platforms = {
    'PC': 'PC',
    'PlayStation': ['PlayStation 5', 'PlayStation', 'PlayStation 2', 'PlayStation 4', 'PlayStation 3'],
    'Xbox': ['Xbox', 'Xbox Series X', 'Xbox One', 'Xbox 360'],
    'Nintendo': ['Switch', 'Wii', 'Nintendo 64', 'Wii U', 'GameCube', '3DS', 'Game Boy Advance'],
    'Other': ['Dreamcast']
}

def get_publisher(platform):
    for k, v in platforms.items():
        if platform in v:
            return k
    return None

def plot_graph(df):
    # Remove duplicate games based on the "Name" column
    df = df.drop_duplicates(subset="Name").copy()

    # Add the "Publisher" column based on the "Platform" column
    df.loc[:, 'Publisher'] = df['Platform'].apply(get_publisher)

    # Group the games by publisher and calculate the average scores
    grouped = df.groupby('Publisher')['Metascore'].mean()

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

    # Plot the average scores by publisher
    ax1.bar(grouped.index, grouped.values)
    ax1.set_title("Average Scores by Publisher")
    ax1.set_xlabel("Publisher")
    ax1.set_ylabel("Average Score")

    # Set the tick locations and labels for the x-axis in subplot 1
    ax1.set_xticks(range(len(grouped.index)))
    ax1.set_xticklabels(grouped.index, rotation=45)

    # Subplot 2: Top 5 Highest Scoring Games
    top_five_games = df.nlargest(5, "Metascore")
    ax2.barh(top_five_games["Name"], top_five_games["Metascore"], color="#FF6F61")
    ax2.set_xlabel("Score")
    ax2.set_ylabel("Game Title")
    ax2.set_title("Top 5 Highest Scoring Games (Cross Platform)")

    # Annotate the scores on top of each bar in subplot 2
    for i, (name, score) in enumerate(zip(top_five_games["Name"], top_five_games["Metascore"])):
        ax2.annotate(str(score), xy=(score, i), xytext=(score + 1, i),
                     ha='left', va='center')

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()


def main():
    # Read the CSV file into a DataFrame
    df = pd.read_csv("best_steam_video_games.csv")

    # Call the plot_graph function
    plot_graph(df)
    
if __name__ == "__main__":
    main()
