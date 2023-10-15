'''  Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:
           city
     Field      type
      ID        number
      CITY      varchar(21)
      STATE     varcahr(22)
      LAT_N     number
      LONG_W    number  
      
'''
SELECT count(city)-count(Distinct city) FROM STATION;
