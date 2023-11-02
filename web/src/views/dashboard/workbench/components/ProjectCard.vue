<template>
  <Card title="项目" v-bind="$attrs">
    <CardGrid v-for="item in items" :key="item" class="!md:w-1/3 !w-full" @click="go(item)">
      <span class="flex">
        <SvgIcon :name="item.icon" :color="item.color" size="50" />
        <span class="text-lg ml-4">{{ item.title }}</span>
      </span>
      <div class="flex mt-2 h-10 text-secondary">{{ item.desc }}</div>
      <div class="flex justify-between text-secondary">
<!--        <span>{{ item.group }}</span>-->
<!--        <span>{{ item.date }}</span>-->
      </div>
    </CardGrid>
  </Card>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';
  import { Card } from 'ant-design-vue';
  import Icon from '/@/components/Icon/Icon.vue';
  import { GroupItem, groupItems } from './data';
  import { openWindow } from "/@/utils";
  import { useGo } from '/@/hooks/web/usePage';
  import SvgIcon from "/@/components/Icon/src/SvgIcon.vue";

  export default defineComponent({
    components: { SvgIcon, Card, CardGrid: Card.Grid, Icon },
    setup() {
      function go(item:GroupItem) {
        if (item.type === "url") {
          openWindow(item.path);
        } else {
          const go = useGo();
          // 执行刷新
          go(item.path);
        }
        console.log(item.path);
      }
      return { items: groupItems, go };
    },
  });
</script>
