import arcpy 

from arcpy.sa import *     #importing Spatial Analyst tools

baseRaster = Raster('DEM_elkhorn.tif')     #creating the raster object

baseRaster.maximum              #2856.9016113281 - raster object property

baseRaster.minimum              #2174.0673828125 - raster object property

baseRaster.noDataValue          #-3.4028230607370965e+38 - raster object property

baseRaster.uncompressedSize     #62886120 - For 8-bit per pixel data, uncompressed size can be found with this formula:
                                #pixels X * pixels Y * number of bands = uncompressed bytes


slopeRaster = Slope('DEM_elkhorn.tif', 'DEGREE')    #creating a slope raster and evaluate the values calculated

gThan40 = slopeRaster > 40       #evaluating slope to determine the areas greater than 40 degrees.
 
cliff = baseRaster - baseRaster.mean       #using the mean value from the baseRaster for the value to be subtracted from each raster cell value

cliffPresent = GreaterThan(cliff, 160)     #identifying the potential cliffs by selecting all the areas above 160

falconHabitat = gThan40 & cliffPresent     #after analyzed the digital elevation for all requirements, next is comparing both outputs to determine the potential habitat locations

falconHabitat.save('C:\\EsriTraining\\PythonScriptsRaster\\PythRasterAnalysis\\Data\\HabitatOutput.tif')         #making the results permanent by saving the raster





# All the portions of the script are combined into one Python script command

#falconHabitat2 = (Slope(baseRaster, 'DEGREE') > 40) & ((baseRaster-baseRaster.mean) > 160)