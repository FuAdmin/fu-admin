#!/bin/python
#coding: utf-8
# +-------------------------------------------------------------------
# | django-vue3-lyadmin
# +-------------------------------------------------------------------
# | Author: lybbn
# +-------------------------------------------------------------------
# | QQ: 1042594286
# +-------------------------------------------------------------------

# ------------------------------
# 系统命令封装
# ------------------------------

import platform

plat = platform.system().lower()
if plat == 'windows':
    import windows as myos
else:
    import linux as myos


class system:

    isWindows = False

    def __init__(self):
        self.isWindows = self.isWindows()

    def isWindows(self):
        plat = platform.system().lower()
        if plat == 'windows':
            return True
        return False

    def GetSystemAllInfo(self,isCache=False):
        """
        获取系统所有信息
        """
        data = {}
        data['mem'] = self.GetMemInfo()
        data['load_average'] = self.GetLoadAverage()
        data['network'] = self.GetNetWork()
        data['cpu'] = self.GetCpuInfo(1)
        data['disk'] = self.GetDiskInfo()
        data['time'] = self.GetBootTime()
        data['system'] = self.GetSystemVersion()
        data['is_windows'] = self.isWindows
        return data

    def GetMemInfo(self):
        memInfo =  myos.GetMemInfo()
        return memInfo

    def GetLoadAverage(self):
        data = myos.GetLoadAverage()
        return data

    def GetNetWork(self):
        data = myos.GetNetWork()
        return data

    def GetCpuInfo(self,interval=1):
        data = myos.GetCpuInfo(interval)
        return data

    def GetBootTime(self):
        data = myos.GetBootTime()
        return data

    def GetDiskInfo(self):
        data = myos.GetDiskInfo()
        return data

    def GetSystemVersion(self):
        data = myos.GetSystemVersion()
        return data