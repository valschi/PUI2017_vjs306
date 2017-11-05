__Assignment 1__

For HW7 we worked in a team: Matt, Kent, Tarek and myself

We reviewed the test suggestions we each got from our reviewers, they included Chi-square (for Valeria's and Kent's), Z-test (Matt), and T-test (for Valeria).

After doing some dialogue between the four of us we concluded a T test was a valid test. This because the IV is categorical and the DV is continous, specifically the IV is dichotomus. We discussed how we could also use an ANOVA test. Originally, we were thinking of doing a one sided T test, but we concluded hat we didn't have strong indication that the significance was going to go in any particular direction, so we then used a two sided T test therefore, we modified our H0 formula to better reflect this. 

Kent found the scipy test specifically for the two sided T test which receives two arrays as input, so we prepared the data for it. 

The results allowed us to reject our H0 that there is no difference in the average age in male riders vs average age of female riders.

_Authorea link:_

https://www.authorea.com/users/175471/articles/210788-hw7-working-title#

__Assignment 2__

During class we were able to complete Prof. Ho's instructions in Carto. For reference the code that we used..

SELECT CDB_TransformToWebmercator( 
  			CDB_LatLng(start_station_latitude,start_station_longitude)) as the_geom_webmercator,  
       MIN(cartodb_id) as cartodb_id,   /* needed to plot, because we are using a set we need a min, if we where using sy, an average, we wouldnt need it*/   
       AVG(tripduration) as ta  
FROM citibike  
WHERE ST_DWithin (CDB_LatLng(start_station_latitude,start_station_longitude)::geography,  
                  CDB_LatLng(40.7577, -73.9857)::geography,  
                  500)  
GROUP BY start_station_id,  
start_station_latitude, start_station_longitude
