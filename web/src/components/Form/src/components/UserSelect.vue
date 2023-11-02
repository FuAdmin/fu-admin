<template>
  <Select
    @dropdown-visible-change="handleFetch"
    v-bind="$attrs"
    show-search
    @change="handleChange"
    :options="getOptions"
    :filter-option="filterOption"
    v-model:value="state"
  >
    <template #option="{ value: val, label, desc }">
      <span class="option-label"> {{ label }} </span>
      <span class="option-description"> {{ desc }} </span>
    </template>

    <template #[item]="data" v-for="item in Object.keys($slots)">
      <slot :name="item" v-bind="data || {}"></slot>
    </template>
    <template #suffixIcon v-if="loading">
      <LoadingOutlined spin />
    </template>
    <template #notFoundContent v-if="loading">
      <span>
        <LoadingOutlined spin class="mr-1" />
        {{ t('component.form.apiSelectNotFound') }}
      </span>
    </template>
  </Select>
</template>
<script lang="ts">
  import { defineComponent, PropType, watchEffect, ref, computed, unref, watch } from 'vue';
  import { Select } from 'ant-design-vue';
  import type { SelectValue } from 'ant-design-vue/es/select';
  import { isFunction } from '/@/utils/is';
  import { useRuleFormItem } from '/@/hooks/component/useFormItem';
  import { useAttrs } from '@vben/hooks';
  import { get, omit } from 'lodash-es';
  import { LoadingOutlined } from '@ant-design/icons-vue';
  import { useI18n } from '/@/hooks/web/useI18n';
  import { propTypes } from '/@/utils/propTypes';
  import { getAllList } from "/@/views/fuadmin/system/account/account.api";
  import SvgIcon from '/@/components/Icon/src/SvgIcon.vue';

  type OptionsItem = { label: string; value: string; desc: string; disabled?: boolean };

  export default defineComponent({
    name: 'UserSelect',
    components: {
      SvgIcon,
      Select,
      LoadingOutlined,
    },
    inheritAttrs: false,
    props: {
      value: [Array, Object, String, Number],
      numberToString: propTypes.bool,
      dictCode: propTypes.string,
      // support xxx.xxx.xx
      resultField: propTypes.string.def(''),
      labelField: propTypes.string.def('name'),
      valueField: propTypes.string.def('username'),
      descField: propTypes.string.def('username'),
      immediate: propTypes.bool.def(true),
      alwaysLoad: propTypes.bool.def(false),
    },
    emits: ['options-change', 'change'],
    setup(props, { emit }) {
      const options = ref<OptionsItem[]>([]);
      const loading = ref(false);
      const isFirstLoad = ref(true);
      const emitData = ref<any[]>([]);
      const attrs = useAttrs();
      const { t } = useI18n();
      const api = getAllList;

      // Embedded in the form, just use the hook binding to perform form verification
      const [state] = useRuleFormItem(props, 'value', 'change', emitData);

      const getOptions = computed(() => {
        const { labelField, valueField, descField, numberToString } = props;

        return unref(options).reduce((prev, next: Recordable) => {
          if (next) {
            const value = next[valueField];
            prev.push({
              ...omit(next, [labelField, valueField]),
              label: next[labelField],
              value: numberToString ? `${value}` : value,
              desc: next[descField],
            });
          }
          return prev;
        }, [] as OptionsItem[]);
      });
      const filterOption = (input: string, option: any) => {
          return option.label.toLowerCase().indexOf(input.toLowerCase()) >= 0 || option.desc.toLowerCase().indexOf(input.toLowerCase()) >= 0
      };
      watchEffect(() => {
        props.immediate && !props.alwaysLoad && fetch();
      });

      watch(
        () => props.dictCode,
        () => {
          !unref(isFirstLoad) && fetch();
        },
        { deep: true },
      );

      async function fetch() {
        if (!api || !isFunction(api)) return;
        options.value = [];
        try {
          loading.value = true;
          const res = await api();
          if (Array.isArray(res)) {
            options.value = res;
            emitChange();
            return;
          }
          if (props.resultField) {
            options.value = get(res, props.resultField) || [];
          }
          emitChange();
        } catch (error) {
          console.warn(error);
        } finally {
          loading.value = false;
        }
      }

      async function handleFetch(visible) {
        if (visible) {
          if (props.alwaysLoad) {
            await fetch();
          } else if (!props.immediate && unref(isFirstLoad)) {
            await fetch();
            isFirstLoad.value = false;
          }
        }
      }

      function emitChange() {
        emit('options-change', unref(getOptions));
      }

      function handleChange(_, ...args) {
        emitData.value = args;
      }

      return { state, attrs, getOptions, loading, t, handleFetch, handleChange, filterOption };
    },
  });
</script>
<style>
.option-label {
  display: inline-block;
  width: 85%; /* 调整为合适的宽度 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.option-description {
  display: inline-block;
  width: 15%; /* 调整为合适的宽度 */
  //text-align: right;
  color: #999;
}
</style>
