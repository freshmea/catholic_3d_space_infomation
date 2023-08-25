import open3d as o3d
pcd = o3d.io.read_point_cloud("catholic_3d_space_infomation/000000.pcd")

# visualization with open3d
o3d.visualization.draw_geometries([pcd])

# # visualization with pptk
# v = pptk.viewer(pcd.points)