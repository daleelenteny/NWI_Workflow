# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2022-07-27 16:03:34
"""
import arcpy
from sys import argv

def NWIBackUp(Output_Shapefile_Name="NBE_Jun", Local_Backup_Folder="C:\\WorkSpace\\NWI\\Local Project Folder Connections\\NWI_Shapefile_Backups_Local", Network_Backup_Folder="Y:\\NWI_Backup\\Dale_Elenteny\\Network Project Folder Connections\\NWI_Shapefile_Backups_Network", Segments_Feature_Class="Berrien_Springs_NewSegments"):  # Backup with shapefile

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx")

    # Process: Feature Class To Feature Class (Feature Class To Feature Class) (conversion)
    Output_Feature_Class = arcpy.conversion.FeatureClassToFeatureClass(in_features=Segments_Feature_Class, out_path="C:\\Users\\delenteny\\Documents\\ArcGIS\\Projects\\Dale_NWI\\Dale_NWI.gdb", out_name=Output_Shapefile_Name, where_clause="", field_mapping="OBJECTID_1 \"OBJECTID_1\" true true false 4 Long 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,OBJECTID_1,-1,-1;County \"County\" true true false 50 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,County,0,50;Name \"Name\" true true false 50 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,Name,0,50;ACRES \"ACRES\" true true false 8 Double 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,ACRES,-1,-1;Shape_Leng \"Shape_Leng\" true true false 8 Double 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,Shape_Leng,-1,-1;ATTRIBUTE \"ATTRIBUTE\" true true false 20 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,ATTRIBUTE,0,20;COMMENTS \"COMMENTS\" true true false 50 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,COMMENTS,0,50;FIELD_VER \"FIELD_VER\" true true false 1 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,FIELD_VER,0,1;MULTIPART \"MULTIPART\" true true false 10 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,MULTIPART,0,10;QAQC_CODE \"QAQC_CODE\" true true false 10 Text 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,QAQC_CODE,0,10;Shape_Length \"Shape_Length\" false true true 8 Double 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,Shape_Length,-1,-1;Shape_Area \"Shape_Area\" false true true 8 Double 0 0,First,#,C:\\WorkSpace\\NWI\\SW_MI_NWI\\Dale\\SW_MI_NWI\\PI\\Galien.gdb\\Galien_Vector\\Galien_Segments,Shape_Area,-1,-1", config_keyword="")[0]

    # Process: Feature Class To Shapefile (2) (Feature Class To Shapefile) (conversion)
    Updated_Output_Folder_2_ = arcpy.conversion.FeatureClassToShapefile(Input_Features=[Output_Feature_Class], Output_Folder=Network_Backup_Folder)[0]

    # Process: Feature Class To Shapefile (Feature Class To Shapefile) (conversion)
    if Updated_Output_Folder_2_:
        Updated_Output_Folder = arcpy.conversion.FeatureClassToShapefile(Input_Features=[Output_Feature_Class], Output_Folder=Local_Backup_Folder)[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\delenteny\Documents\ArcGIS\Projects\Dale_NWI\Dale_NWI.gdb", workspace=r"C:\Users\delenteny\Documents\ArcGIS\Projects\Dale_NWI\Dale_NWI.gdb"):
        NWIBackUp(*argv[1:])
