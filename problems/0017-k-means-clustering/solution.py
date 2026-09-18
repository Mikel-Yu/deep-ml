import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = list(initial_centroids)
    
    for _ in range(max_iterations):
        # Initialize clusters mapping centroid indices to lists of points
        clusters = {i: [] for i in range(k)}
        
        # 1. Assignment step: find the closest centroid for each point
        for point in points:
            point_arr = np.array(point)
            min_dist = np.inf
            closest_idx = 0
            
            for idx, centroid in enumerate(centroids):
                distance = np.linalg.norm(point_arr - np.array(centroid))
                if distance < min_dist:
                    min_dist = distance
                    closest_idx = idx
            
            clusters[closest_idx].append(point)
        
        # 2. Update step: compute the new centroids as the mean of cluster points
        new_centroids = []
        for idx in range(k):
            if clusters[idx]:
                # Calculate mean along axis 0 and convert back to a tuple
                mean_point = tuple(np.mean(clusters[idx], axis=0))
                new_centroids.append(mean_point)
            else:
                # Keep the old centroid if the cluster is empty
                new_centroids.append(centroids[idx])
        
        # Check for convergence
        if new_centroids == centroids:
            break
            
        centroids = new_centroids

    return centroids