import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

class Visualization():
    def __init__(self, main_folder_path: str,
                 planets_file_name: str,
                 spaceship_file_name: str,
                 people_file_name: str):
        self.path = main_folder_path
        self.planets_file = self.path + "/" + planets_file_name
        self.spaceship_file = self.path + "/" + spaceship_file_name
        self.people_file = self.path + "/" + people_file_name
        self.planets = pd.DataFrame()
        self.people = pd.DataFrame()
        self.spacecrafts = pd.DataFrame()
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.colors = sns.color_palette("husl", 8)
        self.markers = ['o', 's', 'D', '^', 'v', 'x', '*', '+']
        self.line_styles = ['-', '--', '-.', ':']

    def read_data(self):
        self.planets = pd.read_csv(self.planets_file)
        self.spacecrafts = pd.read_csv(self.spaceship_file)
        self.people = pd.read_csv(self.people_file)

    def plot_planets(self):
        plt.pie(self.planets['Population'], labels=self.planets['Name']) # type: ignore
        plt.title("Population Distribution")
        circle = plt.Circle((0, 0), 0.8, color="white") # type: ignore
        plt.gca().add_artist(circle)
        plt.legend(title="Planets", loc="center")
        plt.show()
        
    def plot_spacecrafts(self):
        
        (self.spacecrafts['Status'].value_counts()).plot(kind="pie")
        plt.title("Spacecraft Status Distribution")
        circle = plt.Circle((0, 0), 0.8, color="white") # type: ignore
        plt.gca().add_artist(circle)
        plt.legend(title="Spacecrafts", loc="center")
        plt.show()