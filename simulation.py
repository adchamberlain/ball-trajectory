import numpy as np
import matplotlib.pyplot as plt

def calculate_trajectory(angle_degrees, initial_velocity):
    # Convert angle to radians
    angle = np.radians(angle_degrees)
    
    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    
    # Initial velocities
    v0x = initial_velocity * np.cos(angle)
    v0y = initial_velocity * np.sin(angle)
    
    # Time of flight
    flight_time = 2 * v0y / g
    
    # Create time points
    t = np.linspace(0, flight_time, 100)
    
    # Calculate positions
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    
    return x, y

def plot_trajectory():
    # Get user input
    angle = float(input("Enter launch angle (degrees): "))
    velocity = float(input("Enter initial velocity (m/s): "))
    
    # Calculate trajectory
    x, y = calculate_trajectory(angle, velocity)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='Ball Path')
    plt.grid(True)
    plt.xlabel('Distance (meters)')
    plt.ylabel('Height (meters)')
    plt.title(f'Ball Trajectory\nAngle: {angle}°, Initial Velocity: {velocity} m/s')
    plt.axis('equal')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_trajectory()
