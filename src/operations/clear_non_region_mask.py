from typing import List

import cv2
import numpy as np

from model import Rectangle


def clear_non_region_mask(mask: np.ndarray, regions: List[Rectangle]) -> np.array:
    """
    Sets the area of the mask not covered by any region to 0.
    :param mask: the sign mask
    :param regions: the list of regions
    :return: a mask where all the whites are inside the regions
    """
    m = np.zeros(mask.shape, mask.dtype)
    for region in regions:
        cv2.rectangle(m, (region.top_left[1], region.top_left[0]),
                      (region.get_bottom_right()[1], region.get_bottom_right()[0]), 255, thickness=cv2.FILLED)

    mask = cv2.bitwise_and(mask, m)
    return mask
