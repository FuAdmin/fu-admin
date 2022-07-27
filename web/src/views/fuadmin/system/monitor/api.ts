/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/22 23:43
 * author: 臧成龙
 * QQ: 939589097
 */
import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/system/monitor',
}

export const getSystemInfo = () => {
  return defHttp.get({ url: DeptApi.prefix });
};
