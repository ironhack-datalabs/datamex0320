#deleting duplicate
#This entry is not really a duplicate as the car model is different is more an error of VIN classification. In my design I used the VIN as Key field so when I added the data I had to change the duplicated VIN as my VIN column only allowed unique values.

DELETE FROM Cars WHERE vin = 'DAM41UDN3CHU2WVF6-1';

