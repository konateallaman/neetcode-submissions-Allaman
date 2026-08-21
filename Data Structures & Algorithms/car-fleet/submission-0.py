class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        I sort the cars from closest to the target to farthest,
         calculate each car's arrival time,
          and create a new fleet whenever its arrival time is greater than the fleet ahead
        '''
        list_Of_Cars=list(zip(position,speed)) #pair position and speed for each car
        list_Of_Cars.sort(reverse=True)
        Total_Fleet=0 #total fleets
        previous_Time= 0 #the arrival time of the fleet immediately ahead
        for position,speed in list_Of_Cars:
            current_Time=(target - position)/speed #arrival time for each car
            if current_Time>previous_Time:
                Total_Fleet += 1  #create a new fleet only and only if current_Time>previous time
                previous_Time=current_Time
        return Total_Fleet

        