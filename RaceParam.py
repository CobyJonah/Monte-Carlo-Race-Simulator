from CarParam import Car

class Race:

    def __init__(self, TotalLaps, StartingGrid, Driver):
        self.TotalLaps = TotalLaps
        # self.TrackLength = TrackLength
        self.StartingGrid = StartingGrid
        self.finishingPosition = None
        self.Driver = Driver

        self.lapsDone  = 0
        # premise is that a Race is represented by a Array that comprises of Car Objects. Based off laptimes of each car Overtakes will happen Occordingly
        #This Class should just act as a Race manager 

    def GridPrep(self):
        num_cars = len(self.StartingGrid)

        for i, car in enumerate(self.StartingGrid):
            if i == 0:
                car.CarInfront = None
                car.CarBehind = self.StartingGrid[i + 1] if num_cars > 1 else None
            elif i == num_cars - 1:
                car.CarInfront = self.StartingGrid[i - 1]
                car.CarBehind = None
            else:
                car.CarInfront = self.StartingGrid[i - 1]
                car.CarBehind = self.StartingGrid[i + 1]

            car.LapNumber = 1  # Set the initial LapNumber to 1 for each car

        if num_cars > 1:
            self.StartingGrid[-1].CarBehind = None








    # def GridPrep(self):
    #     num_cars = len(self.StartingGrid)

    #     for i, car in enumerate(self.StartingGrid):
    #         if i == 0:
    #             car.CarInfront = None
    #             car.CarBehind = self.StartingGrid[i + 1] if num_cars > 1 else None
    #         elif i == num_cars - 1:
    #             car.CarInfront = self.StartingGrid[i - 1]
    #             car.CarBehind = None
    #         else:
    #             car.CarInfront = self.StartingGrid[i - 1]
    #             car.CarBehind = self.StartingGrid[i + 1]

    #     if num_cars > 1:
    #         self.StartingGrid[-1].CarBehind = None

    # def RaceStart(self):

    #     # go through each car and set the max laps for the race
    #     for car in self.StartingGrid:
    #         car.maxLaps = self.TotalLaps

    #         # Race simulation loop
    #     for lap in range(1, self.TotalLaps + 1):
    #         for i in range(len(self.StartingGrid)):
    #             current_car = self.StartingGrid[i]
    #             if current_car.LapNumber < lap:
    #                 continue  # Skip cars that have already completed the current lap

    #             # Check for overtakes
    #             if current_car.CarInfront is not None:
    #                 if current_car.Laptime < current_car.CarInfront.Laptime:
    #                     current_car.Overtake()  # Successful overtake

    #                     # Update the car positions in the StartingGrid array
    #                     self.StartingGrid[i], self.StartingGrid[i-1] = self.StartingGrid[i-1], self.StartingGrid[i]

    #     # Determine finishing positions based on the final lap number and track position
    #     self.finishingPosition = sorted(self.StartingGrid, key=lambda car: (car.LapNumber, car.TrackPosition))

    #     for position, car in enumerate(self.finishingPosition, start=1):
    #         if car.driverName == self.Driver:
    #             return position

    #     return None  # If the specified driver is not found in the finishing positions

    def RaceStart(self):
        # go through each car and set the max laps for the race
        for car in self.StartingGrid:
            car.maxLaps = self.TotalLaps

        lapsDone = 0  # Initialize the lapsDone attribute

        # Race simulation loop
        for lap in range(1, self.TotalLaps + 1):
            for i in range(len(self.StartingGrid)):
                current_car = self.StartingGrid[i]
                if current_car.LapNumber < lap:
                    continue  # Skip cars that have already completed the current lap

                # Check for overtakes
                if current_car.CarInfront is not None:
                    if current_car.Laptime < current_car.CarInfront.Laptime:
                        current_car.Overtake()  # Successful overtake

                        # Update the car positions in the StartingGrid array
                        self.StartingGrid[i], self.StartingGrid[i-1] = self.StartingGrid[i-1], self.StartingGrid[i]

                current_car.LapNumber += 1  # Increment the LapNumber attribute
                lapsDone += 1  # Increment the lapsDone attribute

        # Determine finishing positions based on the final lap number and track position
        self.finishingPosition = sorted(self.StartingGrid, key=lambda car: (car.LapNumber, car.TrackPosition))

        for position, car in enumerate(self.finishingPosition, start=1):
            if car.driverName == self.Driver:
                return position

        return None  # If the specified driver is not found in the finishing positions
    def RaceStart(self):
        # Go through each car and set the max laps for the race
        for car in self.StartingGrid:
            car.maxLaps = self.TotalLaps

        lapsDone = 0  # Initialize the lapsDone attribute

        # Race simulation loop
        for lap in range(1, self.TotalLaps + 1):
            for i in range(len(self.StartingGrid)):
                current_car = self.StartingGrid[i]
                if current_car.LapNumber < lap:
                    continue  # Skip cars that have already completed the current lap

                # Check for overtakes
                if current_car.CarInfront is not None:
                    if current_car.Laptime < current_car.CarInfront.Laptime:
                        current_car.Overtake()  # Successful overtake

                        # Update the car positions in the StartingGrid array
                        self.StartingGrid[i], self.StartingGrid[i-1] = self.StartingGrid[i-1], self.StartingGrid[i]

                current_car.LapNumber += 1  # Increment the LapNumber attribute
                lapsDone += 1  # Increment the lapsDone attribute

        # Determine finishing positions based on the final lap number and track position
        self.finishingPosition = sorted(self.StartingGrid, key=lambda car: (car.LapNumber, car.TrackPosition))

        for position, car in enumerate(self.finishingPosition, start=1):
            if car.driverName == self.Driver:
                return position

        return None  # If the specified driver is not found in the finishing positions
    def RaceStart(self):
    # Go through each car and set the max laps for the race
        for car in self.StartingGrid:
            car.maxLaps = self.TotalLaps

        # Race simulation loop
        for lap in range(1, self.TotalLaps + 1):
            for car in self.StartingGrid:
                car.Laptime = car.laptimeGenerator()  # Assign a new lap time for each car
                car.fuelLoad -= car.FuelConsumption

            for i in range(len(self.StartingGrid)):
                current_car = self.StartingGrid[i]

                # Check for overtakes
                if current_car.CarInfront is not None:
                    if current_car.Laptime < current_car.CarInfront.Laptime:
                        current_car.Overtake()  # Successful overtake
                        if current_car.Overtake_Success:
                            # Update the car positions in the StartingGrid array
                            self.StartingGrid[i], self.StartingGrid[i-1] = self.StartingGrid[i-1], self.StartingGrid[i]
                            
        




        # Determine finishing positions based on the final lap number and track position
        self.finishingPosition = sorted(self.StartingGrid, key=lambda car: (car.Laptime, car.TrackPosition))

        for car in self.StartingGrid:
            car.Overtake_Success = False  # Reset the Overtake_Success attribute for the next lap

        positions = []
        for position, car in enumerate(self.finishingPosition, start=1):
            positions.append(f"{position}. {car.driverName}")
        print(f"Lap {lap}: {positions}")

        for position, car in enumerate(self.finishingPosition, start=1):
            if car.driverName == self.Driver:
                return position
            
        

        return None  # If the specified driver is not found in the finishing positions


    # def RaceStart(self):
    #     # Go through each car and set the max laps for the race
    #     for car in self.StartingGrid:
    #         car.maxLaps = self.TotalLaps

    #     # Race simulation loop
    #     for lap in range(1, self.TotalLaps + 1):
    #         for car in self.StartingGrid:
    #             car.Laptime = car.laptimeGenerator()  # Assign a new lap time for each car
    #             car.fuelLoad -= car.FuelConsumption

    #             # # Check if the car ran out of fuel
    #             # if car.fuelLoad < 0:
    #             #     car.fuelLoad = 0
    #             #     car.LapNumber = self.TotalLaps + 1  # Set LapNumber to a value greater than TotalLaps

    #         for i in range(len(self.StartingGrid)):
    #             current_car = self.StartingGrid[i]

    #             # Check for overtakes
    #             if current_car.CarInfront is not None:
    #                 if current_car.Laptime < current_car.CarInfront.Laptime:
    #                     current_car.Overtake()  # Successful overtake
    #                     if current_car.Overtake_Success:
    #                         # Update the car positions in the StartingGrid array
    #                         self.StartingGrid[i], self.StartingGrid[i-1] = self.StartingGrid[i-1], self.StartingGrid[i]
        
    #     # Determine finishing positions based on the final lap number and track position
    #     self.finishingPosition = sorted(self.StartingGrid, key=lambda car: (car.LapNumber, car.TrackPosition))

    #     for car in self.StartingGrid:
    #         car.Overtake_Success = False  # Reset the Overtake_Success attribute for the next lap

    #     positions = []
    #     for position, car in enumerate(self.finishingPosition, start=1):
    #         positions.append(f"{position}. {car.driverName}")
    #     print(f"Finishing Positions: {positions}")

    #     for position, car in enumerate(self.finishingPosition, start=1):
    #         if car.driverName == self.Driver:
    #             return position

    #     return None  # If the specified driver is not found in the finishing positions
