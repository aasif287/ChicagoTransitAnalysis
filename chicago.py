#for part 1
#gets the necessary libaries 
import pandas as pd
#reads csv file
df = pd.read_csv("CTA_-_Ridership_-__L__Station_Entries_-_Daily_Totals.csv" )

# a. What's the busiest station (most boardings) in Chicago?
#counts the station with the most amount of boardings 
busiest_station = df.groupby('stationname')['rides'].sum().idxmax()
busiest_station_boardings = df.groupby('stationname')['rides'].sum().max()
print(f"a. The busiest station in Chicago is {busiest_station} with {busiest_station_boardings} boardings.")

# Convert the 'date' column to a datetime format
df['date'] = pd.to_datetime(df['date'])

# b. What was the busiest day in these 20 years?
#counts and gets the busiest date based on amount of rides
busiest_day = df.groupby('date')['rides'].sum().idxmax()
print(f"b. The busiest day in these 20 years was on {busiest_day.strftime('%m/%d/%Y')}.")

# c. What was the least busy weekday?
#counts and gets the least amount of rides for each weekday
weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df['weekday_name'] = df['date'].dt.dayofweek.map(lambda x: weekday_names[x])
least_busy_weekday = df.groupby('weekday_name')['rides'].sum().idxmin()
print(f"c. The least busy weekday is {least_busy_weekday}.")

#part 2
#imports necessary Libraries 
import pandas as pd
#reads csv files
df_tenth = pd.read_csv('BARTtenth.csv')
df_hundreth = pd.read_csv('BARThundredth.csv')

# Convert the hour value to time format
def convert_to_am_pm(hour):
    if hour == 0:
        return "12:00 AM"
    elif 1 <= hour < 12:
        return f"{hour}:00 AM"
    elif hour == 12:
        return "12:00 PM"
    else:
        return f"{hour - 12}:00 PM"

# a. What's the busiest hour in the 1/10th sample data (BARTtenth.csv)?
#writes function to get the busiest hour from counting the individuals taking a ride
busiest_hour_tenth = df_tenth.groupby('Hour')['Count'].sum().idxmax()
busiest_hour_tenth_formatted = convert_to_am_pm(busiest_hour_tenth)
print(f"a. The busiest hour in the 1/10th sample data (BARTtenth.csv) is {busiest_hour_tenth_formatted}.")

# b. What's the busiest hour in the 1/100th sample data (BARThundreth.csv)?
#writes function to get the busiest hour from counting the individuals taking a ride 
busiest_hour_hundreth = df_hundreth.groupby('Hour')['Count'].sum().idxmax()
busiest_hour_hundreth_formatted = convert_to_am_pm(busiest_hour_hundreth)
print(f"b. The busiest hour in the 1/100th sample data (BARThundredth.csv) is {busiest_hour_hundreth_formatted}.")
