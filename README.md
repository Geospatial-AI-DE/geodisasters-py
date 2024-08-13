# geodisasters-py
Query broadcasted news related to natural disasters and visualize them using spatial aggregations.

Broadcasted news serves as a valuable source of information for identifying natural disasters globally. Geospatial features represent extracted locations from broadcasted news to identify the locations of these events. Natural disasters such as hurricanes, floods, wildfires, and others are captured and represented as geospatial features.

The service filters thousands of online news sources mentioning occurred natural disasters. We constructed a web mercator spatial grid having a grid size being optimized for geographic visualization. Each grid cell is enriched with a count attribute representing the number of news article related to locations of the corresponding grid cell.

The service uses the impressive data source provided by the [Global Database of Events, Language and Tone (GDELT) Project](https://www.gdeltproject.org/).

Every geospatial result support the GeoJSON and Esri FeatureSet format out of the box. For best performance, the serverless cloud-backend calculate the geospatial aggregations of the last 24 hours between midnight and 1 AM UTC. The serverless functions save these geospatial features since 24th May 2023 and yesterday should be the latest available date.
