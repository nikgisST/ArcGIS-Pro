import arcpy

# Set geoprocessing environments
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create list of feature classes in SanJuan.gdb
fcList = arcpy.ListFeatureClasses()    #If you do not provide any parameters,the function will return a Python list for all feature classes

# Create a loop to buffer Lakes and Streams
bufferList = []
for fc in fcList:
    if fc == "Lakes" or fc == "Streams":         # Geoprocessing tools in ArcToolbox are functions in ArcPy-Buffer function
        #LakesBuffer and StreamsBuffer
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "ALL")     # line_side="", line_end_type= "", dissolve_option = "ALL"
        bufferList.append(fc + "Buffer")

# arcpy.Union_analysis(in_features, out_feature_class)
arcpy.Union_analysis(bufferList, "WaterBuffers")
