<template>
  <VFormDesign @formConfig="getFormConfig"></VFormDesign>

</template>
<script lang="ts">
import { defineComponent, reactive, ref, watch } from "vue";
import VFormDesign from "/@/views/sys/form-design/components/VFormDesign/index.vue";


export default defineComponent({
  name: "formDesign",
  components: {VFormDesign},
  emits: ['designFormConfig'],
  setup(_, {emit}) {
    const getFormConfig = (val)=>{
      emit('designFormConfig', val)
    }

    return {
      getFormConfig,
    };
  },
});
</script>
