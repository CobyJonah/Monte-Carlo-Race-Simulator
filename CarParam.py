import random




#this file contains parameters for a standard GB3 car
#LapTime = ForecastedPrimeTime + Random + TyreDeg + FuelAdj.

#fuel tank assume is 55l
#extra urban  is 7.7l per 100km

#fuel burn per silverstone lap = 0.4536072857

#track length =  5.89100371 kilometers

#https://www.focusrsbuildlist.com/index.php/information/specification

# Weight including the driver of the MSV-022 is 598kg


#assuming density for fuel is 0.75 kg/litre




class Car:

    

    def __init__(self, weight, fuelLoad, FuelEffect, FuelConsumption, Qualitime, TheoreticalBest):
        self.TrackPosition = 0
        self.LapNumber = 0
        self.CarNumber = 0
        self.maxLaps = 0
        self.driverName = ''
        self.CarInfront = None
        self.CarBehind = None
        self.Overtake_Success = False
        self.LostPosition = False
        self.weight = weight
        self.fuelLoad = fuelLoad
        self.FuelEffect = FuelEffect
        self.FuelConsumption = FuelConsumption
        self.Qualitime = Qualitime
        self.TheoreticalBest = TheoreticalBest
        self.laptime = 0
    
    
    

    def GridSlot(self,ahead,behind):
        CarInfront = ahead
        # in cases like P1  Carinfront should be set to null in the arguments   
        CarBehind = behind
        #in cases like P20 Carbehind should be set to null in the arguement

    def TyreModel(self):
        # Calculate the quadratic tyre degradation penalty
        max_laps = 50  # Adjust the number of laps at which degradation reaches its maximum
        lap_ratio = self.LapNumber / max_laps
        tyre_deg_penalty = lap_ratio ** 2  # Quadratic penalty initially

        if lap_ratio > 1.0:
            tyre_deg_penalty = (1 / lap_ratio) ** 2  # Quadratic penalty worsens after certain point
        
        return tyre_deg_penalty


    def FuelLoadPenalty(self):
        max_fuel_load = self.fuelLoad  # Maximum fuel load at the start of the race
        # min_fuel_load = 3.0  # Minimum fuel load at which penalty reaches its minimum
        # fuel_load_ratio = (self.fuelLoad - min_fuel_load) / (max_fuel_load - min_fuel_load)
        # fuel_load_penalty = (1- fuel_load_ratio) * 0.3  # Linear penalty based on fuel load ratio
        fuel_load_penalty = self.FuelEffect * self.fuelLoad

        return fuel_load_penalty
        #revise fuel model Lower fuel should be better 

        #revise this and include fuel effect attribute.... multiuplu effect by kg and add ?

    # def FuelLoadPenalty(self):
    #     max_fuel_load = self.fuelLoad  # Maximum fuel load at the start of the race
    #     min_fuel_load = 3.0  # Minimum fuel load at which penalty reaches its minimum
    #     fuel_load_ratio = (self.fuelLoad - min_fuel_load) / (max_fuel_load - min_fuel_load)
    #     fuel_load_penalty = 1 - fuel_load_ratio ** 2  # quadratic penalty based on fuel load ratio

    #     return fuel_load_penalty


    def FuelModel(self,state):
        if state == "normal_use":
            self.FuelConsumption = self.FuelConsumption  # Set fuel consumption to the original value
        elif state == "lift_and_coast":
            self.FuelConsumption = self.FuelConsumption * 0.7  # Decrease fuel consumption by 30%
    def Overtake(self):
        
        #for an overtake to happen there must be a few conditions met 

        # there should be a minimum and maximum threshold for it to take placce i.e 0.2s a lap faster than car in front min  and 0.5 max  = garantueed

        # a sucessful overtake should yield a time penalty for both the overtaker and overtaken 

        if self.CarInfront is not None:
            time_difference = self.CarInfront.Laptime - self.Laptime

        if time_difference >= 0.2:
            success_probability = 0.78
        elif 0 < time_difference < 0.2:
            success_probability = time_difference / 0.2 * 0.78
        else:
            success_probability = 0

        if random.random() < success_probability:
            self.CarInfront.Laptime += 0.3  # Apply penalty to the car in front
            self.Laptime += 0.3  # Apply penalty to our own lap time
            self.Overtake_Success = True  # Set Overtake_Success attribute to True if successful

    def laptimeGenerator(self):

        '''Our lap time gen should be a function of this equation

            laptime  = Qualitime + Random deviation of Theoretical best and their average lap + a tyre deg penalty and a fuel load time penalty 
            this all gets fuel corrected
        
        '''

        deviation = random.uniform(-0.5, 1.5)  # Random deviation between -0.2 and 0.3
        avg_lap = (self.Qualitime + self.TheoreticalBest) / 2.0
        tyre_deg_penalty = self.TyreModel()  # Calculate the tyre degradation penalty based on your tire model
        fuel_load_penalty = self.FuelLoadPenalty()  # Calculate the fuel load penalty based on fuel load and consumption rate

        self.laptime = (avg_lap + deviation) + tyre_deg_penalty + fuel_load_penalty

        # Apply fuel correction



        

        #fuel correct formula = time (s) - (fueleffect(s/kg) * fuelload in kg)
        # fuel_correction = self.fuelLoad * self.FuelEffect
        # self.laptime -= fuel_correction
        self.fuelLoad -= self.FuelConsumption  # Update fuel load after each lap

        
        return self.laptime

    # def laptimeGenerator(self):
    #     deviation = random.uniform(-0.5, 1.5)  # Random deviation between -0.5 and 1.5
    #     avg_lap = (self.Qualitime + self.TheoreticalBest) / 2.0
    #     tyre_deg_penalty = self.TyreModel()  # Calculate the tyre degradation penalty based on your tire model
    #     fuel_load_penalty = self.FuelLoadPenalty()  # Calculate the fuel load penalty based on fuel load and consumption rate

    #     self.laptime = (avg_lap + deviation) + tyre_deg_penalty + fuel_load_penalty

    #     if self.fuelLoad <= 0:
    #         self.fuelLoad = 0
    #         self.laptime = 0

    #     else:
    #         fuel_used = self.FuelConsumption * self.LapNumber  # Calculate the fuel used based on fuel consumption rate and lap number
    #         self.fuelLoad -= fuel_used

    #         if self.fuelLoad < 0:
    #             self.fuelLoad = 0

    #         # Fuel correction formula: time (s) - (fueleffect(s/kg) * fuelload in kg)
    #         fuel_correction = self.fuelLoad * self.FuelEffect
    #         self.laptime -= fuel_correction

    #     return self.laptime



        