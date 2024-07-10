"""
This is the LabelStudioController module.
It contains the controller class for managing Label Studio connectivity with the API and front-end react components (runtime).
Will be used to fetch information that will be used for the pyQt GUI.
"""

class LabelStudioController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    runtimeAnnotationsArray = []

    apiKey = ""

    def fetchCurrentAnnotations(self):
        """
        Fetches the current annotations from the RegionStore.js
        1. Fetches the annotations from the RegionStore.js from custom defined function x. 
        2. Returns the annotations array.
        3. Sort by score.
        """
        pass
    
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
        For each annotation, call the hideAnnotation function, located in the RegionStore.js.

        """
        pass

    def fetchPreannotations(self):
        """
        Fetches the preannotations from the API.
        """
        pass
    
    def getZoomInformation(self):
        """
        Fetches the zoom information from function y in the Zoom.jsx.
        """
        pass

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

    
    

