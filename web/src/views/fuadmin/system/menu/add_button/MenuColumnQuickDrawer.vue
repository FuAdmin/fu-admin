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
      <a-input
        v-model:value="url"
        placeholder="/api/demo/demo"
        addon-before="URL"
        allowClear
        style="width: calc(100% - 80px)"
      >
        <template #suffix>
          <BasicHelp
            placement="top"
            class="mx-1"
            text="输入获取数据的api，例如项目演示中的GET api：/api/demo/demo"
          />
        </template>
      </a-input>
      <a-button type="primary" style="width: 70px" :loading="buttonLoanding" @click="loadField">{{
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
                  confirm: handleDelete.bind(null, record),
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
  import { batchCreate } from '/@/views/fuadmin/system/menu/add_button/menu_column_field.api';
  import { InfoCircleOutlined } from '@ant-design/icons-vue';
  import { Tooltip } from 'ant-design-vue';
  import BasicHelp from "/@/components/Basic/src/BasicHelp.vue";

  export default defineComponent({
    name: 'MenuColumnQuickDrawer',
    components: {BasicHelp, BasicDrawer, TableAction, BasicTable, InfoCircleOutlined, Tooltip },
    emits: ['success', 'register'],
    setup(_, { emit }) {
      const { t } = useI18n();

      let tableData = ref();
      const path = ref();
      const url = ref();
      let buttonLoading = ref(false);
      let menuId = '';

      const [registerDrawer, { setDrawerProps, closeDrawer }] = useDrawerInner(async (data) => {
        setDrawerProps({ confirmLoading: false });
        path.value = data.path;
        menuId = data.menuId;
      });
      const [registerTable, { reload, deleteTableDataRecord }] = useTable({
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
        buttonLoading.value = true;
        const returnData = await defHttp.get({ url: unref(url) });
        if (returnData.items.length > 0) {
          const item = returnData.items[0];
          const fields = Object.keys(item);
          tableData.value = fields.map((item) => {
            return {
              name: item,
              code: path.value + ':' + item,
              menu_id: menuId,
            };
          });
        }
        buttonLoading.value = false;
      }

      async function handleDelete(record) {
        deleteTableDataRecord(record.key);
        tableData.value = unref(tableData).filter((item) => item.code !== record.code);
        await reload();
      }
      async function handleSubmit() {
        try {
          setDrawerProps({ confirmLoading: true });
          await batchCreate({ batch_info: unref(tableData) });
          tableData.value = [];
          url.value = '';
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
        buttonLoanding: buttonLoading,
        url,
        t,
      };
    },
  });
</script>
