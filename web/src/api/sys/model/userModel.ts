/**
 * @description: Login interface parameters
 */
export interface LoginParams {
  username: string;
  password: string;
}

export interface RoleInfo {
  name: string;
  value: string;
}

/**
 * @description: Login interface return value
 */
export interface LoginResultModel {
  userId: string | number;
  token: string;
  role: RoleInfo;
}

/**
 * @description: Get user information return value
 */
export interface GetUserInfoModel {
  role: RoleInfo[];
  // 用户id
  id: string | number;
  // 用户名
  username: string;
  // 真实名字
  name: string;
  // 头像
  avatar: string;
  // 介绍
  desc?: string;
}
