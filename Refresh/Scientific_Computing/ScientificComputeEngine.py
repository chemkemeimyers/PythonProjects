import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

class ScientificComputingEngine:
    def __init__(self, nx: int, ny: int, nz: int, dx=1.0, dy=1.0, dz=1.0):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.dy = dy
        self.dz = dz
    
    def laplace_smooth_vecrotized(self, grid_3d: np.ndarray, max_iterations: int=500, tolerance: float = 1e-4) -> np.ndarray:

        #Create copy to preserve original data
        smoothed = grid_3d.copy()

        for i in range(max_iterations):
            # Take a snapshot of current values before updating
            previous_core = smoothed[1:-1, 1:-1, 1:-1].copy()

            #7 point stencil: Value = (left + right + top + bottom + front + back) / 6
            smoothed[1:-1, 1:-1, 1:-1] = (
                smoothed[1:-1, 1:-1, 0:-2] + #Left (-x)
                smoothed[1:-1, 1:-1, 2:] + #Right (+x)
                smoothed[1:-1, 0:-2, 1:-1] + #Top (-Y)
                smoothed[1:-1, 2:, 1:-1] + #Bottom (+y)
                smoothed[0:-2, 1:-1, 1:-1] + #Front (-z)
                smoothed[2:, 1:-1, 1:-1] #Back (+z)
            )/6

            max_delta = np.max(np.abs(smoothed[1:-1, 1:-1, 1:-1] - previous_core))

            if max_delta < tolerance:
                print(f" --> Convergence achieved early at iteration {i+1}. Max delta: {max_delta:.2e}")
            else:
                print(f" --> After {i+1} iterations lowest tolerance observed is {max_delta:.2e} which is higher than the tolerance value {tolerance:.2e}")
            
        return smoothed
    
    def extract_anomalies(self, smoothed_grid: np.ndarray, threshold:float) -> pd.DataFrame:
        """
        Computes the 3D Gradient Magnitude using vectorized operations
        and isolates high-contrast structural boundaries"""
        #Compute central spatial differences across the 3D grid
        grad_z, grad_y, grad_x = np.gradient(smoothed_grid, self.dz, self.dy, self.dx)

        # Calculate Gradient Magnitude: = \sqrt{gx^2 + gy^2 + gz^2)}
        gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2 + grad_z**2)

        # Generate absolute spatial coordinate grids matching the volume layout
        z_idx, y_idx, x_idx = np.indices((self.nz, self.ny, self.nx))

        #Flatten tensors into a structured tabular format
        df = pd.DataFrame({
            'x': x_idx.ravel() * self.dx,
            'y': y_idx.ravel() * self.dy,
            'z': z_idx.ravel() * self.dz,
            'filtered_val': smoothed_grid.ravel(),
            'gradient_mag': gradient_magnitude.ravel()
        })

        return df[df['gradient_mag'] > threshold].copy()
    
    def plot_cross_section(self, smoothed_grid: np.ndarray, target_z_layer:int):

        """
        Extracts a horizantal cross-sectional plane at a specific depth layer.
        """
        z_slice = smoothed_grid[target_z_layer,:,:]

        plt.figure(figsize=(8,6))

        #Remder the 2D matrix as a heatmap image
        img = plt.imshow(z_slice, cmap='plasma', origin='lower')

        plt.colorbar(img, label='Physical Voxel Measurement')
        plt.title(f'Horizontal Depth Cross-Section plane (Z layer = {target_z_layer})')
        plt.xlabel('X Spatial Nodes')
        plt.ylabel('Y Spatial Nodes')
        plt.grid(True, alpha=0.3)

        plt.show()
    
#Execution verification
if __name__ == "__main__":
    # Define a 3D grid
    NX, NY, NZ = 120, 120, 60

    # Initialize Synthetic Noisy Volume
    np.random.seed(42)
    raw_data = np.random.normal(loc = 10, scale=1.5, size=(NZ, NY, NX))

    #Inject a target ore body
    # Center coordinates of 3D grid
    center_z, center_y, center_x = NZ//2, NY//2, NX//2
    radius = 18 # Voxel radius of the target ore body

    #Generate spatial distance meshes foe the center point
    z_indices, y_indices, x_indices = np.indices((NZ, NY, NX))
    distance_from_center = np.sqrt(
        (z_indices - center_z)**2 +
        (y_indices - center_y)**2 +
        (x_indices - center_x)**2
    )

    #Where the distance is less than the radius, inject a massive signal anomaly
    raw_data[distance_from_center <= radius] +=25.0

    # Force static boundary conditions e.g. edges fixed to baseline values
    raw_data[0, :, :] = 0.0; raw_data[-1,:,:] = 0.0

    #Intantiate engine
    engine = ScientificComputingEngine(nx=NX, ny=NY, nz=NZ)

    #Time the numerical stensic kernel
    start_time = time.time()

    smoothed_volume = engine.laplace_smooth_vecrotized(raw_data, max_iterations=50)
    print(f"Laplace Relaxation Complete in: {time.time() - start_time} seconds.")

    # Extract spatial structural anomalies
    anomalies_df = engine.extract_anomalies(smoothed_volume, threshold=1.5)
    print(f"Extraction complete. Found {len(anomalies_df)} target coordinates matching threshold criteria")
    print(f"Sample output target matrix:")
    print(anomalies_df.head())

    #plot Matplotlib depth slice
    print('Generating Matplotlib Depth Slice Profiler')
    engine.plot_cross_section(smoothed_volume, target_z_layer=30)


