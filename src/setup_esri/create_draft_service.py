import arcpy

# define local variables
workspace = 'd:/projects/ProtectedPlanet-ESRI/mxd/'
mapDoc = arcpy.mapping.MapDocument(workspace + 'wdpa.mxd')
con = 'GIS Servers/arcgis on localhost_6080 (admin).ags'
service = 'wdpa'
sddraft = workspace + service + '.sddraft'
sd = workspace + service + '.sd'
summary = 'WDPA'
tags = 'Protected Areas, Conservation, UNEP-WCMC'

# create service definition draft
analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER',
                                          con, True, None, summary, tags)

# stage and upload the service if the sddraft analysis did not contain errors
if analysis['errors'] == {}:
    # Execute StageService
    arcpy.StageService_server(sddraft, sd)
    # Execute UploadServiceDefinition
    arcpy.UploadServiceDefinition_server(sd, con)
else:
    # if the sddraft analysis contained errors, display them
    print analysis['errors']
