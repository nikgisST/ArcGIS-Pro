import arcpy 
from arcpy.sa import *     #importing Spatial Analyst tools

# Load the raster data
baseRaster = Raster('DEM_elkhorn.tif')     #creating the raster object

# Get the raster properties
baseRaster.maximum              #2856.9016113281 - raster object property
baseRaster.minimum              #2174.0673828125
baseRaster.noDataValue          #-3.4028230607370965e+38
baseRaster.uncompressedSize     #62886120 - For 8-bit per pixel data, uncompressed size can be found with this formula:
                                #pixels X * pixels Y * number of bands = uncompressed bytes

# Create the slope raster
slopeRaster = Slope('DEM_elkhorn.tif', 'DEGREE')    #creating a slope raster and evaluate the values calculated

# Identify areas with slope greater than 40 degrees
gThan40 = slopeRaster > 40                           #evaluating slope to determine the areas greater than 40 degrees.
 
# Subtract the mean value from each cell value
cliff = baseRaster - baseRaster.mean             #using the mean value from the baseRaster for the value to be subtracted from each raster cell value

# Identify areas where the value is greater than 160
cliffPresent = GreaterThan(cliff, 160)                 #identifying the potential cliffs by selecting all the areas above 160

# Combine both criteria to identify potential falcon habitats
falconHabitat = gThan40 & cliffPresent                             #after analyzed the digital elevation for all requirements, next is comparing both outputs to determine the potential habitat locations

# Save the resulting raster to a file
falconHabitat.save('C:\\EsriTraining\\PythonScriptsRaster\\PythRasterAnalysis\\Data\\HabitatOutput.tif')         #making the results permanent by saving the raster




#You have now created all the portions of the script that you will need for the analysis. Can you combine them into one Python script command?
#--> You can keep the raster object that you created in place for the solution

falconHabitat2 = (Slope(baseRaster, 'DEGREE') > 40) & ((baseRaster-baseRaster.mean) > 160)
