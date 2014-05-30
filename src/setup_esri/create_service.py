import arcpy

workspace = 'd:/projects/ProtectedPlanet-ESRI/lib/'
mapDoc = arcpy.mapping.MapDocument(workspace + 'wdpa.mxd')
con = 'GIS Servers/arcgis on localhost_6080 (admin).ags'
service = 'wdpa'
sddraft = workspace + service + '.sddraft'
sd = workspace + service + '.sd'
summary = 'WDPA'
tags = 'Protected Areas, Conservation, UNEP-WCMC'

# Analyse service definition draft
analysis = arcpy.mapping.AnalyzeForSD(sddraft)
if analysis['errors'] == {}:
    arcpy.UploadServiceDefinition_server(sd, con)
else:
    print analysis['errors']
