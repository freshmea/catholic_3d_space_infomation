import open3d as o3d

def main():
    pcd = o3d.io.read_point_cloud("catholic_3d_space_infomation/000000.pcd")
    pcd = pcd.voxel_down_sample(voxel_size=0.2)
    o3d.visualization.draw_geometries([pcd])

if __name__ =='__main__':
    main()