# NASA-Earth-Data

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/NASA-Earth-Data/blob/main/nasa_earth_data.ipynb)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

This repository provides a comprehensive list of NASA's Earth science data products available for research and analysis. The data is managed and maintained by NASA's Earth Science Data Systems ([ESDS](https://www.earthdata.nasa.gov/esds)) Program, which ensures the accessibility and usability of the data.

You can access the NASA Earth science data through the official Earthdata website at [earthdata.nasa.gov](https://earthdata.nasa.gov). To download and access the data, you will need to create an Earthdata login. You can register for an account at [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov).

The repository includes a curated list of NASA Earth science data products compiled using the Python package called [earthaccess](https://github.com/nsidc/earthaccess). The list is available in two formats: Tab Separated Values (TSV) and JSON.

## Usage

To access the list of NASA Earth data, you can use the following links:

- [nasa_earth_data.tsv](https://github.com/opengeos/NASA-Earth-Data/blob/main/nasa_earth_data.tsv): This is the TSV file format, suitable for reading data into Pandas DataFrame or other tabular data processing tools.
- [nasa_earth_data.json](https://github.com/opengeos/NASA-Earth-Data/blob/main/nasa_earth_data.json): This is the JSON file format, which provides a structured representation of the data.

Here is an example of how to read the TSV file into a Pandas DataFrame using Python:

```python
import pandas as pd

url = 'https://github.com/opengeos/NASA-Earth-Data/raw/main/nasa_earth_data.tsv'
df = pd.read_csv(url, sep='\t')
df.head()
```

There are over 9,000 NASA Earth data products available. The list is being updated daily. Feel free to explore the data and utilize it for your research, analysis, and Earth science projects.

## Related Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/giswqs/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/giswqs/aws-open-data-geo)
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/giswqs/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/giswqs/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/giswqs/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/giswqs/Earth-Engine-Catalog)
- A list of geospatial datasets on NASA's Common Metadata Repository (CMR): [NASA-CMR-STAC](https://github.com/giswqs/NASA-CMR-STAC)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs)
