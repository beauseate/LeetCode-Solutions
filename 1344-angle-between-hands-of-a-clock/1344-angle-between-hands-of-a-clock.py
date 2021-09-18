class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        minuteAngle = minutes * 6
        hourAngle = (hour + (minutes/60)) * 30
        
        if hour == 12:
            hourAngle -= 360
        
        retAngle = abs(hourAngle - minuteAngle)
        
        if retAngle >= 180:
            retAngle = 360 - retAngle
        
        return retAngle
        