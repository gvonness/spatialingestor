formats_data = [
    {
        'type': 'KML',
        'description': 'View a map of this dataset in web and desktop spatial data tools including Google Earth',
        'name': '{package_title} KML',
        'url': '{ws_addr}wms?request=GetMap&layers={layer}&bbox={bbox_obj_minx},{bbox_obj_miny},{bbox_obj_maxx},{bbox_obj_maxy}&width=512&height=512&format={format}',
        'format': 'kml'
    },
    {
        'type': 'IMAGE/PNG',
        'description': 'View overview image of this dataset',
        'name': '{package_title} Preview Image',
        'url': '{ws_addr}wms?request=GetMap&layers={layer}&bbox={bbox_obj_minx},{bbox_obj_miny},{bbox_obj_maxx},{bbox_obj_maxy}&width=512&height=512&format={format}',
        'format': 'png'
    },
    {
        'type': 'WMS',
        'description': 'View the data in this dataset online via an online map',
        'name': '{package_title} - Preview this Dataset (WMS)',
        'url': '{ws_addr}wms?request=GetCapabilities',
        'wms_layer': '{layer}',
        'format': 'wms'
    },
    {
        'type': 'WFS',
        'description': 'WFS API Link for use in Desktop GIS tools',
        'name': '{package_title} Web Feature Service API Link',
        'url': '{ws_addr}wfs',
        'wfs_layer': '{layer}',
        'format': 'wfs'
    },
    {
        'type': 'CSV',
        'description': 'For summary of the objects/data in this collection',
        'name': '{package_title} CSV',
        'url': '{ws_addr}wfs?request=GetFeature&typeName={layer}&outputFormat={format}',
        'format': 'csv'
    },
    {
        'type': 'JSON',
        'description': 'For use in web-based data visualisation of this collection',
        'name': '{package_title} GeoJSON',
        'url': '{ws_addr}wfs?request=GetFeature&typeName={layer}&outputFormat={format}',
        'format': 'json'
    },
    {
        'type': 'GEOJSON',
        'description': 'For use in web-based data visualisation of this collection',
        'name': '{package_title} GeoJSON',
        'url': '{ws_addr}wfs?request=GetFeature&typeName={layer}&outputFormat={format}',
        'format': 'geojson'
    }
]