import pandas as pd
import matplotlib.pyplot as plt

url="https://docs.google.com/spreadsheets/d/18jS3wrf2yXZSa1TzcKQnSfKRJL5VFFVXAU4KtgxFjxw/export?format=csv"
df=pd.read_csv(url)
tab=pd.DataFrame(df,columns=['name','gender','age','use sites or not?',
                            'name of sites used devices used',
                           'number of accounts','most active hours',
                            'time spend','hours of a week you spend',
                           'information shared','use to connect to family',
                            'use to connect to the friends',
                           'use for reasearch', 'us to find jobs',
                            'use for enternment','others uses',
                            'always used sites',
                           'oftenly uses sites','rarely used sites',
                            'never used sites'])
 
print("****************************************************")
print("HELLO DEAR!!")
print("****************************************************")
print("Here, we have conducted a survey about how people of different age groups are using the different social media sites and to check there mindset that how they think that social media is useful to them or not ")
print("****************************************************")
print('displaying the data of survey conducted')
print('===============')
while True:
    ch=input("press * to proceed:")
    if ch=="*":
        print('To know the dataframe statics menu enter the following choice')
        print('1.display whole data')
        print('2.display all column values')
        print('3.display the indexes')
        print('4.displays the shape')
        print('5. display the dimension')
        print('6.displaythe datatype of all column')
        print('7.display the size')
        print('8.exit')
        print("9.for more options")
        print('===============')
        break
    else:
        print("wrong input")
    
while True:
    ch1=int(input('enter your choice(1-8)-'))
    if ch1==1:
        print(tab)
    elif ch1==2:
       print(tab.columns)
    elif ch1==3:
       print(tab.index)
    elif ch1==4:
        print(tab.shape)
    elif ch1==5:
       print(tab.ndim)
    elif ch1==6:
       print(tab.dtypes)
    elif ch1==7:
       print(tab.size)
       
    elif ch1==8:
        print("thank you for visiting!!")
        exit()
    elif ch1==9:
        print('===============')    
        print('displaying record menu')
        print('1.top 5 record ')
        print('2.bottom record')
        print('3.specific number of records from the tops')
        print('4.specific number of records from the bottom')
        print('5.exit')
        print("6.for more options")
        break
    else:
        print("wrong input")
while True:
    ch2=int(input('enter your choice(1-6)-'))
    if ch2==1:
       print(tab.head())
    elif ch2==2:
       print(tab.tail())
    elif ch2==3:
       n=int(input('enter no. of record you want to display from the top - '))
       print(tab.head(n))
    elif ch2==4:
       n=int(input('enter no. of record you want to display from the bottom -'))
       print(tab.tail(n))
    elif ch2==5:
        print("thank you for visiting!!")
        exit()
    elif ch2==6:
        print('===============')
        print('displaying visualization menu')
        print('1.bar plot--> no. of accounts')
        print('2.bar plot--> always used sites ')
        print('3.bar plot--> oftenly used sites ')
        print('4.bar plot--> rarely used sites ')
        print('5.bar plot--> never used sites ')
        print('6.exit')
        print('===============')
        break
    else:
        print("wrong input")
            

while True:
    ch3=int(input('enterchoice-'))
    if ch3==1:
        x=tab.name
        y=tab['number of accounts']
        plt.bar(x,y,width=.5,color=['b','r','k','c','c','g','y','m','gold','silver','brown','k'])
        plt.ylabel('no. of accounts')
        plt.xlabel('name')
        plt.title('survey on no. of accounts')
        plt.show()
    elif ch3==2:
        y =tab['always used sites'].value_counts().plot(kind='bar')
        plt.xlabel('Name of sites')
        plt.ylabel('count of sites')
        plt.title('always used sites')
        plt.show()
    elif ch3==3:
        y =tab['oftenly uses sites'].value_counts().plot(kind='bar')
        plt.xlabel('Name of sites')
        plt.ylabel('count of sites')
        plt.title('oftenly uses sites')
        plt.show()                                
    elif ch3==4:
        y =tab['rarely used sites'].value_counts().plot(kind='bar')
        plt.xlabel('Name of sites')
        plt.ylabel('count of sites')
        plt.title('rarely used sites')
        plt.show()                                    
    elif ch3==5:
        y =tab['never used sites'].value_counts().plot(kind='bar')
        plt.xlabel('Name of sites')
        plt.ylabel('count of sites')
        plt.title('never used sites')
        plt.show()
    elif ch==6:
        print("TANK YOU FOR VISITING !!")
        exit()
 
 
