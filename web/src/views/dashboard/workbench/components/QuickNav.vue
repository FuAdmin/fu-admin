<template>
  <Card title="快捷导航" v-bind="$attrs">
    <CardGrid v-for="item in groupItems" :key="item" style="cursor:pointer" @click="go(item)">
      <span class="flex flex-col items-center">
        <SvgIcon :name="item.icon" :weight="item.size.width" :height ="item.size.height" />
        <span class="text-md mt-2">{{ item.title }}</span>
<!--        <span class="mt-2 h-10 text-secondary">{{ item.desc }}</span>-->
      </span>
    </CardGrid>
  </Card>
  <Drawer @register="registerDrawer" @success="handleSuccess" />

</template>
<script lang="ts" setup>
import { Card, message } from "ant-design-vue";
  import { GroupItem, groupItems } from "./data";
  import SvgIcon from "/@/components/Icon/src/SvgIcon.vue";
  import { openWindow } from "/@/utils";
  import { useGo } from "/@/hooks/web/usePage";
  const CardGrid = Card.Grid;
  import Drawer from '/@/views/apply_access/drawer.vue';
  import { useDrawer } from "/@/components/Drawer";
  import { useI18n } from "/@/hooks/web/useI18n";
  const { t } = useI18n();

  const [registerDrawer, { openDrawer }] = useDrawer();
  function handleSuccess() {
    message.success(t('common.successText'));
  }
  function go(item:GroupItem) {
    if (item.type === "url") {
      openWindow(item.path);
    } else if (item.type === "model") {
      openDrawer(true, {
        isUpdate: false,
      });
    }
    else {
      const go = useGo();
      // 执行刷新
      go(item.path);
    }
    console.log(item.path);
  }

</script>
