def reward_function(params):
    
    # Steering threshold value 
    STEERING_THRESHOLD = 15
    # Speed threshold value 
    SPEED_THRESHOLD = 2
    # Maximum speed
    SPEED_MAX = 3

    # Input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    is_offtrack = params['is_offtrack']
    speed = params['speed']
    steering_angle = params['steering_angle']
    track_width = params['track_width']

    # If the car is going off-track or all the wheels are 
    # not present on the track, penalise it.  
    if not all_wheels_on_track or is_offtrack:
        reward = 1e-3
        return float(reward)
    
    # Quadratic equation to reward the vehicle if it is following the 
    # center-line (but not making the function too restrictive).
    reward = 1 - (distance_from_center/(track_width/2))**(1/4)
    
    # If steering angle is less than steering threshold and 
    # speed is greater than the speed threshold, reward the vehicle.
    if abs(steering_angle) < STEERING_THRESHOLD and speed > SPEED_THRESHOLD:
        reward += speed/SPEED_MAX
    
    # Return the float reward value.
    return float(reward)