import os 
os.chdir(r'C:/Users/Powertec/Desktop/Jupyter_Notebook/Spliting_shapefile_polygon') 
import geopandas as gpd 
 
import matplotlib.pyplot as plt 
%matplotlib inline 
 
Shapefile=gpd.read_file('C:/Users/Powertec/Desktop/Jupyter_Notebook/Spliting_shapefil
e_polygon/wgsGNwestern.shp') 
 
shapefile.head() 
 
fig, ax = plt.subplots(figsize = (18,10)) 
shapefile.plot(ax  =ax,  column  =  'DISTRICT_N',legend  =  True,  legend_kwds  = 
{'loc':'upper left'}) 
plt.show() 
 
shapefile.loc[[0]] 
 
len(shapefile) 
 
for i in range(len(shapefile)): 
    print(i) 
15 
 
 
shapefile.loc[0,'DISTRICT_N'] 
 
for i in range(len(shapefile)): 
#    print(i) 
    name = shapefile.loc[i,'DISTRICT_N'] 
 
shapefile.loc[[i]].to_file('C:/Users/Powertec/Desktop/Jupyter_Notebook/Spliting_shapefile
_polygon/Split22/Boundaries/'+name+'.shp') 
 
from glob import glob 
 
shapefile_names=glob('C:/Users/Powertec/Desktop/Jupyter_Notebook/Spliting_shapefile_
polygon/Split22/Boundaries/*.shp') 
 
shapefile_names 
 
for i in shapefile_names: 
    shp = gpd.read_file(i) 
    fig, ax = plt.subplots(figsize = (4,4)) 
    shp.plot(ax=ax) 
    plt.title(shp.loc[0,'DISTRICT_N']) 
    plt.show() 