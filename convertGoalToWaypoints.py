import math

class Waypoint:
    def __init__(self, x, y, angle, index):
        self.x = x
        self.y = y
        self.angle = angle
        self.index = index

def calculate_angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.atan2(dy, dx)

goal_positions = {
    'austin_track': [
        [0.0, 0.0], [0.9114490385, -0.6963720732], [1.8229057219, -1.3927312266], [2.7344172186, -2.0890257812]
    ],
    # Add more tracks here
}

new_goal_positions = {}

for track_name, waypoints in goal_positions.items():
    new_track = []
    for i, waypoint in enumerate(waypoints):
        if i < len(waypoints) - 1:
            angle = calculate_angle(waypoint, waypoints[i + 1])
        else:
            angle = calculate_angle(waypoint, waypoints[0])  # Angle to the first waypoint
        new_track.append(Waypoint(waypoint[0], waypoint[1], angle, i))
    new_goal_positions[track_name] = new_track

# Generate formatted text
formatted_output = f"waypoints = {{\n"
for track_name, waypoints in new_goal_positions.items():
    formatted_output += f"    '{track_name}': [\n"
    for waypoint in waypoints:
        formatted_output += f"        Waypoint({waypoint.x:.2f}, {waypoint.y:.2f}, {waypoint.angle:.2f}, {waypoint.index}),\n"
    formatted_output += "    ],\n"
formatted_output += "}\n"

print(formatted_output)
