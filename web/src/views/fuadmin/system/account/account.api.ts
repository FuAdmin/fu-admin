/**
 * -*- coding: utf-8 -*-
 * time: 2022/3/30 15:55
 * author: 臧成龙
 * QQ: 939589097
 */
import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/system/user',
}

/**
 * 获取
 */

export const getList = (params) => {
  return defHttp.get({ url: DeptApi.prefix, params });
};

export const getAllList = () => {
  return defHttp.get({ url: DeptApi.prefix + '/all/list' });
};

export const getById = (id) => {
  return defHttp.get({ url: DeptApi.prefix + '/' + id });
};

export const repassword = (params) => {
  return defHttp.post({ url: DeptApi.prefix + '/set/repassword', params });
};



export const resetPassword = (id) => {
  return defHttp.put({ url: DeptApi.prefix + '/reset/password/' + id });
};



// export const getAllList = () => {
//   return defHttp.get({ url: DeptApi.prefix + '/all/list' });
// };

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
