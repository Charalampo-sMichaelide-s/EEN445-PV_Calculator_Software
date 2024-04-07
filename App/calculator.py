## Here goes the logic of the app.

import math

def minimum_pv_shadow_length(latitude, slope, height):
    """
    Calculate the minimum shadow length of a PV panel on December 21st.

    Parameters:
    - slope (float): The tilt angle of the PV panel from the horizontal (in degrees).
    - height (float): The height of the PV panel above the ground (in meters).
    - latitude (float): The latitude of the location (in degrees).

    Returns:
    - minimum_shadow_length (float): The minimum shadow length of the PV panel (in meters).
    """
    # Solar declination on December 21st
    solar_declination = -23.45  # degrees

    # Calculate the sun's elevation angle at solar noon
    alpha = 90 - latitude + solar_declination

    # Calculate the length of the shadow
    minimum_shadow_length = height / math.tan(math.radians(alpha - slope))

    return minimum_shadow_length

# # Example usage
# slope = 10  # degrees
# height = 2  # meters
# latitude = 33  # degrees
# shadow_length = minimum_pv_shadow_length(slope, height, latitude)
# print(f"The minimum shadow length of the PV panel is approximately {minimum_shadow_length:.2f} meters.")
