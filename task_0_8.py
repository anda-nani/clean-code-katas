def convert_to_time(num : int ) -> str:
    
    hours = num // 60
    minutes = num % 60

    h = m = ""  # Initialize empty strings for hour and minute labels
    if hours == 1:  #Determining singular or plural for hours
        h = "hour"
    else:
        h = "hours"

    if minutes == 1: #Determining singular or plural for minutes
        m = "minute"
    else:
        m = "minutes"
        
    return f"{hours} {h}, {minutes} {m}"

print(convert_to_time(133))  