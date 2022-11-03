<template>
  <Cascader v-bind="attrs" :value="state" :options="getOptions" @change="handleChange" />
</template>
<script lang="ts">
  import { defineComponent, ref, watchEffect, computed } from 'vue';
  import { Cascader } from 'ant-design-vue';
  import {
    provinceAndCityData,
    regionData,
    provinceAndCityDataPlus,
    regionDataPlus,
  } from '../utils/areaDataUtil';
  import { useRuleFormItem } from '/@/hooks/component/useFormItem';
  import { propTypes } from '/@/utils/propTypes';
  import { useAttrs } from '/@/hooks/core/useAttrs';
  export default defineComponent({
    name: 'AreaLinkage',
    components: {
      Cascader,
    },
    inheritAttrs: false,
    props: {
      value: propTypes.oneOfType([propTypes.object, propTypes.array]),
      //是否显示区县
      showArea: propTypes.bool.def(true),
      //是否是全部
      showAll: propTypes.bool.def(false),
    },
    emits: ['change'],
    setup(props) {
      const emitData = ref<any[]>([]);
      const attrs = useAttrs();
      const [state] = useRuleFormItem(props, 'value', 'change', emitData);
      // eslint-disable-next-line vue/return-in-computed-property
      const getOptions = computed(() => {
        if (props.showArea && props.showAll) {
          return regionDataPlus;
        }
        if (props.showArea && !props.showAll) {
          return regionData;
        }
        if (!props.showArea && !props.showAll) {
          return provinceAndCityData;
        }
        if (!props.showArea && props.showAll) {
          return provinceAndCityDataPlus;
        }
      });
      /**
       * 监听value变化
       */
      watchEffect(() => {
        props.value && initValue();
      });

      /**
       * 将字符串值转化为数组
       */
      function initValue() {
        let value = props.value ? props.value : [];
        if (value && typeof value === 'string' && value != 'null' && value != 'undefined') {
          state.value = value.split(',');
        }
      }

      function handleChange(array, ...args) {
        emitData.value = args;
        //update-begin-author:taoyan date:2022-6-27 for: VUEN-1424【vue3】树表、单表、jvxe、erp 、内嵌子表省市县 选择不上
        // 上面改的v-model:value导致选中数据没有显示
        state.value = array;
        //update-end-author:taoyan date:2022-6-27 for: VUEN-1424【vue3】树表、单表、jvxe、erp 、内嵌子表省市县 选择不上
      }
      return {
        state,
        attrs,
        regionData,
        getOptions,
        handleChange,
      };
    },
  });
</script>
