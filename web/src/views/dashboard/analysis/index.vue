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
      title="Fu Admin Pro"
      @ok="handleOk"
      centered
      cancel-text="关闭"
      ok-text="立即体验"
    >
      <div style="padding: 10px 20px">
        <b>Fu Admin Pro</b> 已发布， 体验地址：<a :href="url" target="_blank">
          {{ url }}
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
  import { Modal } from 'ant-design-vue';

  const loading = ref(true);
  const open = ref(true);

  const url = 'http://124.222.210.96:6060';

  setTimeout(() => {
    loading.value = false;
  }, 1500);

  const handleOk = () => {
    window.location.href = url;
    open.value = false;
  };
</script>
