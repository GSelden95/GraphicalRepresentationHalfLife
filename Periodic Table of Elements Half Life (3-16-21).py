#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from skimage import io


# In[ ]:


#Make sure you put the correct directory name in here or else the .csv won't read!!!
periodic_table = pd.read_csv("~/Periodic Table With Half Life.csv", encoding = 'unicode_escape')


# In[ ]:


#This is the csv file that was read, it includes a half life column. The half life unit of measurement is just a "time" variable 
#(for example Radon is in days but other elements may be in years.)
periodic_table


# In[ ]:


periodic_table.rename(columns = {'half-life': 'Half-Life', 'lifetime': 'Lifetime'}, inplace=True)


# In[ ]:


element_list = periodic_table['name'].tolist()


# In[ ]:


#This 'while' loop asks you to input the number of atoms you're looking to start out with. It only accepts integers.
while True:
    print("Input the number of atoms of a particular element you are looking to seek the half life for.\n")
    try:
        amount = int(input())
        print(f"\nAwesome! You chose {amount} atom(s)!\n")
        break
    except ValueError:
        print("\nThat was not an integer. Please type an integer:\n")


# In[ ]:


#A picture of all the radioactive elements. 
#Again, make sure you put in the corrrect directory here or else the code won't load properly.
radioactive_image = io.imread("~/Radioactive Elements.png")
print("Here is a list of all the radioactive elements to choose from. You can save the image to get a better look at which\n ones are which.\n")
io.imshow(radioactive_image)


# In[ ]:


#Here is a list of all the elements to work with. 
print('Here\'s a list of all the periodic table of elements to choose from:\n')
for i in periodic_table['name']:
    print(i)


# In[ ]:


#This 'while' loop asks you to input an element. It will only accept the elements that are spelled correctly in 'element list'.
#If you input a float or integer, it will ask you to try again.
#If you spell the element incorrectly, it will ask you to try again.
while True:
    element = input('Input the element you want to represent the half life of over the time span of Earth\'s age!\n')
    if element in element_list:
        print(f"\nAwesome! You chose {element}\n")
        break
    else:
        print("\nThat is not an existing element in the periodic table. Please try again:\n")


# In[ ]:


#I'm going to make an index match scenario where it's just a table of the element and it's half life status

#Creating an empty dataframe
half_life_table = pd.DataFrame()

#Naming the columns
half_life_table['Element'] = []
half_life_table['Half Life'] = []


# In[ ]:


#Assigning the new columns
half_life_table['Element'] = pd.Series(periodic_table['name'])
half_life_table['Half Life'] = pd.Series(periodic_table['Half-Life'])


# In[ ]:


half_life_table


# In[ ]:


#DON'T RUN THIS LINE OF CODE IF YOU DON'T WANT THE INDEX/MATCH .CSV FILE!!!!
half_life_table.to_csv("/Users/geoffdselden/Desktop/OUTCOMES:FINDING A JOB!!!/Periodic Table Half Life Project (3-7-23)/half life table.csv")


# In[ ]:


#Okay so now we've located the element you wanted. It drops all the other elements with this command
index_match_first = half_life_table.where(half_life_table['Element'] == element).dropna()


# In[ ]:


#We reset the index, this is important for later
index_match_first.reset_index(drop=True, inplace=True)


# In[ ]:


index_match_first


# In[ ]:


#Half Life 

def half_life_function():

    #If the index/match has nothing in the table, there is no information and it asks you to try again (hence len == 0 means there was no half life information available.)
    if len(index_match_first) == 0:
        print('No information for the half life of this element. Try another element.\n')
        
    #Remember how we reset the index? That's because now index 0 is the element we've locked in on. This is checking for stability. 
    #If it's stable it will print the following message: 
    elif index_match_first['Half Life'][0] == 'Stable':
        print('Element is stable. No graphical representation available.\n')
        
    #This is if it does have a graphical information available!
    else:
        
        while True:
            #Asks you to input how much time you want to graph the function over
            print("Input a number for how big you want the x-axis of your graph to be")
            try:
                x_ending = float(input())
                print(f"Nice! You chose {x_ending} amount of time!")
                
                #Converts the half life into a float
                half_life_var = float(index_match_first['Half Life'])

                #This creates the x axis with the amount of time you chose. 
                time = np.linspace(0, x_ending)
                
                #This is the amount of atoms remaining formula!
                quantity_remaining = amount *((1/2)**(time/half_life_var))
                
                fig = plt.figure()

                #Naming our Axes!
                plt.xlabel('Time') 
                plt.ylabel('Quantity') 
  
                # displaying the title
                plt.title("Quantity of Isotope Over Time")

            
                plt.plot(time, quantity_remaining, 'r')

                plt.show()
                
                break
            #This prints if you didn't enter a float for the amount of time you want to graph the function over.
            except ValueError:
                print("\nThat was not a number. Please type a number:\n")
                
                


# In[ ]:


half_life_function()

