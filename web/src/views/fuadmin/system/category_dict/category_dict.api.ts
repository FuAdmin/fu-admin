/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/8 00:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/system/category_dict',
  GetDeptList = '/api/system/category_dict/list/tree',
}

/**
 * 获取
 */

export const getList = (params) => {
  return defHttp.get({ url: DeptApi.GetDeptList, params });
};

/**
 * 保存或更新
 */

export const createOrUpdate = (params, isUpdate) => {
  if (isUpdate) {
    return defHttp.put({ url: DeptApi.prefix + '/' + params.id, params });
  } else {
    return defHttp.post({ url: DeptApi.prefix, params });
  }
};

/**
 * 删除
 */

export const deleteItem = (id) => {
  return defHttp.delete({ url: DeptApi.prefix + '/' + id });
};
