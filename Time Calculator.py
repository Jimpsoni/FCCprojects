def add_time(start, duration, weekday=None):
    # Get the data we want from the arguments
    hours, minutes, daytime = start.replace(":", " ").split(" ")
    hours, minutes = int(hours), int(minutes)

    add_hours, add_minutes = map(int, duration.split(":"))

    # Change our hour format to 24h/day to handle days better
    hours += 12 if daytime == "PM" else 0
  
    # Add all the hours and minutes
    hours += add_hours
    minutes += add_minutes

    # If minutes go 60 or over, add 1 hour to hours
    if minutes > 59:
      hours += 1
      minutes -= 60

    # If hours go 24 or over, count the days
    days = 0
    if hours > 23:
      # Divide hours by 24 and round down using int()
      days = int(hours / 24)
      
      # Use modulus to get the time of the day
      hours = hours % 24

    # adjust our daytime
    if hours >= 12:
      if hours == 12:
        daytime = "PM"
      else:
        hours -= 12
        daytime = "PM"
    elif hours == 0:
      daytime = "AM"
      hours = 12
    else:
      daytime = "AM"

    # Make minutes to be format XX for example: (06, 24, 09)
    if minutes < 10:
      minutes = f"0{minutes}"

    # Format the string we return
    new_time = f"{hours}:{minutes} {daytime}"

    if weekday is not None:
      # Calculate the weekday
      weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                  "Friday", "Saturday", "Sunday"]
      weekday = weekdays[(weekdays.index(weekday.capitalize()) + days) % 7]

      new_time += f", {weekday}"

    if days != 0:
      if days == 1:
        new_time += " (next day)"
      else:
        new_time += f" ({days} days later)"

    return new_time
