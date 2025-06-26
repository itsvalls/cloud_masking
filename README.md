#  TerraScan — Cloud Masking Module
This module enables **cloud and shadow masking** for Sentinel-2 Level-2A imagery using Google Earth Engine (GEE). It clips the satellite image to a specified **Area of Interest (AOI)** and **time range**, then exports a clean `.tif` file with selected bands (NIR, Red, Green).
Useful for preprocessing satellite images before NDVI, NDWI, and land-use change detection.
---
##  Features

-  Cloud & shadow removal using SCL (Scene Classification Layer)
-  Select AOI and date range dynamically
-  Export cloud-free `.tif` to Google Drive
- Uses Sentinel-2 SR imagery (`COPERNICUS/S2_SR`)
- Reusable function — easily integrates into your pipeline or API

---

## 🛠 Prerequisites

1. **Google Earth Engine Account**  
   Sign up: [https://signup.earthengine.google.com/](https://signup.earthengine.google.com/)

2. **Python Packages**  
   Install the required libraries:

   ```bash
   pip install earthengine-api geemap
   
