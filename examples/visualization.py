# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import pcl
import pcl.pcl_visualization

## @ author: niranjanreddy891

cloud = pcl.load_XYZRGB('./examples/pcldata/tutorials/table_scene_mug_stereo_textured.pcd')
visual = pcl.pcl_visualization.CloudViewing()


visual.ShowColorCloud(cloud, b'cloud')
# visual.ShowColorACloud(cloud, b'cloud')

def check_was_stopped():
     visual.WasStopped()

     root.after(100, check_was_stopped)
check_was_stopped()
