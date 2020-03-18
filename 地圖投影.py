#!/usr/bin/env python
# coding: utf-8

# In[4]:


import folium # 匯入 folium 套件
from folium.plugins import MiniMap
from folium.plugins import MeasureControl
from folium.plugins import Draw
from folium.plugins import MousePosition

fmap = folium.Map(location=[35.709635, 139.810851], zoom_start = 15,world_copy_jump=True,)# 建立地圖與設定位置
#fmap.add_child(folium.Marker(location=[35.709635, 139.810851],
                            # popup='Skytree'))

m1 = folium.Marker(location=[35.709635, 139.810851],
                   popup='Skytree',icon=folium.Icon(icon='info-sign'
                                    ,color ='beige'))


m2 = folium.Marker(location=[35.707595, 139.795530],
                   popup='Hotel',
                   icon=folium.Icon(icon='paper-plane', # Icon類型
                                    color='green',# Marker顏色
                                    prefix='fa')) # 使用Font Awesome Icons

m3 = folium.Marker(location=[35.715092, 139.796666],
                   popup='Asakusa Temple',
                   icon=folium.Icon(icon='info-sign'
                                    ,color ='beige'))
minimap = MiniMap(width=200, height=100,toggle_display=True,zoom_level_offset=-4,tile_layer='stamenwatercolor'
                 )#加入迷你地圖並使迷你地圖可收放,還有大小調整
fmap.add_child(child = minimap)

center_pos = [35.709635, 139.810851]
fmap.add_child(folium.Circle(location=center_pos,
                             color='red', # Circle 顏色
                             radius=500, # Circle 寬度
                             fill=True, # 填滿中間區域
                             fill_opacity=0.2# 設定透明度:1是完全不透
                             ))
points = [[35.709635, 139.810851],
          [35.707595, 139.795530],
          [35.715092, 139.796666]]

fmap.add_child(folium.PolyLine(locations=points, # 座標List
                               weight=8,color = '#9999FF')) # 線條寬度
fmap.add_child(MeasureControl())#量測地圖功能加入
fmap.add_child(MousePosition())

# 將各Marker加入地圖。
fmap.add_child(child=m1)
fmap.add_child(child=m2)
fmap.add_child(child=m3)
fmap.save('map.html')
fmap  # 在notebook中顯示地圖


# In[53]:


'''
我好帥
'''


# In[78]:


help(minimap)


# In[5]:


import folium # 匯入 folium 套件
import numpy as np
from folium.plugins import HeatMap

fmap = folium.Map(location=[35.712326, 139.804037], zoom_start=12)

# 建立隨機資料
data = (np.random.normal(size=(100, 3)) * 0.02 *
        np.array([[1, 1, 1]]) +
        np.array([[35.712326, 139.804037, 1]])).tolist()

fmap.add_child(HeatMap(data=data))


# In[2]:


import numpy as np
from folium.plugins import HeatMapWithTime

center_pos = [35.712326, 139.804037]

# 使用 numpy 建立初始資料
initial_data = (np.random.normal(size=(200, 2)) *
                np.array([[0.07, 0.07]]) +
                np.array([center_pos]))

# 建立連續資料
data = [initial_data.tolist()]
for i in range(80):
    data.append((data[i] + np.random.normal(size=(200, 2)) * 0.122).tolist())

fmap = folium.Map(center_pos, zoom_start=11)
fmap.add_child(HeatMapWithTime(data)) # 顯示連續熱度圖


# In[ ]:




