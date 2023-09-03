import { http } from '@/api/http'
import { httpErrorHandle } from '@/utils'
import { ContentTypeEnum, RequestHttpEnum, ModuleTypeEnum } from '@/enums/httpEnum'
import { ProjectItem, ProjectDetail } from './project'

// * 项目列表
export const projectListApi = async (data: object) => {
  try {
    const res = await http(RequestHttpEnum.GET)<ProjectItem[]>(`/goview/${ModuleTypeEnum.PROJECT}`, data)
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 新增项目
export const createProjectApi = async (data: object) => {
  try {
    const res = await http(RequestHttpEnum.POST)<{
      /**
       * 项目id
       */
      id: number
    }>(`/goview/${ModuleTypeEnum.PROJECT}`, data)
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 获取项目
export const fetchProjectApi = async (data: object) => {
  try {
    const res = await http(RequestHttpEnum.GET)<ProjectDetail>(`/goview/${ModuleTypeEnum.PROJECT}/by/id`, data)
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 保存项目
// export const saveProjectApi = async (data: object) => {
//   try {
//     const res = await http(RequestHttpEnum.POST)(
//       `${ModuleTypeEnum.PROJECT}/save/data`,
//       data,
//       ContentTypeEnum.FORM_URLENCODED
//     )
//     return res
//   } catch {
//     httpErrorHandle()
//   }
// }

export const saveProjectApi = async (data: object) => {
  try {
    const res = await http(RequestHttpEnum.POST)(
        `/goview/${ModuleTypeEnum.PROJECT}/save/data`,
        data,
    )
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 修改项目基础信息
export const updateProjectApi = async (data: object, id: number) => {
  try {
    const res = await http(RequestHttpEnum.PUT)(`/goview/${ModuleTypeEnum.PROJECT}/${id}`, data)
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 删除项目
export const deleteProjectApi = async (id: number) => {
  try {
    const res = await http(RequestHttpEnum.DELETE)(`/goview/${ModuleTypeEnum.PROJECT}/${id}`)
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 修改发布状态 [-1未发布,1发布]
export const changeProjectReleaseApi = async (data: object) => {
  try {
    const res = await http(RequestHttpEnum.PUT)(`/goview/${ModuleTypeEnum.PROJECT}/publish/by_id/${data.id}`, data)
    return res
  } catch {
    httpErrorHandle()
  }
}

// * 上传文件
export const uploadFile = async (data: object) => {
  try {
    const res = await http(RequestHttpEnum.POST)<{
      /**
       * 文件地址
       */
      id: number,
      name: string,
      url: string,
    }>(`/system/upload`, data, ContentTypeEnum.FORM_DATA)
    return res
  } catch {
    httpErrorHandle()
  }
}
