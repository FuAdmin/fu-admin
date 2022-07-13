/**
 * -*- coding: utf-8 -*-
 * time: 2022/4/3 22:35
 * author: 臧成龙
 * QQ: 939589097
 */

import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/system/button',
}

/**
 * 获取
 */

export const getList = () => {
  return defHttp.get({ url: DeptApi.prefix });
};

/**
 * 获取all
 */

export const getAllList = () => {
  return defHttp.get({ url: DeptApi.prefix + '/all/list' });
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
