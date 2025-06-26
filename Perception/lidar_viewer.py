import numpy as np
import open3d as o3d
import os

lidar_path = "C:/INTERNSHIP/kitti/velodyne_points/data/0000000000.bin"  # change to your .bin file path

def load_kitti_bin(bin_path):                                           # Load the .bin file (each point: x, y, z, reflectance)
    scan = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
    points = scan[:, :3]  # Drop reflectance for now
    return points

def show_point_cloud(points):                                           # Convert to Open3D PointCloud object
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    pcd.paint_uniform_color([0.6, 0.6, 0.6])

    o3d.visualization.draw_geometries([pcd], window_name="KITTI LiDAR Viewer")

points = load_kitti_bin(lidar_path)
show_point_cloud(points)
