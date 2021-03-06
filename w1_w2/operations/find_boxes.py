from typing import List
import numpy as np
from model import Rectangle
from operations.clear_non_region_mask import clear_non_region_mask
from .combine_overlapped_regions import combine_overlapped_regions
from .get_cc_regions import get_cc_regions

MIN_AREA = 9000
MIN_ASPECT_RATIO = 0.3
SCALE = 0.1
SCALE_POST = 0.2
MAX_AREA = 200000


def find_boxes(mask: np.ndarray) -> (np.ndarray, List[Rectangle]):
    detections = get_cc_regions(mask)
    for d in detections:
        d.apply_scale(SCALE)

    detections = combine_overlapped_regions(detections)
    remove_by_shape(detections)

    mask = clear_non_region_mask(mask, detections)
    for d in detections:
        d.apply_scale(SCALE_POST)
    return mask, detections


def remove_by_shape(detections):
    i = 0
    while i < len(detections):
        detection = detections[i]
        if detection.get_area() < MIN_AREA or detection.get_area() > MAX_AREA or detection.width / detection.height < MIN_ASPECT_RATIO or \
                detection.height / detection.width < MIN_ASPECT_RATIO:
            detections.pop(i)
        else:
            i += 1
