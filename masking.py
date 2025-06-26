import ee

def get_cloud_free_image(aoi_coords, start_date, end_date, export_name):
    """
    Applies cloud & shadow masking on Sentinel-2 L2A imagery and exports to Google Drive"""
    ee.Initialize()
    aoi = ee.Geometry.Polygon(aoi_coords)


    s2 = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(aoi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30))

    def mask_clouds(image):
        scl = image.select('SCL')
        mask = scl.neq(3).And(scl.neq(8)).And(scl.neq(9))
        return image.updateMask(mask)

    clean = s2.map(mask_clouds).median().clip(aoi)

    bands = clean.select(['B8', 'B4', 'B3'])  
    task = ee.batch.Export.image.toDrive(
        image=bands,
        description=export_name,
        folder='GEE_Exports',
        fileNamePrefix=export_name,
        region=aoi,
        scale=10,
        maxPixels=1e9
    )

    task.start()
    return f" Export started for {export_name}"
