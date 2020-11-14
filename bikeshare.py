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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\n which city you want to explore, chicago, new york City or washington:").strip().lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("\nInvalid inputs. Please try again")
            continue
        else:
            print("\nThe city you want to explore the data is: '{}'".format(city.title()))
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nPick a month from january to june to filter by: ").strip().lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print ("\nInvalid month input. Please try again")
            continue
        else:
            print ("\nThe month you want to explore the data is: '{}'".format(month.title()))
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nThe day of the week you want to explore the data is: ").strip().lower()
        if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("\nInvalid day input. Please try again")
            continue
        else:
            print("\nThe day you want to explore the data is: '{}'". format(day.title()))
            break

    print("\nYour selected filtering paramters are '{}' as city, '{}' as month, and '{}' as day". format(city.title(), month.title(), day.title()))
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'].dt.month
    df['Day of Week']=df['Start Time'].dt.weekday_name
    df['Hour']=df['Start Time'].dt.hour
    #Refrence https://knowledge.udacity.com/questions/373307#
    if month != 'all':
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month)+1
        df=df[df['Month'] == month]
    if day != 'all':
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        df=df[df['Day of Week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    check_month = {'1': 'january', '2': 'february','3': 'march','4': 'april','5': 'may','6': 'june','7': 'july','8': 'auguest', '9': 'september', '10': 'october', '11': 'november', '12': 'december'}
    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    month_in_string = check_month[str(popular_month)]
    print('Based on the selected filter, the most popular month is: ', month_in_string)

    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('Based on the selected filter, the most popular day of week is: ' + str(popular_day) + '.')

    # TO DO: display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Based on the selected filter, the most popular start time is: ' + str(popular_hour) + '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print ("\nThe most commonly used start station is: '{}'".format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print ("\nThe most commonly used end station is: '{}'".format(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    combination_station = str(df['Start-End Combination']
                                            .mode()[0])

    print ("\nThe most frenquent combination of start station and end station trip is: '{}'".format(combination_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    ttt = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print('The total travel time is : ' +
          ttt + '.')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mtt = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print("The mean travel time is : " +
          mtt + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print (user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("\nNo data of genders were found")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_popular_birth = df['Birth Year'].mode()[0]

        print("\nThe oldest person to ride was born in: '{}'".format(int(earliest_birth)))
        print("\nThe youngest person to ride was born in: '{}'".format(int(most_recent_birth)))
        print("\nThe most common year of birth is: '{}'".format(int(most_popular_birth)))
    else:
        print ("\nNo data of 'Birth Year' were found")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Refrence for raw_data https://knowledge.udacity.com/questions/307041 Give users a chance to display raw data#

def raw_data(df):
    i=0

    rawdata_input = input("\nDo you want to have raw data displayed? Enter 'yes' or 'no'\n").strip().lower()
    while rawdata_input in ['yes','y','yeah'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        rawdata_input = input("\nDo you want to see more raw data? Enter 'yes' or 'no'\n").strip().lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
