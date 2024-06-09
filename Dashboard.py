import tkinter as tk
from tkinter import ttk
import Main
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import requests
import io

def Start_dashboard():
    # Moving Developer name FRAME
    Dev_name_frame.place(x=1, y=867, relx=0.004, rely=0.01)

    # General data that the user enters to start the dashboard calculation
    summoner_name = str(Summoner_name_Entry.get())
    tagline_name = str(tagline_Entry.get())
    summoner_region = Region_combobox.get()
    type_of_game = Type_combobox.get()
    number_of_games = int(Number_of_matches_spinbox.get())

    Data_frame = Main.start_main(summoner_name, tagline_name, summoner_region, number_of_games, type_of_game)

    # General info
    root.geometry("1043x905")
    root.title("League of Legends pro analytics stats")

    # style
    root.configure(bg="#333333")

    # Note title
    title_label = tk.Label(root, text="NOTE: Remember your analyze is for " + str(number_of_games) + " games!  |  The code may remove games with incorrect data, reducing their count. ", font=("", 13),
                           bg="#333333", fg="#FFFFFF")
    title_label.place(x=140, y=867, relx=0.004, rely=0.01)

    # General states

    # frame for stats
    State_frame = tk.LabelFrame(root, text="General States", bg="#333333", fg="#FFFFFF", labelanchor="n")
    State_frame.place(x=26, y=1, relx=0.15, rely=0.01)

    # Total kda label
    total_kda_Label = tk.Label(State_frame, text="Total KDA - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    total_kda_Label.grid(row=0, column=0, sticky="n", padx=5, pady=7)

    # Total kda data
    total_kda_data = tk.Label(State_frame, text=round(((Data_frame[0]['Kills'].sum() + Data_frame[0]['Assists'].sum()) / Data_frame[0]['Deaths'].sum()), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    total_kda_data.grid(row=0, column=1, sticky="n", padx=5, pady=7)

    # Total wards placed label
    total_wards_Placed_Label = tk.Label(State_frame, text="Total wards placed - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    total_wards_Placed_Label.grid(row=1, column=0, sticky="n", padx=5, pady=7)

    # Total wards placed data
    total_wards_Placed_data = tk.Label(State_frame, text=round(Data_frame[0]['Wards_placed'].sum(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    total_wards_Placed_data.grid(row=1, column=1, sticky="n", padx=5, pady=7)

    # Total wards killed label
    total_wards_killed_Label = tk.Label(State_frame, text="Total wards destroyed - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    total_wards_killed_Label.grid(row=2, column=0, sticky="n", padx=5, pady=7)

    # Total wards killed data
    total_wards_killed_data = tk.Label(State_frame, text=round(Data_frame[0]['Wards_killed'].sum(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    total_wards_killed_data.grid(row=2, column=1, sticky="n", padx=5, pady=7)

    # Efficiency Metrics
    efficiency_metrics_frame = tk.LabelFrame(root, text="Efficiency Metrics", bg="#333333", fg="#FFFFFF", labelanchor="n")
    efficiency_metrics_frame.place(x=1, y=612, relx=0.004, rely=0.01)

    # KDA per minute label
    kda_per_min_Label = tk.Label(efficiency_metrics_frame, text="KDA per minute - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    kda_per_min_Label.grid(row=0, column=0, sticky="n", padx=5, pady=7)

    # KDA per minute data
    kda_per_min_data = tk.Label(efficiency_metrics_frame, text=round(Data_frame[0]['KDA_per_min'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    kda_per_min_data.grid(row=0, column=1, sticky="n", padx=5, pady=7)

    # Damage per minute label
    dmg_per_min_Label = tk.Label(efficiency_metrics_frame, text="Damage per minute - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    dmg_per_min_Label.grid(row=1, column=0, sticky="n", padx=5, pady=7)

    # Damage per minute data
    dmg_per_min_data = tk.Label(efficiency_metrics_frame, text=round(Data_frame[0]['Dmg_per_min'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    dmg_per_min_data.grid(row=1, column=1, sticky="n", padx=5, pady=7)

    # Gold per minute label
    gold_per_min_Label = tk.Label(efficiency_metrics_frame, text="Gold per minute - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    gold_per_min_Label.grid(row=2, column=0, sticky="n", padx=5, pady=7)

    # Gold per minute data
    gold_per_min_data = tk.Label(efficiency_metrics_frame, text=round(Data_frame[0]['Gold_per_min'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    gold_per_min_data.grid(row=2, column=1, sticky="n", padx=5, pady=7)

    # CS per minute label
    cs_per_min_Label = tk.Label(efficiency_metrics_frame, text="CS per minute - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    cs_per_min_Label.grid(row=3, column=0, sticky="n", padx=5, pady=7)

    # CS per minute data
    cs_per_min_data = tk.Label(efficiency_metrics_frame, text=round(Data_frame[0]['CS_per_min'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    cs_per_min_data.grid(row=3, column=1, sticky="n", padx=5, pady=7)

    # Lane Control Metrics
    lane_control_frame = tk.LabelFrame(root, text="Lane Control Metrics", bg="#333333", fg="#FFFFFF", labelanchor="n")
    lane_control_frame.place(x=502, y=1, relx=0.15, rely=0.01)

    # CS differential at 10 minutes label
    cs_diff_10_Label = tk.Label(lane_control_frame, text="CS differential at 10 min - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    cs_diff_10_Label.grid(row=0, column=0, sticky="n", padx=5, pady=7)

    # CS differential at 10 minutes data
    cs_diff_10_data = tk.Label(lane_control_frame, text=round(Data_frame[0]['CS_diff_at_10'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    cs_diff_10_data.grid(row=0, column=1, sticky="n", padx=5, pady=7)

    # XP differential at 10 minutes label
    xp_diff_10_Label = tk.Label(lane_control_frame, text="XP differential at 10 min - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    xp_diff_10_Label.grid(row=1, column=0, sticky="n", padx=5, pady=7)

    # XP differential at 10 minutes data
    xp_diff_10_data = tk.Label(lane_control_frame, text=round(Data_frame[0]['XP_diff_at_10'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    xp_diff_10_data.grid(row=1, column=1, sticky="n", padx=5, pady=7)

    # Gold differential at 10 minutes label
    gold_diff_10_Label = tk.Label(lane_control_frame, text="Gold differential at 10 min - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    gold_diff_10_Label.grid(row=2, column=0, sticky="n", padx=5, pady=7)

    # Gold differential at 10 minutes data
    gold_diff_10_data = tk.Label(lane_control_frame, text=round(Data_frame[0]['Gold_diff_at_10'].mean(), 2), font=("", 8), bg="#333333", fg="#FFFFFF")
    gold_diff_10_data.grid(row=2, column=1, sticky="n", padx=5, pady=7)

    # Most played champions

    # Create a count for the most frequnsi champion
    top_champions = Data_frame[0]["Champion_name"].value_counts()

    # Photo prepreition
    def url(Champname, size):
        response = requests.get("http://ddragon.leagueoflegends.com/cdn/13.12.1/img/champion/" + Champname.capitalize() + ".png")
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        resized_image = image.resize(size)
        photo = ImageTk.PhotoImage(resized_image)
        return photo

    size = (30, 30)

    # Tops 3 champion frame
    Tops_3_champ_frame = tk.LabelFrame(root, text="Most played champions", bg="#333333", fg="#FFFFFF", labelanchor="n")
    Tops_3_champ_frame.place(x=1, y=332, relx=0.004, rely=0.01)

    # Top 1 champion label
    Top_1_champ_Label = tk.Label(Tops_3_champ_frame, text="Top 1 champion - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    Top_1_champ_Label.grid(row=0, column=0, sticky="n", padx=5, pady=7)

    # Top 1 champion photo
    photo_top1 = url(str(top_champions.index[0]), size)
    champ_name_top1_photo = tk.Label(Tops_3_champ_frame, image=photo_top1, highlightthickness=0, bd=0)
    champ_name_top1_photo.image = photo_top1
    champ_name_top1_photo.grid(row=0, column=1, sticky="n", padx=(5, 0), pady=7)
    champ_name_top1_photo.configure(highlightbackground=Tops_3_champ_frame.cget('bg'))

    # Top 1 champion data
    champ_name_top1_data = tk.Label(Tops_3_champ_frame, text=top_champions.index[0], font=("", 8), bg="#333333", fg="#FFFFFF")
    champ_name_top1_data.grid(row=0, column=2, sticky="n", padx=5, pady=7)

    # Top 2 champion label
    Top_2_champ_Label = tk.Label(Tops_3_champ_frame, text="Top 2 champion - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    Top_2_champ_Label.grid(row=1, column=0, sticky="n", padx=5, pady=7)

    # Top 2 champion photo
    photo_top2 = url(str(top_champions.index[1]), size)
    champ_name_top2_photo = tk.Label(Tops_3_champ_frame, image=photo_top2, highlightthickness=0, bd=0)
    champ_name_top2_photo.image = photo_top2
    champ_name_top2_photo.grid(row=1, column=1, sticky="n", padx=(5, 0), pady=7)
    champ_name_top2_photo.configure(highlightbackground=Tops_3_champ_frame.cget('bg'))

    # Top 2 champion data
    champ_name_top2_data = tk.Label(Tops_3_champ_frame, text=top_champions.index[1], font=("", 8), bg="#333333", fg="#FFFFFF")
    champ_name_top2_data.grid(row=1, column=2, sticky="n", padx=5, pady=7)

    # Top 3 champion label
    Top_3_champ_Label = tk.Label(Tops_3_champ_frame, text="Top 3 champion - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    Top_3_champ_Label.grid(row=2, column=0, sticky="n", padx=5, pady=7)

    # Top 3 champion photo
    photo_top3 = url(str(top_champions.index[2]), size)
    champ_name_top3_photo = tk.Label(Tops_3_champ_frame, image=photo_top3, highlightthickness=0, bd=0)
    champ_name_top3_photo.image = photo_top3
    champ_name_top3_photo.grid(row=2, column=1, sticky="n", padx=(5, 0), pady=7)
    champ_name_top3_photo.configure(highlightbackground=Tops_3_champ_frame.cget('bg'))

    # Top 3 champion data
    champ_name_top3_data = tk.Label(Tops_3_champ_frame, text=top_champions.index[2], font=("", 8), bg="#333333", fg="#FFFFFF")
    champ_name_top3_data.grid(row=2, column=2, sticky="n", padx=5, pady=7)

    # Level 5 details
    Level_5_frame = tk.LabelFrame(root, text="Who reach faster to level 5", bg="#333333", fg="#FFFFFF", labelanchor="n")
    Level_5_frame.place(x=226, y=1, relx=0.15, rely=0.01)

    # Total number reach level 5 player label
    total_counter_level3_player_Label = tk.Label(Level_5_frame, text="Number of times you reach faster -  ", font=("", 8), bg="#333333", fg="#FFFFFF")
    total_counter_level3_player_Label.grid(row=0, column=0, sticky="n", padx=5, pady=7)

    # Total number reach level 5 player data
    value_counts = Data_frame[0]['level_5_player'].value_counts()

    total_counter_level3_player_data = tk.Label(Level_5_frame, text=value_counts[True].sum(), font=("", 8), bg="#333333", fg="#FFFFFF")
    total_counter_level3_player_data.grid(row=0, column=1, sticky="n", padx=5, pady=7)

    # Total number your opponent reach level 5 label
    total_counter_level3_opponent_Label = tk.Label(Level_5_frame, text="Number of times your opp reach faster -  ", font=("", 8), bg="#333333", fg="#FFFFFF")
    total_counter_level3_opponent_Label.grid(row=1, column=0, sticky="n", padx=5, pady=7)

    # Total number your opponent reach level 5 data
    total_counter_level3_opponent_data = tk.Label(Level_5_frame, text=value_counts[False].sum(), font=("", 8), bg="#333333", fg="#FFFFFF")
    total_counter_level3_opponent_data.grid(row=1, column=1, sticky="n", padx=5, pady=7)

    # Average time of the difference label
    Average_time_Label = tk.Label(Level_5_frame, text="Average time of the difference in sec - ", font=("", 8), bg="#333333", fg="#FFFFFF")
    Average_time_Label.grid(row=2, column=0, sticky="n", padx=5, pady=7)

    # Average time of the difference data
    level_5_average_DF = Data_frame[0]
    level_5_average_DF["Time Difference"] = Data_frame[0]['Time_level_5_player'] - Data_frame[0]['Time_level_5_Opponent']
    Average_time = -round(level_5_average_DF["Time Difference"].mean() / 1000, 2)

    Average_time_data = tk.Label(Level_5_frame, text=Average_time, font=("", 8), bg="#333333", fg="#FFFFFF")
    Average_time_data.grid(row=2, column=1, sticky="n", padx=5, pady=7)

    # Favorite Roles

    # Mean of KDA by position frame
    KDA_by_position_frame = tk.LabelFrame(root, text="Favorite Roles", bg="#333333", fg="#FFFFFF", labelanchor="n")
    KDA_by_position_frame.place(x=1, y=487, relx=0.004, rely=0.01)

    # Prepare the data use this data also in the
    mean_kda_data = Data_frame[0]
    mean_kda_data['number_of_games'] = mean_kda_data.groupby("Player_position")["KDA"].transform('count')
    mean_kda_data_MAIN = mean_kda_data.groupby('Player_position').agg({'KDA': 'mean', 'number_of_games': 'first'}).sort_values(by='KDA', ascending=False)

    # First row object (Headers)
    # Position label
    Mean_position_Label = tk.Label(KDA_by_position_frame, text="Position ", font=("", 8), bg="#333333", fg="#FFFFFF")
    Mean_position_Label.grid(row=0, column=0, sticky="n", padx=5, pady=7)
    # kda label
    kda_position_Label = tk.Label(KDA_by_position_frame, text="KDA ", font=("", 8), bg="#333333", fg="#FFFFFF")
    kda_position_Label.grid(row=0, column=1, sticky="n", padx=5, pady=7)
    # N.games label
    N_games_position_Label = tk.Label(KDA_by_position_frame, text="N.games ", font=("", 8), bg="#333333", fg="#FFFFFF")
    N_games_position_Label.grid(row=0, column=2, sticky="n", padx=5, pady=7)

    Mean_KDA_count = 1

    for position, kda in mean_kda_data_MAIN.iterrows():
        if kda['KDA'] != 0:
            position_label = tk.Label(KDA_by_position_frame, text=position + " - ", font=("", 8), bg="#333333", fg="#FFFFFF")
            position_label.grid(row=Mean_KDA_count, column=0, sticky="n", padx=5, pady=7)

            kda_label = tk.Label(KDA_by_position_frame, text=round(kda['KDA'], 2), font=("", 8), bg="#333333", fg="#FFFFFF")
            kda_label.grid(row=Mean_KDA_count, column=1, sticky="n", padx=5, pady=7)

            number_of_game_label = tk.Label(KDA_by_position_frame, text=round(kda['number_of_games'], 1), font=("", 8), bg="#333333", fg="#FFFFFF")
            number_of_game_label.grid(row=Mean_KDA_count, column=2, sticky="n", padx=5, pady=7)

            Mean_KDA_count += 1

    # Position rate
    Position_frame = tk.LabelFrame(root, text="Positions", bg="#333333", fg="#FFFFFF", labelanchor="n")
    Position_frame.place(x=26, y=156, relx=0.15, rely=0.01)

    # Prepare the data
    Position_rate_data = Data_frame[0]
    Position_rate_data['number_of_games'] = Position_rate_data.groupby("Player_position").count
    mean_kda_data_MAIN = Position_rate_data.groupby("Player_position").size()

    fig = plt.figure(figsize=(2.5, 2.5), dpi=100)

    fig.patch.set_facecolor("#333333")
    plt.rcParams['text.color'] = '#FFFFFF'

    mean_kda_data_MAIN.plot(kind='pie', y=0, labels=mean_kda_data_MAIN.index, autopct='%.0f%%')

    canvas_Positions_bar = FigureCanvasTkAgg(fig, master=Position_frame)
    canvas_Positions_bar.draw()
    canvas_Positions_bar.get_tk_widget().pack()
    # type_of_kills
    type_of_killing_frame = tk.LabelFrame(root, text="Type of kills", bg="#333333", fg="#FFFFFF", labelanchor="n")
    type_of_killing_frame.place(x=292, y=156, relx=0.15, rely=0.01)

    # type_of_killing data
    type_of_killing_label = ["Main kill", "ks", "Regular kill", "Solo kill"]
    type_of_killing_Sizes = [Data_frame[0]['My_main_kill'].sum(), Data_frame[0]['Kill_Steal'].sum(),
                             Data_frame[0]['Regular_kill'].sum(), Data_frame[0]['Solo_kill'].sum()]

    # filter slices with no data
    filtered_labels1 = [label for label, size in zip(type_of_killing_label, type_of_killing_Sizes) if size != 0]
    filtered_sizes1 = [size for size in type_of_killing_Sizes if size != 0]

    fig1 = plt.figure(figsize=(3, 2.5), dpi=100)

    fig1.patch.set_facecolor("#333333")
    plt.rcParams['text.color'] = '#FFFFFF'

    plt.pie(filtered_sizes1, labels=filtered_labels1, autopct='%.0f%%')

    canvas_ks_or_my_kill_or_main_assist = FigureCanvasTkAgg(fig1, master=type_of_killing_frame)
    canvas_ks_or_my_kill_or_main_assist.draw()
    canvas_ks_or_my_kill_or_main_assist.get_tk_widget().pack()

    # death map by kda
    # Death map by kda
    Death_map_frame = tk.LabelFrame(root, text="Death map by KDA - Blue > 2 | Red < 2", bg="#333333", fg="#FFFFFF",
                                    labelanchor="n")
    Death_map_frame.place(x=26, y=427, relx=0.15, rely=0.01)

    image = Data_frame[1]
    size_map = (567, 415)
    resized_image = image.resize(size_map)
    Death_nap_toTK = ImageTk.PhotoImage(resized_image)
    Death_map = tk.Label(Death_map_frame, image=Death_nap_toTK, highlightthickness=0, bd=0)
    Death_map.image = Death_nap_toTK  # Keep a reference to avoid garbage collection
    Death_map.pack()
    Death_map.configure(highlightbackground=Death_map_frame.cget("bg"))


# General info
root = tk.Tk()
root.geometry("175x360")
root.title("League of Legends pro analytics stats")

# style
root.configure(bg="#333333")

# General info

# Summoner name and Region frame
S_R_frame = tk.LabelFrame(root, text="General info", font=("", 10), bg="#333333", fg="#FFFFFF", labelanchor="n")
S_R_frame.place(x=1, y=1, relx=0.004, rely=0.01)

# Summoner name Label
Summoner_name_Label = tk.Label(S_R_frame, text="Summoner name", font=("", 8), bg="#333333", fg="#FFFFFF", width=20)
Summoner_name_Label.grid(row=0, column=0, sticky="n")

# Summoner name Entry
Summoner_name_Entry = tk.Entry(S_R_frame, width=20)
Summoner_name_Entry.grid(row=1, column=0, sticky="n", pady=7)

# tagline name Label
tagline_Label = tk.Label(S_R_frame, text="Tag line", font=("", 8), bg="#333333", fg="#FFFFFF", width=20)
tagline_Label.grid(row=2, column=0, sticky="n")

# tagline name Entry
tagline_Entry = tk.Entry(S_R_frame, width=20)
tagline_Entry.grid(row=3, column=0, sticky="n", pady=7)

# Region Label
Region_Label = tk.Label(S_R_frame, text="Region", font=("", 8), bg="#333333", fg="#FFFFFF", width=20)
Region_Label.grid(row=4, column=0, sticky="n")

# Region combobox
Region_combobox = ttk.Combobox(S_R_frame, values=["EUNE", "EUW", "NA"], width=17)
Region_combobox.current(0)
Region_combobox.grid(row=5, column=0, sticky="n", padx=14, pady=7)

# Type of game Label
Type_Label = tk.Label(S_R_frame, text="Type of Game", font=("", 8), bg="#333333", fg="#FFFFFF", width=20)
Type_Label.grid(row=6, column=0, sticky="n")

# Type combobox
Type_combobox = ttk.Combobox(S_R_frame, values=["ranked", "normal"], width=17)
Type_combobox.current(0)
Type_combobox.grid(row=7, column=0, sticky="n", padx=14, pady=7)

# Number of matches Label
Number_of_matches_Label = tk.Label(S_R_frame, text="Number of matches", font=("", 8), bg="#333333", fg="#FFFFFF",
                                   width=20)
Number_of_matches_Label.grid(row=8, column=0, sticky="n")

# Number of matches spinbox
Number_of_matches_spinbox = tk.Spinbox(S_R_frame, from_=3, to=100, width=19)
Number_of_matches_spinbox.grid(row=9, column=0, sticky="n", padx=14, pady=7)

# analyze button
Analyze_button = tk.Button(S_R_frame, text="Analyze", command=Start_dashboard, width=15)
Analyze_button.grid(row=10, column=0, sticky="n", padx=14, pady=(5, 5))

# Developer name
Dev_name_frame = tk.LabelFrame(root)
Dev_name_frame.place(x=1, y=330, relx=0.004, rely=0.01)

# Developer name Label
Dev_name_Label = tk.Label(Dev_name_frame, text="By Aviv Richman", font=("", 8), bg="#333333", fg="#FFFFFF", width=20)
Dev_name_Label.pack()

root.mainloop()