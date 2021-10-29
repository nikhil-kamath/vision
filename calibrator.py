from bounding_box import BoundingBoxGenerator
import cv2

'''returns 4 tuples corresponding to corners of the points'''
def get_points(bounding_box):
    return (int(bounding_box[0][0]), int(bounding_box[0][1])), (int(bounding_box[1][0]), int(bounding_box[1][1])), (int(bounding_box[2][0]), int(bounding_box[2][1])), (int(bounding_box[3][0]), int(bounding_box[3][1]))

'''returns the calibrated focal length inputted a picture with a starting distance'''
def calibrate(image, initial_distance: float, initial_width: float) -> float:
    estimator = BoundingBoxGenerator(image_array=image, width=initial_width)
    box_dims = estimator.estimate()
    bounding_box = cv2.boxPoints(box_dims)

    _, p2, p3, _ = get_points(bounding_box)
    box_width = abs(p2[0] - p3[0])
    print('width: ', box_width)
    focal_length = (box_width * initial_distance) / initial_width

    return focal_length