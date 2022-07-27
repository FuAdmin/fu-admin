<template>
  <Card
    :tab-list="tabListTitle"
    v-bind="$attrs"
    :active-tab-key="activeKey"
    @tab-change="onTabChange"
  >
    <p v-if="activeKey === 'tab1'">
      <LyMonitorLineEchart v-model="network" />
    </p>
    <p v-if="activeKey === 'tab2'">
      <!--      <VisitAnalysisBar />-->
    </p>
  </Card>
</template>
<script lang="ts" setup>
  import { ref } from 'vue';
  import { Card } from 'ant-design-vue';
  import LyMonitorLineEchart from './lineEchart.vue';

  defineProps({
    network: {
      type: Object,
      // eslint-disable-next-line vue/require-valid-default-prop
    },
  });

  const activeKey = ref('tab1');

  const tabListTitle = [
    {
      key: 'tab1',
      tab: '流量趋势',
    },
    // {
    //   key: 'tab2',
    //   tab: '访问量',
    // },
  ];

  function onTabChange(key) {
    activeKey.value = key;
  }
</script>
