<template>
  <BasicDrawer
    v-bind="$attrs"
    @register="registerDrawer"
    showFooter
    :title="getTitle"
    width="40%"
    @ok="handleSubmit"
  >
    <a-input-group compact style="padding: 6px">
      <a-input v-model:value="url" addon-before="URL" style="width: calc(100% - 64px)" />
      <a-button type="primary" style="width: 64px" @click="loadField">{{
        t('common.loadText')
      }}</a-button>
    </a-input-group>

    <BasicTable @register="registerTable">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <TableAction
            :actions="[
              {
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                placement: 'left',
                auth: ['demo:delete'],
                popConfirm: {
                  title: t('common.delHintText'),
                  confirm: handleDelete.bind(null, record.id),
                },
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, ref, unref } from 'vue';
  import { columnsQuick } from './menu_column_field.data';
  import { BasicDrawer, useDrawerInner } from '/@/components/Drawer';
  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { useI18n } from '/@/hooks/web/useI18n';
  import { defHttp } from '/@/utils/http/axios';

  export default defineComponent({
    name: 'MenuColumnQuickDrawer',
    components: { BasicDrawer, TableAction, BasicTable },
    emits: ['success', 'register'],
    setup(_, { emit }) {
      const { t } = useI18n();

      let tableData = ref();
      const path = ref();
      const url = ref();
      const [registerDrawer, { setDrawerProps, closeDrawer }] = useDrawerInner(async (data) => {
        setDrawerProps({ confirmLoading: false });
        path.value = data.path;
      });
      const [registerTable, { reload, getSelectRows }] = useTable({
        dataSource: tableData,
        columns: columnsQuick,
        useSearchForm: false,
        showTableSetting: false,
        tableSetting: { fullScreen: true },
        bordered: true,
        showIndexColumn: true,
        actionColumn: {
          width: 50,
          title: t('common.operationText'),
          dataIndex: 'action',
          fixed: undefined,
        },
      });
      const getTitle = '快速导入';

      async function loadField() {
        const returnData = await defHttp.get({ url: unref(url) });
        if (returnData.items.length > 0) {
          const item = returnData.items[0];
          const fields = Object.keys(item);
          tableData.value = fields.map((item) => {
            return {
              name: item,
              code: path.value + ':' + item,
            };
          });
          console.log(tableData.value);
        }
      }

      async function handleDelete(id: number) {
        await reload();
      }
      async function handleSubmit() {
        try {
          setDrawerProps({ confirmLoading: true });

          closeDrawer();
          emit('success');
        } finally {
          setDrawerProps({ confirmLoading: false });
        }
      }

      return {
        registerDrawer,
        getTitle,
        handleSubmit,
        registerTable,
        loadField,
        handleDelete,
        tableData,
        url,
        t,
      };
    },
  });
</script>
