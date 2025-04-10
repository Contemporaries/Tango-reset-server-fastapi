# Author: HuangLi
# E-Mail: lihuang@ihep.ac.cn
# Version: 1.0.0
# Date: 3/27/2025

from tango import Database, DeviceProxy

db = Database()

if __name__ == "__main__":
    def get_device_attributes(device_name):
        """获取指定设备的所有attributes"""
        attr_list = []
        attr_list = DeviceProxy(device_name).attribute_list_query_ex()
        return attr_list[0]


    # 测试函数
    print("单个设备的attributes:")
    print(get_device_attributes("lact/pk9019/1"))

    print("\n所有设备的attributes:")
    # print(get_all_device_attributes())
