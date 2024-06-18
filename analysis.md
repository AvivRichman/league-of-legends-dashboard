# League of Legends Dashboard Analysis

## Introduction

As a passionate gamer and data analyst, I have spent nearly a decade playing League of Legends. This extensive experience has given me a deep understanding of the game's mechanics, strategies, and nuances. Combining my love for gaming with my analytical expertise, I have developed a comprehensive League of Legends dashboard. 

The purpose of this dashboard is to provide a detailed analysis of parameters, metrics, tools, and analytical approaches used in the development of this League of Legends dashboard, offering valuable insights that can help players improve their gameplay. By including this project in my portfolio, I aim to demonstrate my proficiency in data analysis, visualization, and the practical application of analytical skills in a gaming-world context.

**The dashboard can make an analysis between 3-100 matches in the specific modes of Ranked or normal.

## key terms
This section describes the key terms in the League of Legends.

**Champion -**
The specific character chosen by the player for a match.<br />
Importance: Different champions have unique abilities, strengths, and roles that significantly impact gameplay and strategy.

**Role -**
The position or role assigned to the player within the game (e.g., Top, Jungle, Mid, ADC, Support).<br />
Importance: Each role has distinct responsibilities and contributions to the team's success, influencing gameplay style and tactics.

**Game Mode -**
The type of game being played (e.g., Ranked, Normal, ARAM).<br />
Importance: Different game modes have varying rules and objectives, affecting player performance and strategic approach.

**Match Duration -**
The length of time a match lasts.<br />
Importance: Match duration can impact player performance metrics and overall game dynamics.

**Region -**
The geographical region or server where the match was played. (I focus only on Europe and the Americas region)

**Lane -**
The specific lane the player is assigned to (e.g., Top, Jungle, Mid, Bot).<br />
Importance: The lane assignment impacts gameplay strategy, matchups, and role responsibilities.

There are other parameters that I didn't mention in building this dashboard like runes, Items, Summoner Spells, etc....

## Metrics
This section describes the key metrics analyzed in the League of Legends dashboard, providing valuable insights into player performance and gameplay dynamics.

**KDA Ratio**<br />
Description: Kill/Death/Assist ratio.<br />
Calculation: (Kills + Assists) / Deaths<br />
Importance: Measures individual contribution to the team's success, highlighting a player's combat effectiveness and teamwork.

**Average Gold Earned**<br />
Description: The average amount of gold earned per match.<br />
Importance: Indicates economic efficiency and the player's ability to acquire resources necessary for purchasing items and gaining advantages.

**Average Damage Dealt**<br />
Description: The average amount of damage dealt to enemy champions per match.<br />
Importance: Measures offensive contribution, indicating the player's ability to inflict damage and influence fights.

**Average Damage Taken**<br />
Description: The average amount of damage taken from enemy champions per match.<br />
Importance: Reflects the player's ability to absorb damage and their role in protecting teammates or tanking damage.

**Average Game Duration**<br />
Description: The average duration of the player's games.<br />
Purpose: Helps understand the typical length of games and can be used to analyze pacing and game flow.

**Wards placed and destroyed**<br />
Description: Reflects the player's effectiveness in placing and destroying wards, providing vision for the team.<br />
Importance: Essential for map control and strategic planning, as vision helps prevent ambushes and provides crucial information about enemy movements.

**CS per Minute**<br />
Description: The average number of minions killed per minute.<br />
Importance: Indicates farming efficiency, crucial for gaining gold and experience advantages.

**Objective Control**<br />
Description: The player's effectiveness in securing major objectives such as dragons, barons, and turrets.<br />
Importance: Objective control is vital for gaining strategic advantages and securing victories.

These metrics provide a comprehensive overview of player performance, enabling a detailed analysis of strengths, weaknesses, and areas for improvement in League of Legends gameplay.

## Parameters
This section describes all the parameters and the information displayed on the League of Legends dashboard.

**General Stats**<br />

&ensp; Description: A summary of general statistics including total games played, total wins, total losses, and     
&ensp; overall win rate.<br />

&ensp; Purpose: Provides a quick overview of the player's overall performance.<br />

&ensp; Metrics Used: Total Games Played, Total Wins, Total Losses, KDA Ratio, Wards placed and destroyed.<br />

&ensp; Parameters description: <br />
&ensp; &ensp; -Total KDA - The total KDA the player have in the analysis<br />
&ensp; &ensp; -Total wards placed - The total wards the players placed in all the games.<br />
&ensp; &ensp; -Total wards destroyed - The total wards the players destroyed in all the games.<br />

**Who Reaches Level 5 the Fastest**<br />

&ensp; Description: A chart showing the average time it takes for the player to reach level 5 in different matches.<br />
&ensp; Getting to level 5 is critical because in that level you get the ultimate ability called "Ult" - A special<br />
&ensp; &ensp; and unique ability, if you get the ability faster from your enemy you have a significant advantage over him) <br />

&ensp; Purpose: Provides insights into early-game performance and efficiency in gaining experience.<br />

&ensp; Metrics Used: Time to Level 5<br /> 

&ensp; Parameters Description:<br />
&ensp; &ensp; Number of times you reach faster 5: The number of times you reach faster to level 5 more than your <br />
&ensp; &ensp; &ensp; opponent in the same role in all the matches.<br />
&ensp; &ensp; Number of times your opp reach faster 5:  The number of times your opponent in the same role reaches <br /> 
&ensp; &ensp; &ensp; faster to level 5 than you in all the matches.<br />
&ensp; &ensp; Average time of the difference in sec: The average time in seconds that shows the difference in <br />
&ensp; &ensp; &ensp; reaching level 5 between the player and his enemy in the same role. If the time is in <br /> 
&ensp; &ensp; &ensp; plus (above zero)  then the player reaches level 5 faster on average, if the time is <br /> 
&ensp; &ensp; &ensp; minus (below zero)  then the &ensp; &ensp; enemy reaches level 5 faster on average than the player.<br />

**Lane Control Metrics**<br />
&ensp; Description: Parameters that evaluate the differences in the player's performance against his opponent <br />
&ensp; &ensp; in the lane assigned to him within 10 minutes.<br />

&ensp; Purpose: Analyzes the player's effectiveness in the laning phase at the early game, including farming(CS), <br />
&ensp; &ensp; XP, and Gold control which can affect the player's strength and contribution to the team. <br />

&ensp; Metrics Used: CS per Minute, , Gold earned, Xp earned.<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; CS differential at 10 minutes: The differential number of minions killed at 10 minutes.<br />
&ensp; &ensp; XP differential at 10 minutes: The differential number of experience points (XP) at 10 minutes.<br />
&ensp; &ensp; Gold differential at 10 minutes: The differential number of gold they get at 10 minutes.<br />


**Most Played Champions**<br />

&ensp; Description: A list of the player's most played champions with their respective games played.<br />

&ensp; Purpose: Highlights the player's most effective champions.<br />

&ensp; Metrics Used: Games Played per Champion.<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; Top 1 champion: The most played champion with the most games in the number of games the <br /> 
&ensp; &ensp; &ensp; analysis calculates.<br />
&ensp; &ensp; Top 2 champion: The second most played champion with the most games in the number of games the <br /> 
&ensp; &ensp; &ensp; analysis calculates.<br />
&ensp; &ensp; Top 3 champion: The third most played champion with the most games in the number of games the 
&ensp; &ensp; &ensp; analysis calculate.<br />

**Favorite Roles**<br />

&ensp; Description: A breakdown of the player's favorite roles, showing the distribution and KDA rates for each role.<br />

&ensp; Purpose: Highlights the roles in which the player excels.<br />

&ensp; Metrics Used: Role Distribution, KDA Rate<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; N.games: Number of games played in each role.<br />
&ensp; &ensp; KDA: KDA rate for each role.<br />

**Efficiency Metrics**<br />

&ensp; Description: Parameters that measure the player's efficiency in farming, gold earning, and damage dealt .<br />

&ensp; Purpose: Evaluate the player's performance and game pacing.<br />

&ensp; Metrics Used: CS per Minute, Average Gold Earned, Average Game Duration,Average Damage Dealt<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; Damage per minute: The average damage dealt to enemy champions by the player per minute.<br />
&ensp; &ensp; CS per Minute: Average number of minions killed per minute.<br />
&ensp; &ensp; Gold Earned Over Time: Amount of gold earned at different stages of the game.<br />

**pie chart - Position**<br />

&ensp; Description: A pie chart showing the distribution of positions/roles played by the player (e.g., Top, Jungle, &ensp; Mid, ADC, Support).<br />

&ensp; Purpose: Visualizes the player's role distribution, helping to understand which roles are most frequently &ensp; played.<br />

&ensp; Metrics Used: Role Distribution<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; Role Distribution: Percentage of games played in each role.<br />
&ensp; ![Position pie chart](https://github.com/AvivRichman/league-of-legends-dashboard/assets/172200945/7713a761-562d-4de6-a5d1-c16aac6bddd5)

**pie chart - type of kills**<br />

&ensp; Description: A pie chart displaying the distribution of different types of kills achieved by the player <br />
&ensp; &ensp; (e.g., solo kills, ks(kill steak), etc.).<br />

&ensp; Purpose: Visualizes the player's kill distribution, helping to understand the player's impact on the team. &ensp; kills.<br />

&ensp; Metrics Used: Kill Distribution<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; Solo Kill: Kills achieved by the player alone. The player did 100% of the damage to the enemy. <br />
&ensp; &ensp; ks (kill steal): Kills achieved by the player. but he only does below 10% of the damage to the enemy. <br />
&ensp; &ensp; Main Kill: Kills achieved by the player with the help of teammates. But the player did more than 65% <br /> 
&ensp; &ensp; &ensp; of the  damage to the enemy. <br />
&ensp; &ensp; Regular Kill: Kills achieved by the player with the help of teammates. But the player did between 10%-65% <br /> 
&ensp; &ensp; &ensp; damage to the enemy.<br />
&ensp; ![Type of kiils pie chart](https://github.com/AvivRichman/league-of-legends-dashboard/assets/172200945/ebc85a04-7930-439c-b3e3-662763888e1c)

**pie chart - type of death**<br />

&ensp; Description: A pie chart showing the distribution of different types of deaths experienced by the player <br />
&ensp; &ensp; (e.g., solo deaths, team fight deaths, etc..).<br />

&ensp; Purpose: Visualizes the player's death distribution, helping to understand the circumstances leading to deaths.<br />

&ensp; Metrics Used: Death Distribution<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; Solo Death: Deaths where the player dies to only one enemy.<br />
&ensp; &ensp; adc & supp: Deaths where the player dies only to the enemy adc and supp.<br />
&ensp; &ensp; myL & Jun: Deaths where the player dies only to the enemy at the same role and their<br />
&ensp; &ensp; &ensp; jungler (most of the time its means the death was by Gank).<br />
&ensp; &ensp; Team fight: Deaths occurring during team fights 
&ensp; &ensp; (More then 3 participants in the player kill)<br />
![Type of death pie chart](https://github.com/AvivRichman/league-of-legends-dashboard/assets/172200945/7261d4cd-6747-4c3b-aa8c-b460cad674bf)

**Death map by KDA**<br />

&ensp; Description: A heatmap showing the locations of player deaths on the map, color-coded by KDA ratio <br /> 

&ensp; Purpose: Helps identify high-risk areas on the map and understand where players tend to die most frequently,<br /> 
&ensp; &ensp; providing insights into positioning and map awareness.<br />

&ensp; Metrics Used: KDA Ratio, Death Locations<br />

&ensp; Parameters Description:<br />
&ensp; &ensp; Blue points: Where the player died when he got more than 2 KDA at that game.<br />
&ensp; &ensp;  Red points: Where the player died when he got Below than 2 KDA at that game.<br />
![Death map by KDA](https://github.com/AvivRichman/league-of-legends-dashboard/assets/172200945/27f81ef0-0cdb-406b-ae91-0d9ccc6c4d13)



