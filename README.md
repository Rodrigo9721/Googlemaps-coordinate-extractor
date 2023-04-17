# Googlemaps-coordinate-extractor
Extract the names, coordinates and other relevant information from pins inside google maps - Progresol example
1. Set up:
 - Set the appropiate headers for requests
 - Get the start and the end of the page source that contains the pins inside the interactive map
2. Extraction:
 - Extract the subset of the page source delimited by start and end
 - Make a dictionary and clean the extracted data
3. Save:
 - You can save everything inside one json file or pandas dataframe, or store them individually. 
