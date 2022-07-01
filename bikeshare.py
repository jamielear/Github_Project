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
    
    city_list = ['chicago','new york city','washington']
    while True:
        city = input("Enter city: ")
        if city in city_list:
            break
        print("Please enter a valid city")    
    
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter month: ")
        if month in month_list:
            break
        print("Please enter a valid month")

    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']
    while True:
        day = input("Enter day: ")
        if day in day_list:
            break
        print("Please enter a valid day")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    #Create day of week column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month as a month
    popular_month = df['month'].mode()[0]
    month_lookup = {
        1 : 'january',
        2 : 'february',
        3 : 'march',
        4 : 'april',
        5 : 'may',
        6 : 'june'
    }
    popular_month = month_lookup[popular_month]
    print('The month with the most journeys was {}'.format(popular_month))

    # Display the most common day of week as a day
    #TO DO days of week properly
    popular_day = df['day'].mode()[0]
    print('The day with the most journeys was {}'.format(popular_day))


    # Display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("This most common departure hour was: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most frequently departed station was {}".format(popular_start_station))
    
    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most frequent destination station was {}".format(popular_end_station))

    # Display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + " to " + df['End Station']
    popular_route = df['route'].mode()[0]
    print("The most frequently used route was {}".format(popular_route))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time was {} minutes".format(travel_time))

    # Display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("Average travel time was {} minutes".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    print("\nThe earliest year of birth is {}".format(int(df['Birth Year'].min())))
    
    print("\nThe latest year of birth is {}".format(int(df['Birth Year'].max())))
    
    print("\nThe most common year of birth is {}".format(int(df['Birth Year'].mode())))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def test():
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print(df['day_of_week'])    

def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
