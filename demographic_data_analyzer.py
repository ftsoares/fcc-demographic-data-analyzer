import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv",sep = ',',header = 0)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male','age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    education = df['education'].value_counts()
    percentage_bachelors = education['Bachelors'] / education.sum() * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = education[['Bachelors','Masters','Doctorate']].sum()
    lower_education = education.drop(['Bachelors','Masters','Doctorate']).sum()

    # percentage with salary >50K
    edu_up_50k = df.loc[df['salary'] == '>50K','education'].value_counts()
    higher_education_rich = edu_up_50k[['Bachelors','Masters','Doctorate']].sum() / higher_education * 100
    lower_education_rich = edu_up_50k.drop(['Bachelors','Masters','Doctorate']).sum() / lower_education * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week'] == min_work_hours).sum()

    rich_percentage = (df.loc[df['hours-per-week'] == min_work_hours, 'salary'] == '>50K').sum() / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    country_count_up_50k = df.loc[df['salary'] == '>50K','native-country'].value_counts()
    country_up_50k_percentage = (country_count_up_50k / country_count) * 100

    highest_earning_country_percentage = country_up_50k_percentage.max()
    highest_earning_country = country_up_50k_percentage[country_up_50k_percentage == highest_earning_country_percentage].index[0]

    # Identify the most popular occupation for those who earn >50K in India.
    index_serie = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    top_IN_occupation = df.loc[index_serie,'occupation'].value_counts().index[0]

    # Round `all` decimals to the nearest tenth
    average_age_men = round(average_age_men,1)
    percentage_bachelors = round(percentage_bachelors,1)
    higher_education = round(higher_education,1)
    lower_education = round(lower_education,1)
    higher_education_rich = round(higher_education_rich,1)
    lower_education_rich = round(lower_education_rich,1)
    min_work_hours = round(min_work_hours,1)
    num_min_workers = round(num_min_workers,1)
    rich_percentage = round(rich_percentage,1)
    highest_earning_country_percentage = round(highest_earning_country_percentage,1)
    
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
