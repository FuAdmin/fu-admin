<template>
  <Card
    :tab-list="tabListTitle"
    v-bind="$attrs"
    :active-tab-key="activeKey"
    @tab-change="onTabChange"
  >
    <p v-if="activeKey === 'tab1'">
      <LyMonitorLineEchart :model-value="network" />
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
  import { useI18n } from '/@/hooks/web/useI18n';

  defineProps({
    network: {
      type: Object,
      // eslint-disable-next-line vue/require-valid-default-prop
    },
  });

  const { t } = useI18n();

  const activeKey = ref('tab1');

  const tabListTitle = [
    {
      key: 'tab1',
      tab: t('common.monitor.networkTrafficTrendText'),
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
