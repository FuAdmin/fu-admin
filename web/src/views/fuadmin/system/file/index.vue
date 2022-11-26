<template>
  <div>
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <Space style="height: 40px">
          <BasicUpload :maxSize="20" :maxNumber="10" @change="handleChange" class="my-5" />
        </Space>
      </template>
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <TableAction
            :actions="[
              {
                type: 'button',
                icon: 'bi:eye',
                color: 'success',
                auth: ['post:update'],
                onClick: handleEdit.bind(null, record),
              },
              {
                type: 'button',
                icon: 'ant-design:cloud-download-outlined',
                color: 'primary',
                auth: ['post:update'],
                onClick: handleDownload.bind(null, record),
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <Drawer @register="registerDrawer" @success="handleSuccess" />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { usePermission } from '/@/hooks/web/usePermission';
  import { useDrawer } from '/@/components/Drawer';
  import Drawer from './Drawer.vue';
  import { deleteItem, download, getList } from './api';
  import { columns, searchFormSchema } from './data';
  import { message, Space } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { BasicUpload } from '/@/components/Upload';
  import { downloadByData } from '/@/utils/file/download';
  import { useI18n } from '/@/hooks/web/useI18n';
  export default defineComponent({
    name: 'CeleryLogManagement',
    components: { BasicTable, Drawer, BasicUpload, TableAction, Space },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const { createMessage } = useMessage();
      const { hasPermission } = usePermission();
      const { t } = useI18n();
      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
        },
        useSearchForm: true,
        showTableSetting: true,
        tableSetting: { fullScreen: true },
        bordered: true,
        showIndexColumn: false,
        actionColumn: {
          width: 80,
          title: t('common.operationText'),
          dataIndex: 'action',
          fixed: undefined,
        },
      });

      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
        });
      }

      function handleEdit(record: Recordable) {
        openDrawer(true, {
          record,
          isUpdate: true,
        });
      }

      async function handleDownload(record: Recordable) {
        const response = await download(record);
        await downloadByData(response.data, record.name);
        // downloadByData('text content', 'testName.txt');
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success(t('common.successText'));
        await reload();
      }

      function handleSuccess() {
        message.success(t('common.successText'));
        reload();
      }

      async function handleChange() {
        createMessage.info(`上传成功`);
        await reload();
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        handleChange,
        hasPermission,
        handleDownload,
      };
    },
  });
</script>
