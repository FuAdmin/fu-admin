<template>
  <VFormDesign @formConfig="getFormConfig" :formInfo="props.formInfo" />
</template>
<script lang="ts">
  import { defineComponent, ref } from 'vue';
  import VFormDesign from '/@/views/sys/form-design/components/VFormDesign/index.vue';

  export default defineComponent({
    name: 'FormDesign',
    components: { VFormDesign },
    props: {
      formInfo: Object,
    },
    emits: ['designFormConfig'],
    setup(props, { emit }) {
      const formRev = ref();
      const getFormConfig = (val) => {
        emit('designFormConfig', val);
      };
      return {
        getFormConfig,
        formRev,
        props,
      };
    },
  });
</script>
