import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input

    while True:
      city = input("\nWhich city would you like to filter by? New York , Chicago or Washington?\n").lower().title()
      if city not in ('New York', 'Chicago', 'Washington'):
        print("Sorry, Please Try again.")
        continue
      else:
        break

    # TO DO: Asks user to specify which period to filter by   
    while True:
      period = input("\nWould you like to filter the data by month, day, or not at all?\n").lower()
      if period not in ('month', 'day', 'not at all'):
        print("Sorry, Please Try again.")
        continue
      else:
        break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'none' if you do not want to filter \n").lower()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'none'):
        print("Sorry, Please Try again.")
        continue
      else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich day would you like to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'none' if you do not want to filter.\n").lower()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'none'):
        print("Sorry, please Try again.")
        continue
      else:
        break
    print('-'*40)
    return city, period, month, day


def load_data(city, period, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #Loading data for the specified city in a Pandas DataFrame

    df = pd.read_csv(CITY_DATA[city.lower()])
    
    #Converting the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extracting the month, day and hours of the week from Start Time

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month']==month]
        
    #Filtering by day (if applicable)
    if day != 'none':
        df = df[df['day']==day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The Most Common Month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print("The Most Common Day of Week: ", most_common_day)

    # TO DO: display the most common start hour
    
    most_common_starthr = df['Start Hour'].mode()[0]
    print("The Most Common Start Hour: ", most_common_starthr)

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combo_station = df.groupby(['Start Station', 'End Station']).count()
    print("Most common trip from start to end : ", frequent_combo_station.idxmax()[0][0], " and ", frequent_combo_station.idxmax()[0][1])

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600
    print("Total Travel Time = ", total_travel_time, "hrs")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/3600
    print("Mean Travel Time = ", mean_travel_time, "hrs")

    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nCounts of gender: ", gender_count)
        print()
    else:
        print("\nCounts of gender: No data available for this month\n")

    # TO DO: Display earliest year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print("\nEarliest Year of Birth: ", earliest_birth_year)
        print()
        
    except KeyError:
        print("\nEarliest Year of Birth: No data available for this month\n")
    # TO DO: Display most recent year of birth   
    try:
        most_recent_birth_year = df['Birth Year'].max()
        print("\nMost Recent Year of Birth: ", most_recent_birth_year)
        print()

    except KeyError:
        print("\nMost Recent Year of Birth: No data available for this month\n")

    # TO DO: Display most common year of birth    
    try:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("\nMost Common Year of Birth: ", most_common_birth_year)
        print()
    except KeyError:
        print("\nMost Common Year of Birth: No data available for this month\n")

    print('-'*40)


def main():

    while True:
        city, period, month, day = get_filters()
        df = load_data(city, period, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        step=1
        start=0
        end=5

        while(step ==1):
            step=int(input('\nWould you like to view individual trip data? \nType 1 or 2 \n1:True\n2:False\n'))
            while((step != 1) and (step!=2)):
                step=int(input('\nPlease enter Try again: '))
            print(df.iloc[start:end])
            start+=5
            end+=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
