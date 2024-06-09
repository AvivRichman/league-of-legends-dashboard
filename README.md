# League of Legends Dashboard

A Python-based dashboard for analyzing and visualizing player data from the game League of Legends. This dashboard fetches data from the Riot Games API and displays various performance metrics and visualizations.

If you want to see my whole way of thinking behind this dashboard, Which describes all the parameters, metrics, tools, and analytical mindset behind this dashboard. you can go to "analysis.md" and enjoy the ride with me :)


## Features

- Retrieve player data using the Riot Games API
- Display general statistics such as KDA, wards placed, wards killed, etc...
- Show efficiency metrics like KDA per minute, damage per minute, gold per minute, and CS per minute
- Display lane control metrics such as CS differential, XP differential, and gold differential at 10 minutes
- Visualize most played champions with icons
- Display who reaches level 5 faster between the player and their opponent
- Visualize player deaths on a map by KDA

## Important!!!

  **The code will not run** as-is because accessing the Riot Games API requires an API key. I do not publish my personal key here, but you can obtain your own key through the Riot Games developer portal at the following link: [Riot Games Developer Portal](https://developer.riotgames.com/).

If you have the API key, Paste it inside the "main.py" file into a variable named "key" in row number 8 (it's important to make sure you paste the key in quotes)

For any questions on the subject, please contact me using the details at the bottom of this README file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/league-of-legends-dashboard.git
    ```

2. Navigate to the project directory:

    ```bash
    cd league-of-legends-dashboard
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your API key:
    - Replace `key = "YOUR-API-KEY"` in the `Main.py` file with your Riot Games API key.

## Usage

1. Run the `Dashboard.py` script to launch the dashboard:

    ```bash
    python Dashboard.py
    ```

2. Enter the required information in the dashboard interface:
    - Summoner name
    - Tag line
    - Region (EUNE, EUW, NA)
    - Type of game (ranked, normal)
    - Number of matches to analyze (Minimum 3)

3. Click the "Analyze" button to fetch and display the data.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information

For any questions or feedback, please contact:

- **Aviv Richman**
- **Email:** Aviv12321@gmail.com
- **GitHub:** [AvivRichman](https://github.com/AvivRichman)
