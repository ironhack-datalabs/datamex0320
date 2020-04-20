# Python BI Project

### The following project consists in finding an office space for a Digital Marketing Agency

Main code asks the user for an address or location where they want to search or evaluate if its optimal for their office. 

There are some limitations:
	They want to be sorrounded with Small and Medium Business
	They want to have a coffee shop nearby
	They want to be in San Diego California

### For this project I'm using the following libraries:

+ Pandas
+ Pymongo
+ TQDM
+ Folium
+ Numpy
+ Warnings
+ Regex
+ Pickle
+ OpenCage (for geocode)


### In order to achieve the main result, I'm folowing 6 steps:

#### Step 1
Define client type: as I mentioned in the README ,they want to be sorrounded with Small and Medium Business, they want to have a coffee shop nearby and they want to be in San Diego California

#### Step 2
Correctly query the data I want from Mongo. 

#### Step 3
Transforming data according to client needs.

#### Step 4
Create a new collection with the final DataFrame in MongoCompass so we can add a 2dsphere index. 

#### Step 5
Make geoqueries of the new collection with client input  and display them in a heatmap reflecting the concentration of offices in the selected area.

#### Step 6
Get more information about restaurants in the area and display them with the heatmap mentioned above and marking where the restaurants of coffee shops are. 