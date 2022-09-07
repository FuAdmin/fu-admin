<template>
  <BasicDrawer
    v-bind="$attrs"
    @register="registerDrawer"
    showFooter
    :title="getTitle"
    width="50%"
    @ok="handleSubmit"
  >
    <BasicForm @register="registerForm" />
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, ref, computed, unref } from 'vue';
  import { BasicForm, useForm } from '/@/components/Form/index';
  import { BasicDrawer, useDrawerInner } from '/@/components/Drawer';
  import { createOrUpdate } from './api';
  import { formSchema } from './data';
  import { getAllList as getCrontabList } from '/@/views/fuadmin/system/celery/crontab/api';
  import { getAllList as getIntervalList } from '/@/views/fuadmin/system/celery/interval/api';
  import { getCrontabData, getIntervalData } from '/@/views/fuadmin/system/celery/util';
  import { useI18n } from '/@/hooks/web/useI18n';

  export default defineComponent({
    name: 'ButtonDrawer',
    components: { BasicDrawer, BasicForm },
    emits: ['success', 'register'],
    setup(_, { emit }) {
      const isUpdate = ref(true);
      const { t } = useI18n();

      const [registerForm, { resetFields, setFieldsValue, updateSchema, validate }] = useForm({
        labelWidth: 100,
        schemas: formSchema,
        showActionButtonGroup: false,
        baseColProps: { lg: 12, md: 24 },
      });

      const [registerDrawer, { setDrawerProps, closeDrawer }] = useDrawerInner(async (data) => {
        await resetFields();
        setDrawerProps({ confirmLoading: false });
        isUpdate.value = !!data?.isUpdate;
        if (unref(isUpdate)) {
          // crontab和interval本来是对象，现在转换为id
          const record = data.record;
          const crontab = record.crontab ? record.crontab.id : undefined;
          const interval = record.interval ? record.interval.id : undefined;
          await setFieldsValue({
            ...record,
            crontab,
            interval,
          });
        }
        let crontabList = await getCrontabList();
        crontabList = crontabList.map((item) => {
          item.label = getCrontabData(item);
          return item;
        });
        let intervalList = await getIntervalList();
        intervalList = intervalList.map((item) => {
          item.label = getIntervalData(item);
          return item;
        });

        await updateSchema([
          {
            field: 'interval',
            componentProps: ({ formModel }) => {
              return {
                fieldNames: {
                  label: 'label',
                  key: 'id',
                  value: 'id',
                },
                options: intervalList,
                onChange: () => {
                  formModel.crontab = undefined;
                },
              };
            },
          },
          {
            field: 'crontab',
            componentProps: ({ formModel }) => {
              return {
                fieldNames: {
                  label: 'label',
                  key: 'id',
                  value: 'id',
                },
                options: crontabList,
                onChange: () => {
                  formModel.interval = undefined;
                },
              };
            },
          },
        ]);
      });

      const getTitle = computed(() =>
        !unref(isUpdate) ? t('common.addText') : t('common.updateText'),
      );

      async function handleSubmit() {
        try {
          const values = await validate();
          setDrawerProps({ confirmLoading: true });
          await createOrUpdate(values, unref(isUpdate));
          closeDrawer();
          emit('success');
        } finally {
          setDrawerProps({ confirmLoading: false });
        }
      }

      return {
        registerDrawer,
        registerForm,
        getTitle,
        handleSubmit,
      };
    },
  });
</script>
