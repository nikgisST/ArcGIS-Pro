# 1) Step 1: Union feature classes

import arcpy

# Set geoprocessing environments
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create Python list of treatment area feature classes
treatmentList = ["RoadBuffers", "WaterBuffers"]

# Union treatment areas
arcpy.Union_analysis(treatmentList,"NonChemical")



# 2) Step 2: Use the Python window to select treatment sites

arcpy.env.workspace = r"C:\EsriTraining\PythonGP\PythonGP\Data\SanJuan.gdb"
arcpy.management.SelectLayerByLocation("Invasive Plants",'INTERSECT', 'NonChemical')



# 3) Step 3: Calculate attributes for the treatment sites

with arcpy.da.UpdateCursor("Invasive Plants", "TREATMENT") as cursor:
    for row in cursor:
        row[0] = "NON-CHEMICAL"
        cursor.updateRow(row)
