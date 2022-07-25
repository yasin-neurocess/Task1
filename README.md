# Task1
Interview for Software Engineer position of Neurocess Inc. in July 2022 : Task1

Task1:
    In this part, you need to change some values according to the given hierarchy. You need to read a pickle file (“data.pkl”) which is provided. This pickle file contains a 3 column dataframe in which these columns are “c1” , “c2” and “task”.The last column, whose name is “task” contains 0 and 1 values. These 0 and 1 values are placed as a group which is shown in the table. ( You just need to work on last column whose name is “task”) 
    We expect you to edit these values on a given data frame according to given figures. After editing these values, you need to count word repetition. Lastly, you need to show these counted values on a bar graph. The x-axis must be counted names and the y-axis must be the count values of these names. 

Solution: 
    The following python libraries were used to solve this problem;
    
        -Pandas
        -NumPy
        -Matplotlib
        -pickle
        -json
        
The data frame was read with the help of pandas library. Then, the data read from the names.json file was replaced with 1 values according to the written condition statement. By keeping the counter, we transferred the counter value, which we recorded, to the array created with the help of NumPy library. Finally, we visualized the requested data using the Matplotlib library.

Also you can find the .png file for the asked bar plot in this repo.
