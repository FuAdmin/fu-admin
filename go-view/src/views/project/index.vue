<template>
  <div class="go-project">
    <n-layout has-sider position="absolute">
      <n-space vertical>
        <project-layout-sider></project-layout-sider>
      </n-space>
      <n-layout>
        <layout-header-pro></layout-header-pro>
        <n-layout
          id="go-project-content-top"
          class="content-top"
          position="absolute"
          :native-scrollbar="false"
        >
          <n-layout-content>
            <layout-transition-main>
              <router-view></router-view>
            </layout-transition-main>
          </n-layout-content>
        </n-layout>
      </n-layout>
    </n-layout>
  </div>
</template>

<script setup lang="ts">
import { ProjectLayoutSider } from './layout/components/ProjectLayoutSider'
import { LayoutHeaderPro } from '@/layout/components/LayoutHeaderPro'
import { LayoutTransitionMain } from '@/layout/components/LayoutTransitionMain/index'
import { SystemStoreUserInfoEnum, SystemStoreEnum } from '@/store/modules/systemStore/systemStore.d'

import { fetchRouteQuery } from '@/utils'
import {useSystemStore} from "@/store/modules/systemStore/systemStore";
const token: string= fetchRouteQuery().token;
if (token) {
  const systemStore = useSystemStore()
// 存储到 pinia
  systemStore.setItem(SystemStoreEnum.USER_INFO, {
    [SystemStoreUserInfoEnum.USER_TOKEN]: token,
    [SystemStoreUserInfoEnum.TOKEN_NAME]: 'Authorization',
    [SystemStoreUserInfoEnum.USER_ID]: 'id',
    [SystemStoreUserInfoEnum.USER_NAME]: 'username',
    [SystemStoreUserInfoEnum.NICK_NAME]: 'nickname',
  })
}

console.log('token', token);
// 提示
// goDialog({
//   message: '不要在官方后端上发布任何私密数据，任何人都看得到并进行删除！！！！',
//   isMaskClosable: true,
//   closeNegativeText: true,
//   transformOrigin: 'center',
//   onPositiveCallback: () => {}
// })
</script>

<style lang="scss" scoped>
@include go(project) {
  .content-top {
    top: $--header-height;
    margin-top: 1px;
  }
}
</style>
