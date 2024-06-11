# 1) Step 1: Make your script dynamic

import arcpy

# Set environments
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\Data\SanJuan.gdb"

# Create list of feature classes to Buffer
bufferList = [arcpy.GetParameterAsText(0), arcpy.GetParameterAsText(1)]     # ["Lakes", "Stream"]

# Initialize a new Python list of feature classes to be Unioned together
unionList = []
for fc in bufferList:
    # Buffer each feature class and dissolve any overlapping polygons
    arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "ALL")
    # Add each buffer feature class to a list of feature classes to Union
    unionList.append(fc + "Buffer")
    
# Union the buffered feature classes
arcpy.Union_analysis(unionList, arcpy.GetParameterAsText(2))    # (unionList, "WaterBuffers")



#Note: The output feature class must have Output specified as the direction.

#The difference between the Feature Class and the Feature Layer data type is that:
#--> the Feature Class only allows you to browse to a location whereas
#--> the Feature Layer additionally allows you to select a layer from your map
