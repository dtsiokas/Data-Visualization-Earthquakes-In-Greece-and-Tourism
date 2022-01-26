# Earthquakes-In-Greece-and-Tourism

In this project, I visualized the relationship between Earthquakes in Greece and Tourism to see if I could gain any insights on the data as well as see if the natural disasters have had any effect on whether or not people would still visit this beautiful country. I analyzed over one century of data which accounts for every earthquake that has ever occured in Greece from 1900 to 2020. I also compared the data to tourist arrivals in Greece from 1995 to 2019. 

Firstly, I created a scatter plot to with 'Years' on the x-axis and "Magnitute in Richter Scale" on the y-axis to see all the data points. From observing this visual, we can see that although the frequency of earthquakes appears to be increasing, the severity of the extreme points on the Richter scale appear to be decreasing. It is important to note, however, that it is possible Greece did not have an advanced earthquake detection system as it does today and therefore were not able to detect lower magnitude earthquakes. Still, the severity of the earthquakes magnitudes appear to be trending downward.

Here is the code and output:

![scatter plot](https://user-images.githubusercontent.com/71915516/151227702-712df5c4-8ad7-4022-851f-4d883d2db1fe.png)



I then created a line chart to see if any additional insights could be picked up from the data points. However, it showed the exact same movement as the scatter plot. 

Here is the code and output:

![line chart](https://user-images.githubusercontent.com/71915516/151227731-4288b057-9503-4c4a-b614-776af4ab279c.png)


Next I created a bar chart visualizing tourist arrivals in Greece from 1995 to 2019. It is clear from this visual that Greece has been experiencing exponential growth in the tourism indistry. It is important to note that the dataset had corrupted data from the years 2007 to 2012, however, those points do not appear to change the overall visualized trend in the data. 

Here is the code and output:

![Bar chart](https://user-images.githubusercontent.com/71915516/151227916-4c327f9f-94ae-4995-ba9f-a5f75c6d588f.png)



Now this was the most intriguing; I created a histogram to visualize how many earthquakes occured for each month and was shocked by the result. Each month is numerical (January = 1, February = 2 ... December = 12) and is located on the x-axis while the y-axis was the count of months where an earthquake has occured. the amount of earthquakes DOUBLE during the months of January and December, the end and beginning of a year. How is this possible? Could it have something to do with the earth's position in orbit? Why is it that this time of year there are double the amount of earthquakes as there are in every other month? Take a look and see for yourself:

![histogram](https://user-images.githubusercontent.com/71915516/151227945-d006bf97-7069-4fd8-a769-46f31702656c.png)

I also created a pie chart which shows all years with international arrivals in Greece. You can see which years have more than others but a pie chart is never the best way to visualize data and was created "for the memes" as they say. I will exclude this code and output but you can view it in the .py file. I will, however, include the code and output for the entire dashboard showing all visualizations here:

![code for dashboard](https://user-images.githubusercontent.com/71915516/151229870-d9f93dee-276a-458e-bb7e-a925e2eaead5.png)


![dashboard output](https://user-images.githubusercontent.com/71915516/151229485-347f079b-8818-4fd4-b85d-b5c95fd9a0cc.png)

In conclusion, it appears that the severity of earthquakes in greece has been decreasing. It also appears that the frequency of earthquakes seems to be increasing, while at the same time tourist arrivals are increasing, meaning that the earthquakes have not had an impact on tourism at all. The finding of earthquakes doubling in frequency during December and January also could have an effect, as the tourism season is from May to September which conveniently dodges those more dnagerous months. A more thorough statistical analysis is needed to determine a more accurate conclusion but since this was a data visualization project, I can cocnlude that based on these findings tourism is not impacted by earthquakes in Greece.
