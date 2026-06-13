import pandas as pd
import matplotlib.pyplot as plt

url="https://docs.google.com/spreadsheets/d/1sw4dhR5zb9lB47ZaFQ_rSRpR_niR8E-bkOPbDR6aJL0/export?format=csv"
df=pd.read_csv(url)
record=pd.DataFrame(df,columns=['what is your name ?', 'what is your gender?',
                                'what is your age?','Which social media platforms do you use regularly?',
                                'How many social media accounts do you have?',
                                'How much time do you spend on social media daily?',
                                'During which time are you most active?',
                                'why do you use social media ?',
                                'Do you think social media improves communication?',
                                'Has social media affected your productivity?',
                                'Do you think you spend too much time on social media?',
                                'Are you concerned about privacy on social media?',
                                'What type of information do you usually share?'])
 
print("*"*30)
print("HELLO DEAR!!")
print("*"*30)
print("Here, we have conducted a survey about how people of different age groups are using the different social media sites and to check there mindset that how they think that social media is useful to them or not ")
print("*"*30)
print('displaying the data of survey conducted')
print("*"*30)
while True:
    start=input("press * to proceed:")
    if start=="*":
        print("="*10)
        print('SOCIAL MEDIA SURVEY')
        print('='*10)
        
        break
    else:
        print("wrong input")
    
while True:
    print('1.Dashboard')
    print('2.View Dataset')
    print('3.Dataset Information')
    print('4.Statistical Analysis')
    print('5.Data Visualization')
    print('6.Survey Insights')
    print('7.Generate Report')
    print('8.Export Data')
    print('9.Data Cleaning')
    print('10.exit')
    print('='*10)
    main_choice =int(input('enter your choice(1-10)-'))
    if main_choice ==1:
        print('-'*10)
        print('DASHBROAD')
        print('-'*10)
        total_responses = len(record)
        male_count = (record['what is your gender?'] == 'Male').sum()
        female_count = (record['what is your gender?'] == 'Female').sum()
        popular_platform =record['Which social media platforms do you use regularly?'].mode()[0]
        active_time = record['During which time are you most active?'].mode()[0]
        avg_accounts = record['How many social media accounts do you have?'].mean()
        print("Total Responses           : ",{total_responses})
        print("Male Users                : ",{male_count})
        print("Female Users              : ",{female_count})
        print("Popular Platform          : ",{popular_platform})
        print("Most Active Time          : ",{active_time})
        print("Average No. of Accounts   : ",{avg_accounts})
        print('-'*10)
    elif main_choice ==2:
        print('-'*10)
        print('VIEW DATASET')
        print('-'*10)
        print('1. View First n Records')
        print('2. View Last n Records')
        print('3. View Complete Dataset')
        print('4. Search Record by Name')
        print('5. Filter by Gender')
        print('6. Filter by Age Group')
        print('7. To comeback to the main menu')
        print('-'*10)
        while True:
            record_choice=int(input('enter your choice(1-7)-'))
            if record_choice==1:
                print('-'*10)
                print('View First n Records')
                print('-'*10)
                n=int(input('enter the number of record you want to print-'))
                print(record.head(n))
            elif record_choice==2:
                print('-'*10)
                print('View last n Records')
                print('-'*10)
                m=int(input('enter the number of record you want to print-'))
                print(record.tail(m))
            elif record_choice==3:
                print('-'*10)
                print('View Complete Dataset')
                print('-'*10)
                print(record)
            elif record_choice==4:
                print('-'*10)
                print('Search Record by Name')
                print('-'*10)
                name=input("enter the name whose record you want to display:")
                result = df[df["what is your name ?"].str.contains(name, case=False, na=False)]
                if len(result) > 0:
                    print(result)
                else:
                    print("No record found.")
            elif record_choice==5:
                print('-'*10)
                print('Sorted by Gender')
                print('-'*10)
                sorted_data = record.sort_values(by='what is your gender?')
                print(sorted_data)
            elif record_choice==6:
                print('-'*10)
                print('Sorted by Age Group')       
                print('-'*10)
                sort_data = record.sort_values(by='what is your age?')
                print(sort_data)
            elif record_choice==7:
                break
            else:
                print('WRONG INPUT')
        
    elif main_choice ==3:
        print('-'*10)
        print('DATASET INFORMATION')
        print('-'*10)
        print('1. Number of Responses')
        print('2. Number of Columns')
        print('3. Column Names')
        print('4. Data Types')
        print('5. Missing Values')
        print('6. Duplicate Records')
        print('7. Memory Usage')
        print('8. To comeback to the main menu')
        print('-'*10)
        while True:
            record_choice1=int(input('enter your choice(1-7)-'))
            if record_choice1==1:
                print('-'*10)
                print('Number of Responses')
                print('-'*10)
                print(record.count())
            elif record_choice1==2:
                print('-'*10)
                print('Number of columns')
                print('-'*10)
                print(record.shape[1])
            elif record_choice1==3:
                print('-'*10)
                print('Column Names')
                print('-'*10)
                print(list(record.columns))
            elif record_choice1==4:
                print('-'*10)
                print('Data Type')
                print('-'*10)
                print(type(record.dtype))
            elif record_choice1==5:
                print('-'*10)
                print('Missing Values')
                print('-'*10)
                print(record.isnull().sum())
                total_missing = record.isnull().sum().sum()
                print("Total Missing Values:", total_missing)
            elif record_choice1==6:
                print('-'*10)
                print('Duplicate Values')
                print('-'*10)
                print(record.duplicated().sum())
                total_duplicate =record.duplicated().sum().sum()
                print("Total duplicate Values:", total_duplicate)
            elif record_choice1==7:
                print('-'*10)
                print('Memory usuage')
                print('-'*10)
                print(record.memory_usage(deep=True).sum(),"bytes")
            elif record_choice1==8:
                break
            else:
                print('WRONG INPUT')   
        print('-'*10)
    elif main_choice ==4:
        print('-'*10)
        print('STATISTICAL ANANLYSIS')
        print('-'*10)
        print('1. Gender Distribution')
        print('2. Age Group Distribution')
        print('3. Most Popular Social Media Platform')
        print('4. Average Number of Accounts')
        print('5. Privacy Concern Analysis')
        print('6. Productivity Impact Analysis')
        print('7. To comeback to the main menu')
        print('-'*10)
        while True:
            analysis_choice = int(input("Enter your choice: "))
            if analysis_choice == 1:
                print(record['what is your gender?'].value_counts())
            elif analysis_choice == 2:
                print(record['what is your age?'].value_counts())
            elif analysis_choice == 3:
                platform_count = record['Which social media platforms do you use regularly?'].value_counts()
                print(platform_count)
            elif analysis_choice == 4:
                avg_accounts = record['How many social media accounts do you have?'].mean()
                print("Average Number of Accounts:",avg_accounts)
            elif analysis_choice == 5:
                privacy = record['Are you concerned about privacy on social media?'].value_counts()
                print(privacy)
            elif analysis_choice == 6:
                productivity = record['Has social media affected your productivity?'].value_counts()
                print(productivity)
            elif analysis_choice==7:
                break
            else:
                print('WRONG INPUT')   
        print('-'*10)
        
        
    elif main_choice ==5:
        print('-'*10)
        print('DATA VISUALIZATION')
        print('-'*10)
        print('1.Pie Charts of Gender distribution')
        print('2.Pie Charts of Privacy concern distribution')
        print('3.Bar Charts of Popular Platform')
        print('4.Bar Chart of Most Active time')
        print('5.Histograms of Age distribution')
        print('6.Histogram of Number of Accounts')
        print('7.Scatter Chart of Age vs Time spent')
        print('8. To comeback to the main menu')
        print('-'*10)
        while True:
            visual_choice = int(input("Enter your choice: "))
 
            if visual_choice == 1:
                print('-'*10)
                print('Pie Charts of Gender distribution')
                print('-'*10)
                gender = record['what is your gender?'].value_counts()
                plt.figure(figsize=(6,6))
                plt.pie(gender,labels=gender.index)
                plt.title("Gender Distribution")
                plt.show()
            elif visual_choice == 2:
                print('-'*10)
                print('Pie Charts of Privacy concern distribution')
                print('-'*10)
                privacy = record['Are you concerned about privacy on social media?'].value_counts()
                plt.figure(figsize=(6,6))
                plt.pie(privacy,labels=privacy.index)
                plt.title("Privacy Concern Distribution")
                plt.show()
            elif visual_choice == 3:
                print('-'*10)
                print('Bar Charts of Popular Platform')
                print('-'*10)
                platform = record['Which social media platforms do you use regularly?'].value_counts()
                plt.figure(figsize=(8,5))
                plt.bar(platform.index, platform.values)
                plt.title("Popular Social Media Platforms")
                plt.xlabel("Platform")
                plt.ylabel("Number of Users")
                plt.show()

            elif visual_choice == 4:
                print('-'*10)
                print('Bar Chart of Most Active time')
                print('-'*10)
                active = record['During which time are you most active on social media?'].value_counts()
                plt.figure(figsize=(8,5))
                plt.bar(active.index, active.values)
                plt.title("Most Active Time of Day")
                plt.xlabel("Time")
                plt.ylabel("Number of Users")
                plt.show()
            elif visual_choice == 5:
                print('-'*10)
                print('Histograms of Age distribution')
                print('-'*10)
                age = record['what is your age?'].value_counts()
                plt.figure(figsize=(8,5))
                plt.bar(age.index, age.values)
                plt.title("Age Group Distribution")
                plt.xlabel("Age Group")
                plt.ylabel("Number of Users")
                plt.show()
            elif visual_choice == 6:
                print('-'*10)
                print('Histogram of Number of Accounts')
                print('-'*10)
                accounts = record['How many social media accounts do you have?']
                plt.figure(figsize=(8,5))
                plt.hist(accounts, bins=10)
                plt.title("Number of Accounts Distribution")
                plt.xlabel("Number of Accounts")
                plt.ylabel("Frequency")
                plt.show()
            elif visual_choice == 7:
                print('-'*10)
                print('Scatter Chart of Age vs Time spent')
                print('-'*10)
                age_map = {'Under 18': 17,'18-24': 21,'25-34': 30,'35-44': 40,'45+': 50}
                time_map = {'Less than 1 hour': 0.5,'1-3 hours': 2,'4-6 hours': 5,'More than 6 hours': 7}
                age = record['what is your age?'].replace(age_map)
                time_spent = record['How much time do you spend on social media daily?'].replace(time_map)
                plt.figure(figsize=(8,5))
                plt.scatter(age, time_spent)
                plt.title("Age vs Time Spent on Social Media")
                plt.xlabel("Age")
                plt.ylabel("Hours Spent Per Day")
                plt.show()
            elif visual_choice==8:
                break
            else:
                print("Invalid Choice")
                print('-'*10)
        
    elif main_choice ==6:
        print('-'*10)
        print('DATA INSIGHTS')
        print('-'*10)
        total_responses = len(record)
        popular_platform =record['Which social media platforms do you use regularly?'].mode()[0]
        active_time = record['During which time are you most active?'].mode()[0]
        age_group = record['what is your age?'].mode()[0]
        gender = record['what is your gender?'].mode()[0]
        privacy = record['Are you concerned about privacy on social media?'].mode()[0]
        print("Total Responses Collected :",{total_responses})
        print()
        print(" Most Common Gender      :",{gender})
        print(" Most Common Age Group   :",{age_group})
        print(" Most Popular Platform   :",{popular_platform})
        print(" Most Active Time        :",{active_time})
        print(" Privacy Opinion         :",{privacy})
        print('-'*10)

        
    elif main_choice ==7:
        print('-'*10)
        print('REPORT')
        print('-'*10)
        popular_platform =record['Which social media platforms do you use regularly?'].mode()[0]
        active_time = record['During which time are you most active?'].mode()[0]
        age_group = record['what is your age?'].mode()[0]
        gender = record['what is your gender?'].mode()[0]
        privacy = record['Are you concerned about privacy on social media?'].mode()[0]
        
        print("Total Responses :", len(record))
        print("Total Columns   :", record.shape[1])
        print("Most Popular Platform:",{popular_platform})
        print("Most Common Gender:",{gender})
        print("Most Common Age Group:",{age_group})
        print("Most Active Time:",{active_time})
        print("Privacy Concern:",{privacy})
        print("Conclusion:")
        print("Social media is widely used among respondents.")
        print("Most users have a preferred platform and")
        print("show varying levels of privacy concern.")
        print('-'*10)
        
       
    elif main_choice ==8:
        print('-'*10)
        print('EXPORT DATA')
        print('-'*10)
        print('1. CSV File')
        print('2. Excel File')
        print('3. Cleaned Dataset')
        print('4. Back TO MAIN MENU')
        print('-'*10)
        while True:
            export_choice = int(input("Enter your choice: "))
            if export_choice == 1:
                record.to_csv("social_media_survey.csv", index=False)
                print("CSV File Exported Successfully")
                print('-'*10)

            elif export_choice == 2:
                record.to_excel("social_media_survey_export.xlsx", index=False)
                print("Excel File Exported Successfully")
                print('-'*10)
            elif export_choice == 3:
                cleaned_data = record.drop_duplicates()
                cleaned_data.to_excel("cleaned_social_media_survey.xlsx",index=False)
                print("Cleaned Dataset Exported Successfully")
                print('-'*10)
            elif export_choice==4:
                break
            else:
                print("WRONG INPUT")
        print('-'*10)
        
    elif main_choice ==9:
        print('-'*10)
        print('DATA CLEANING')
        print('-'*10)
        print('1. Missinf Values')
        print('2. To found duplicate record')
        print('3. Clean Dataset')
        print('4. Back TO MAIN MENU')
        print('-'*10)
        while True:
            clean_choice = int(input("Enter Choice: "))
            if clean_choice == 1:
                print("Missing Values:")
                print(record.isnull().sum())

            elif clean_choice == 2:
                duplicates = record.duplicated().sum()
                print("Duplicate Records Found :", duplicates)
                record = record.drop_duplicates()
                print("Duplicates Removed Successfully")

            elif clean_choice == 3:
                record = record.fillna("Not Available")
                print("Missing Values Filled Successfully")
            elif clean_choice == 4:
                break
            else :
                print('WRONG INPUT')
    elif main_choice ==10:
        print('-'*10)
        print('THANK YOU FOR VISITING!!')
        print('-'*10)
        break
    else:
        print("wrong input")

    
