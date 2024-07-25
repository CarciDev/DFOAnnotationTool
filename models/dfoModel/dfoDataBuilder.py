"""
This class will allow to create a custom data model to capture custom attributes requested by DFO. 

Idea: 

The class will be used when exporting data from the annotation step in label-studio. Once the user requests to export the data,
the data will be a member of this class. Then, each annotation will be analyzed and the custom attributes will be generated and stored in the class.

This class is split into two components. It will hold (the custom attributes):

1) A 'Project Label-Studio JSON' file, which is created at time of instantiation (ensures the freshest data is always available).
2) A list of tasks, which contain a list of annotations and contains custom attributes as:
    - 'geoBox': The georeferenced bounding geometry of the annotation [x1,y1,x2,y2].
    - 'jgwPath': The path to the JGW file.
    - 'flag': A flag to indicate if the annotation is within an intersecting region.

    
The idea of organizing our data into two sections is that label-studio can always parse the 'Project Label-Studio JSON' file, 
and the custom attributes can be used to store the custom attributes. Down the line, this class will be able to update the custom data, given a project update.

In the future, this class will have the ability to modify the custom attributes of the annotations, and export as csv:
- Image ID
- Shape type
- Animal
- Species
- Length / Width
- User Confidence Score
- Model's Confidence Score
- Image Path
- Comment
"""
import json
from label_studio_sdk.client import LabelStudio
import requests

class DfoDataBuilder:
    def exportData(self):
        """
        Pipe and Filter Pattern:
        
        Initial Condition: Data fetched from the API.
        Final Condition: Modified data exported as a JSON file, georeferenced.

        Export the data from the annotation step in label-studio.
        1. Fetch the current project data from the API.
        2. Parse the data and store it in the class.
        3. Generate the custom attributes for each annotation.
        4. Store the custom attributes in the class.
        5. Export the data as a json.

        todo: create annotationConflictModel.py
        """    
        
        # 1:
        self.projectData = self.fetchCurrentProjectData()
        print(self.projectData)
        # 2 + 3:
        pixelCoordinatesAnnotationDictionary = self.parseProjectData(self.projectData)
        # 3 + 4:
        print(json.dumps(pixelCoordinatesAnnotationDictionary, indent=4))
        self.geoReferencedAnnotationsDictionary = self.transformToGeoBox(pixelCoordinatesAnnotationDictionary,"") #todo: test.
        print(json.dumps(self.geoReferencedAnnotationsDictionary))
        # 4:
        #self.setCustomAttributes(geoReferencedAnnotationsDictionary)
        # 5:
        self.dfoDataBuilderExport()

    def __init__(self, projectId, authToken, base_url):
        self.projectId = projectId
        self.authToken = authToken
        self.base_url = base_url
        self.jgwPath = "todo"
        self.exportData()

    def __read_jgw(self, jgwPath):
        """
        Read the JGW file and return the values as a dictionary.
        """
        with open(jgwPath, 'r') as file:
            lines = file.readlines()
            values = [float(line.strip()) for line in lines]
        jgw_values = {
            "X_scale": values[0],
            "X_rotation": values[1],
            "Y_rotation": values[2],
            "Y_scale": values[3],
            "X_origin": values[4],
            "Y_origin": values[5]
        }
        return jgw_values

    def transformToGeoBox(self, annotationBoxDictionary, jgwPath):
        """
        Transform the annotation dictionary to a georeferenced bounding box.
        """

        transformed_boxes = []
        
        # Extract the jgw values from the jgw file.
        #jgw_values = self.__read_jgw(jgwPath)

        jgw_values = {
            "X_scale": -0.0677122017093011,
            "X_rotation": 0.0981166742286165,
            "Y_rotation": 0.0979504802242619,
            "Y_scale": 0.0675975080343044,
            "X_origin": 1398409.18391825,
            "Y_origin": -2187299.12171286
        }

        for box in annotationBoxDictionary:
            x1, y1 = box["x1"], box["y1"]
            x2, y2 = box["x2"], box["y2"]

            top_left_geo = self.pixel_to_geolocation(x1, y1, jgw_values)
            top_right_geo = self.pixel_to_geolocation(x2, y1, jgw_values)
            bottom_right_geo = self.pixel_to_geolocation(x2, y2, jgw_values)
            bottom_left_geo = self.pixel_to_geolocation(x1, y2, jgw_values)

            transformed_boxes.append({
                "id": box["id"],
                "geo_coordinates": [
                    top_left_geo,
                    top_right_geo,
                    bottom_right_geo,
                    bottom_left_geo,
                    top_left_geo  # Close the polygon
                ]
            })
        return transformed_boxes
    
    def pixel_to_geolocation(self, x, y, jgw_values):
        X_geo = jgw_values["X_origin"] + (x * jgw_values["X_scale"]) + (y * jgw_values["X_rotation"])
        Y_geo = jgw_values["Y_origin"] + (x * jgw_values["Y_rotation"]) + (y * jgw_values["Y_scale"])
        return X_geo, Y_geo
    
    def dfoDataBuilderExport(self):
        """
        Export the data to a JSON file.

        Combines the label studio and dictionary data into a single JSON file.
        """
        combined_data = {
            "label-studio-project": self.projectData,
            "geoReferencedAnnotations": self.geoReferencedAnnotationsDictionary
        }

        json_data = json.dumps(combined_data, indent=4)
        with open("combined_data.json", "w") as file:
            file.write(json_data)
    
    def setCustomAttributes(self, customAttributes):
        """
        Set the custom attributes in the class.
        """
        pass

    def fetchCurrentProjectData(self):
        """
        Fetches the current project data from the API.
        """
        # Define the URL and headers
        url = "http://localhost:8080/api/projects/"+str(self.projectId)+"/export?exportType=JSON"
        headers = {
        'Authorization': 'Token '+self.authToken,
        }

        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
        # Parse the response content to a JSON object
            json_data = response.json()
            print("JSON Data:", json.dumps(json_data, indent=4))
        else:
            print(f"Error: Received status code {response.status_code}")

        return json_data
    
    def __convertCoordinatesToPixels(self, x, y, width, height, original_width, original_height):
            """
            Convert the coordinates from percentages to pixels.
            """
            return {
                'x1': x * original_width * 1/100,
                'y1': y * original_height * 1/100,
                'x2': (x + width) * original_width * 1/100,
                'y2': (y + height) * original_height * 1/100
            }
    
    def parseProjectData(self, projectData):
        """
        Parse the project data and store it in the class.
        """
        results = []

        # Check if self.projectId exists in projectData
        project_found = False
        for project in projectData:
            if isinstance(project, dict) and 'id' in project and self.projectId == project['id']:
                project_found = True
                if 'annotations' in project:
                    for annotation in project['annotations']:
                        # Check if 'result' key exists in each annotation
                        if 'result' in annotation:
                            for result in annotation['result']:
                                # Extract Annotation Attributes:
                                original_width = result.get('original_width')
                                original_height = result.get('original_height')
                                id = result.get('id')

                                #Within 'Value' dictionary of Annotations's key
                                value = result.get('value', {})
                                x = value.get('x')
                                y = value.get('y')
                                width = value.get('width')
                                height = value.get('height')

                                # Coordinates are in percentages, convert to pixels:
                                geoPolygon = self.__convertCoordinatesToPixels(x, y, width, height, original_width, original_height)

                                # Store extracted attributes in a dictionary
                                extracted = {
                                    'id': id,
                                    'x1': geoPolygon.get('x1'),
                                    'y1': geoPolygon.get('y1'),
                                    'x2': geoPolygon.get('x2'),
                                    'y2': geoPolygon.get('y2'),
                                }
                                results.append(extracted)
        
        if not project_found:
            raise ValueError(f"Project ID {self.projectId} not found in the provided data.")
        
        print(results)
        return results

def main():
    DfoDataBuilder(1, "dc8a69f107b35394c21a81542b4e766199975028", "http://localhost:8080")

if __name__ == "__main__":
    main()
