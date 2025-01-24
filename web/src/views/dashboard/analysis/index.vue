<template>
  <div>
    <div class="p-4">
      <GrowCard :loading="loading" class="enter-y" />
      <SiteAnalysis class="!my-4 enter-y" :loading="loading" />
      <div class="md:flex enter-y">
        <VisitRadar class="md:w-1/3 w-full" :loading="loading" />
        <VisitSource class="md:w-1/3 !md:mx-4 !md:my-0 !my-4 w-full" :loading="loading" />
        <SalesProductPie class="md:w-1/3 w-full" :loading="loading" />
      </div>
    </div>
    <Modal
      :closable="false"
      v-model:open="open"
      title="Fu Admin"
      @ok="handleOk"
      centered
      width="40%"
      cancel-text="关闭"
      ok-text="立即体验"
    >
      <template #footer>
        <Space>
          <Button @click="handleCancel"> 暂不体验 </Button>
        </Space>
      </template>
      <div style="padding: 10px 20px">
        <b>🔥工作流</b> 已发布， 源码地址：<a :href="url" target="_blank">
          {{ url }}
        </a>
      </div>
      <div style="padding: 10px 20px">
        <b>🔥Fu FastApi 开源版</b> 已发布， 源码地址：<a :href="fastApiOpenUrl" target="_blank">
          {{ fastApiOpenUrl }}
        </a>
      </div>
      <div style="padding: 10px 20px">
        <b>🌟Fu Admin Pro</b> 已发布， 体验地址：<a :href="url" target="_blank">
          {{ url }}
        </a>
      </div>
      <div style="padding: 10px 20px">
        <b>🌟Fu FastApi Pro</b> 已发布， 体验地址：<a :href="fastApiUrl" target="_blank">
          {{ fastApiUrl }}
        </a>
      </div>
    </Modal>
  </div>
</template>
<script lang="ts" setup>
  import { ref } from 'vue';
  import GrowCard from './components/GrowCard.vue';
  import SiteAnalysis from './components/SiteAnalysis.vue';
  import VisitSource from './components/VisitSource.vue';
  import VisitRadar from './components/VisitRadar.vue';
  import SalesProductPie from './components/SalesProductPie.vue';
  import { Modal, Button, Space } from 'ant-design-vue';

  const loading = ref(true);
  const open = ref(true);

  const url = 'http://124.222.210.96:8080';

  const fastApiUrl = 'http://124.222.210.96:7070';

  const fastApiOpenUrl = 'https://gitee.com/fuadmin/fu-fastapi-vue';

  setTimeout(() => {
    loading.value = false;
  }, 1500);

  const handleOk = () => {
    window.location.href = url;
    open.value = false;
  };
  const handleCancel = () => {
    open.value = false;
  };
</script>
