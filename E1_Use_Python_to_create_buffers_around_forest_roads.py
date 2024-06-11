import arcpy


# Set geoprocessing environments

arcpy.env.workspace = r"C:\EsriTraining\PythonGP\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True


# Set parameters used to join the BufferDistance table to the Roads feature class

#arcpy.Usage("JoinField_management")  
#JoinField_management(in_data, in_field, join_table, join_field, {fields, fields...},)

inFeatures = "Roads"
inField = "ROUTE_TYPE"
joinTable = "BufferDistance"
joinField = "ROUTE_TYPE"


# Join table to feature class
arcpy.JoinField_management(inFeatures, inField, joinTable, joinField)


# Set parameters used to buffer Roads feature class
# arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field) ---> inFeatures variable previously set references the Roads features class - reuse it in Buffer statement

outBuffers = "RoadBuffers"
buffField = "DISTANCE"


# Buffer the roads based on DISTANCE attribute
arcpy.Buffer_analysis(inFeatures, outBuffers, buffField)