[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Geospatial-AI-DE/geodisasters-py)](https://pypi.org/project/geodisasters)
![GitHub License](https://img.shields.io/github/license/Geospatial-AI-DE/geodisasters-py)
[![Read the Docs](https://img.shields.io/readthedocs/geodisasters)](https://geodisasters.readthedocs.io/en/latest)
[![Tweet Me](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FGeospatial-AI-DE%geodisasters-py)](https://twitter.com/intent/tweet?text=Outstanding:&url=https%3A%2F%2Fgithub.com%2FGeospatial-AI-DE%geodisasters-py)

# Geospatial Disasters API Service
Query broadcasted news related to natural disasters and visualize them using spatial aggregations.

Broadcasted news serves as a valuable source of information for identifying natural disasters globally. Geospatial features represent extracted locations from broadcasted news to identify the locations of these events. Natural disasters such as hurricanes, floods, wildfires, and others are captured and represented as geospatial features.

The service filters thousands of online news sources mentioning occurred natural disasters. We constructed a web mercator spatial grid having a grid size being optimized for geographic visualization. Each grid cell is enriched with a count attribute representing the number of news article related to locations of the corresponding grid cell.

The service uses the impressive data source provided by the [Global Database of Events, Language and Tone (GDELT) Project](https://www.gdeltproject.org/).

Every geospatial result support the GeoJSON and Esri FeatureSet format out of the box. For best performance, the serverless cloud-backend calculate the geospatial aggregations of the last 24 hours between midnight and 1 AM UTC. The serverless functions save these geospatial features since 24th May 2023 and yesterday should be the latest available date.

## Terms of use

We designed the geospatial intelligence API services for research and analysis of geospatial knowledge worldwide. The geospatial datasets and any result being generated by these API services are available for unrestricted use for academic, commercial, or governmental use of any kind.
Redistribution

You may redistribute, republish, and mirror the geospatial datasets in any form. However, any use or redistribution of the geospatial datasets and results must include a citation to GEOINT API services and a link to our website https://geospatial-ai.de.

### Query the news related to natural disasters occurred the last 365 days

![image](https://github.com/user-attachments/assets/d836fc8e-199e-4009-ab68-dd02807d2f2b)

![image](https://github.com/user-attachments/assets/31e6a33d-8381-4956-8d16-e3108547ccac)
