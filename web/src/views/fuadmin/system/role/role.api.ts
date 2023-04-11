/**
 * -*- coding: utf-8 -*-
 * time: 2022/5/25 22:12
 * author: 臧成龙
 * QQ: 939589097
 */
import { defHttp } from '/@/utils/http/axios';

enum DeptApi {
  prefix = '/api/system/role',
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

/**
 * 获取菜单和按钮list
 */

export const getMenuList = () => {
  return defHttp.get({ url: DeptApi.prefix + '/list/menu' });
};

export const getMenuButtonList = () => {
  return defHttp.get({ url: DeptApi.prefix + '/list/menu_button' });
};

export const getMenuColumnList = () => {
  return defHttp.get({ url: DeptApi.prefix + '/list/menu_column' });
};

export const getButtonByMenuId = (menu_id) => {
  return defHttp.get({ url: DeptApi.prefix + '/list/button/' + menu_id });
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

/**
 * 根据角色查询树信息
 */
export const queryTreeListForRole = () => defHttp.get({ url: DeptApi.prefix });
/**
 * 查询角色权限
 */
export const queryRolePermission = (params) => defHttp.get({ url: DeptApi.prefix, params });
/**
 * 保存角色权限
 */
export const saveRolePermission = (params) => defHttp.post({ url: DeptApi.prefix, params });
/**
 * 查询角色数据规则
 */
export const queryDataRule = (params) =>
  defHttp.get(
    { url: `${DeptApi.prefix}/${params.functionId}/${params.roleId}` },
    { isTransformResponse: false },
  );
/**
 * 保存角色数据规则
 */
export const saveDataRule = (params) => defHttp.post({ url: DeptApi.prefix, params });
