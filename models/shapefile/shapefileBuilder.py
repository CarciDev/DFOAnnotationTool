import json
import os
import fiona
from fiona.crs import from_epsg
from shapely.geometry import mapping, Polygon

class ShapefileBuilder:
    def export_to_shapefile(self, geo_referenced_annotations, label_studio_data, output_dir):
        """
        Export the transformed georeferenced bounding boxes to shapefiles, grouped by taskId and image name.
        Also create a shapefile containing all annotations.
        """
        # Create a mapping of taskId to image name
        task_image_map = {item["id"]: item["data"]["image"] for item in label_studio_data["label-studio-project"]}
        
        # Group annotations by taskId
        grouped_annotations = {}
        for annotation in geo_referenced_annotations:
            task_id = annotation["taskId"]
            if task_id not in grouped_annotations:
                grouped_annotations[task_id] = []
            grouped_annotations[task_id].append(annotation)
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Create a folder for all annotations
        all_annotations_dir = os.path.join(output_dir, "all_annotations")
        os.makedirs(all_annotations_dir, exist_ok=True)
        all_annotations_file = os.path.join(all_annotations_dir, "shapes.shp")
        
        schema = {
            'geometry': 'Polygon',
            'properties': {'annotationId': 'str'}
        }

        # Write all annotations to a single shapefile
        with fiona.open(all_annotations_file, 'w', driver='ESRI Shapefile', schema=schema, crs=from_epsg(4326)) as all_shapefile:
            for annotation in geo_referenced_annotations:
                polygon = {
                    'geometry': mapping(Polygon(annotation["geo_coordinates"])),
                    'properties': {'annotationId': annotation["annotationId"]}
                }
                all_shapefile.write(polygon)
        print(f"Shapefile for all annotations created successfully at {all_annotations_file}")

        # Write separate shapefiles for each taskId
        for task_id, annotations in grouped_annotations.items():
            # Get image name for the task
            image_name = task_image_map.get(task_id, "unknown_image")
            image_name = os.path.basename(image_name)  # Get the base name of the image file
            task_dir = os.path.join(output_dir, f"task_{task_id}_{image_name}")
            os.makedirs(task_dir, exist_ok=True)
            output_file = os.path.join(task_dir, "shapes.shp")
            
            with fiona.open(output_file, 'w', driver='ESRI Shapefile', schema=schema, crs=from_epsg(4326)) as shapefile:
                for annotation in annotations:
                    polygon = {
                        'geometry': mapping(Polygon(annotation["geo_coordinates"])),
                        'properties': {'annotationId': annotation["annotationId"]}
                    }
                    shapefile.write(polygon)
            print(f"Shapefile for task {task_id} with image {image_name} created successfully at {output_file}")

if __name__ == "__main__":
    # Create an instance of ShapefileBuilder
    builder = ShapefileBuilder()

    # Load the data from combined_data.json
    with open("combined_data.json") as file:
        data = json.load(file)

    # Extract the geo_referenced_annotations list from the data
    geo_referenced_annotations = data.get("geoReferencedAnnotations", [])
    label_studio_data = data  # The entire JSON structure

    output_dir = "shapefiles_by_task"  # Directory to save the shapefiles

    # Call the export_to_shapefile method
    builder.export_to_shapefile(geo_referenced_annotations, label_studio_data, output_dir)
