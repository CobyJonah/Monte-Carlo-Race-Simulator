from CarParam import Car
from RaceParam import Race

import matplotlib
from matplotlib import pyplot as plt

import pandas as pd
import seaborn as sns
import numpy as np



''' main assumptions
        --> for all our competitors we assume max stuff i.e we assume max fuel 
        --> we input our car parameters lets say for ease of use we just have 2 cars per team

    future stuff
        -->have a dictionary for different track metrics so it sclaes everywhere



    the final plot should  be frequency of finish postion against finishing Position
'''
def TimeConvertQuali(lapData):
    for index, row in lapData.iterrows():
        laptime = str(row['QualiLap'])  # Convert to string

       

        if ':' in laptime:
            minutes, seconds = laptime.split(':')
            if seconds:
                if '.' in seconds:
                    seconds, milliseconds = seconds.split('.')
                    milliseconds = int(milliseconds)
                else:
                    milliseconds = 0
                total_seconds = int(minutes) * 60 + int(seconds)
            else:
                milliseconds = 0
                total_seconds = int(minutes) * 60
        else:
            if laptime.endswith('.'):
                laptime += '000'  # Add three zeros for missing milliseconds
            total_seconds, milliseconds = map(int, laptime.split('.'))

        # Update the DataFrame with the converted time values
        lapData.at[index, 'QualiLap'] = (total_seconds + milliseconds / 1000) 

def TimeConvertTheoretical(lapData):
    for index, row in lapData.iterrows():
        laptime = str(row['TheoreticalBest'])  # Convert to string

       

        if ':' in laptime:
            minutes, seconds = laptime.split(':')
            if seconds:
                if '.' in seconds:
                    seconds, milliseconds = seconds.split('.')
                    milliseconds = int(milliseconds)
                else:
                    milliseconds = 0
                total_seconds = int(minutes) * 60 + int(seconds)
            else:
                milliseconds = 0
                total_seconds = int(minutes) * 60
        else:
            if laptime.endswith('.'):
                laptime += '000'  # Add three zeros for missing milliseconds
            total_seconds, milliseconds = map(int, laptime.split('.'))

        # Update the DataFrame with the converted time values
        lapData.at[index, 'TheoreticalBest'] = (total_seconds + milliseconds / 1000) 

def DataClean(dataframe):
    TimeConvertQuali(dataframe)
    TimeConvertTheoretical(dataframe)

def PitlaneSet(dataframe):
    Grid = []
    for i in range(20):
        driverNumber = dataframe.loc[i,'DriverNumber']
        quali_lap = dataframe.loc[i, 'QualiLap']
        theoretical_best = dataframe.loc[i, 'TheoreticalBest']
        car = Car(500, 20, 1.8, 2.8, quali_lap, theoretical_best)
        car.driverName = str(driverNumber)
        Grid.append(car)

    return Grid

# def RunSimulation(Array,times,drivertrack):
#     Race_1 = Race(10,Array,drivertrack)
#     for i in range(times):
        
        
#         return Race_1.RaceStart()

def FinalStart(Array):
    sorted_array = sorted(Array, key=lambda car: car.Qualitime)
    return sorted_array



def searchGrid(array, number, load):
    for car in array:
        if car.driverName == number:
            car.fuelLoad = load
            break
        
    return array




def main():
    # obj = Car(55,589,0.2,128.892,128.709)
    # print(obj.LaptimeGenerator())
    # print(PitlaneSet())
    df = pd.read_csv('SilverstoneTest.csv')

    DataClean(df)

    InitialGrid = PitlaneSet(df)
    InitialGrid = FinalStart(InitialGrid)
    
    TeamDriver = str(input('Enter Driver Number :'))
    Car_Fuel = float(input('Enter your Fuel Load (no units) :'))
    NumberOfSimulations = int(input('Enter Number of Simulations :'))


    finish_positions = []  # List to store the finishing positions


    InitialGrid = searchGrid(InitialGrid, TeamDriver, Car_Fuel)
    for i in range(0, NumberOfSimulations):
        Race_1 = Race(10, InitialGrid, TeamDriver)
        finish_position = Race_1.RaceStart()  # Call the RaceStart method, not finishingPosition()
        finish_positions.append(finish_position)  # Add the finishing position to the list
        InitialGrid = PitlaneSet(df)
        InitialGrid = FinalStart(InitialGrid)        


    
    plt.hist(finish_positions, bins=max(finish_positions)-min(finish_positions)+1, align='left')
    plt.xlabel('Finishing Position')
    plt.ylabel('Frequency')
    plt.title('Frequency of Finishing Positions')
    plt.show()
    print(InitialGrid[0].fuelLoad)

    


    



    # plt.figure(figsize=(8, 6))
    # sns.distplot(finish_positions, bins=max(finish_positions)-min(finish_positions)+1, kde=True, hist=True)
    # plt.xlabel('Finishing Position')
    # plt.ylabel('Frequency')
    # plt.title('Frequency of Finishing Positions')
    # plt.show()


    # # Calculate mean and standard deviation of finish positions
    # mean = np.mean(finish_positions)
    # std = np.std(finish_positions)

    # # Generate a normal distribution based on the calculated mean and standard deviation
    # normal_dist = np.random.normal(mean, std, NumberOfSimulations)

    # # Plot the normal distribution
    # plt.hist(normal_dist, bins=20, density=True)
    # plt.xlabel('Finishing Position')
    # plt.ylabel('Density')
    # plt.title('Normal Distribution of Finishing Positions')
    # plt.show()



if __name__ == '__main__':
    main()







'''problems 

    cars arent generating lap times


'''