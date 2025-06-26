def get_hazard_state_from_yolo(detections: list) -> list:
    """
    Converting YOLO object detections into a one-hot hazard state vector.

    :param detections: List of detected class names (e.g., ['car', 'person', 'traffic light'])
    :return: One-hot vector representing the current hazard state
    """

    # Map to hazard index:
    # 0 = Clear
    # 1 = Red light
    # 2 = Roadblock (cones or barricades)
    # 3 = Accident (e.g., stopped car + person)
    hazard_state = 0  # default to clear

    if 'traffic light' in detections:
        hazard_state = 1
    elif 'cone' in detections or 'barricade' in detections:
        hazard_state = 2
    elif 'car' in detections and 'person' in detections:
        hazard_state = 3  # possible accident (stalled car + pedestrian)

    one_hot = [0, 0, 0, 0]
    one_hot[hazard_state] = 1
    return one_hot


if __name__ == "__main__":                                        # Example test
    test1 = get_hazard_state_from_yolo(['car', 'person'])         # Accident
    test2 = get_hazard_state_from_yolo(['traffic light'])         # Red light
    test3 = get_hazard_state_from_yolo(['cone'])                  # Roadblock
    test4 = get_hazard_state_from_yolo([])                        # Clear

    print("Test 1:", test1)
    print("Test 2:", test2)
    print("Test 3:", test3)
    print("Test 4:", test4)
