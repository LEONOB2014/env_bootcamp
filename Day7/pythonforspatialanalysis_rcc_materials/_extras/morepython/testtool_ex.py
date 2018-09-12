# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# testtool2.py
# Created on: 2017-04-21 11:16:02.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Local variables:
tracts = "tabletesting.gdb/tracts"
major_roads = "tabletesting.gdb/major_roads"
major_roads_Buffer = "tabletesting.gdb/major_roads_Buffer"
tracts_Clip = "tabletesting.gdb/tracts_Clip"

Delete_succeeded = "false"
Delete_succeeded__2_ = "false"

inputdata = arcpy.GetParameterAsText(0)

if arcpy.Exists(major_roads_Buffer):
    # Process: Delete
    arcpy.Delete_management(major_roads_Buffer, "FeatureClass")
if arcpy.Exists(tracts_Clip):
    # Process: Delete (2)
    arcpy.Delete_management(tracts_Clip, "FeatureClass")

# Process: Buffer
arcpy.Buffer_analysis(major_roads, major_roads_Buffer, inputdata + " Miles", "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Clip
arcpy.Clip_analysis(tracts, major_roads_Buffer, tracts_Clip, "")

