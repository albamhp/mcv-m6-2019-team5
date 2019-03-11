from typing import List

from model import Video, Rectangle
from operations.find_boxes import find_boxes
from operations.gaussian_model import get_background_model, gaussian_model_adaptive
from operations.morphological_operations import closing, opening, dilate


def week2_adaptive(video: Video) -> List[List[Rectangle]]:
    model_mean, model_std = get_background_model(video, int(2141 * 0.25), total_frames=int(2141 * 0.25))
    bounding_boxes = []

    for mask in gaussian_model_adaptive(video, int(2141 * 0.25), model_mean, model_std,
                                        total_frames=int(2141 * 0.75)):
        mask = closing(opening(closing(mask, 15), 15), 30)

        bbs = find_boxes(mask)
        bounding_boxes.append(bbs)

    return bounding_boxes
