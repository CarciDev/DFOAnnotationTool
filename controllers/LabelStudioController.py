"""
This is the LabelStudioController module.
It contains the controller class for managing Label Studio connectivity with the API and front-end react components (runtime).
Will be used to fetch information that will be used for the pyQt GUI.
"""
import requests
API_TOKEN = "dc8a69f107b35394c21a81542b4e766199975028"
API_URL = "http://localhost:8080/api/dfo"

headers = {
"Authorization": f"Token {API_TOKEN}"
}

class LabelStudioController:

    def fetchCurrentTaskAnnotations(self):
        """
        Fetches the current annotations from the RegionStore.js
        1. Fetches the annotations from the RegionStore.js from custom defined function x. 
        2. Returns the annotations array.
        3. Sort by score.
        """
        # from .RegionStore import getAnnotations

        # self.runtimeAnnotationsArray = getAnnotations()
        # self.runtimeAnnotationsArray.sort(key=lambda annotation: annotation['score'], reverse=True)
        # return self.runtimeAnnotationsArray
    
    def getHighestScoredAnnotation(self):
        """
        Returns the highest scored annotation from the annotations array.
        """
        pass

    def getLowestScoredAnnotation(self):
        """
        Returns the lowest scored annotation from the annotations array.
        """
        pass

    def hideAnnotationsBelowThreshold(self, threshold):
        """
        Hides annotations below a certain threshold.
        
        For all annotations in the annotation array, if the score is below the threshold, hide the annotation.
        For each annotation, call the toggleVisibility function, located in the RegionStore.js.

        """
        pass

    def fetchPreannotations(self):
        """
        Fetches the preannotations from the API.
        """
        pass
    
    def getZoomInformation():
        """
        Fetches the zoom information from the custom API.
        """
        response = requests.get(API_URL + "/zoomdata/", headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")

    def createProject(self):
        """
        Creates a new project.

        1. Create a project. This includes: https://api.labelstud.io/api-reference/api-reference/projects/create

        2. Import our Images / data. Some pre-processing of metadata like geolocations might be required. We might define our own datatype to organize this data.

        """
        pass

    def loadProject(self, id):
        """
        Loads a project via the API. https://api.labelstud.io/api-reference/api-reference/projects/get
        """
        pass

    def listProjects(self):
        """
        Lists all projects via the API. https://api.labelstud.io/api-reference/api-reference/projects/list
        """
        pass

    def exportAnnotationCOCO(self):
        """
        Exports the annotations in COCO format.

        ex: curl -X GET http://localhost:8080/api/projects/1/export?exportType=COCO -H 'Authorization: Token dc8a69f107b35394c21a81542b4e766199975028' --output 'project.zip'
        from https://labelstud.io/api#tag/Export
        """
        pass