<template>
  <div>
    <BasicTable @register="registerTable">
      <template #toolbar>
        <a-button type="primary" v-auth="['post:add']" @click="handleCreate"> 新增 </a-button>
      </template>
      <template #action="{ record }">
        <TableAction
          :actions="[
            {
              type: 'button',
              icon: 'clarity:note-edit-line',
              color: 'primary',
              auth: ['post:update'],
              onClick: handleEdit.bind(null, record),
            },
            {
              icon: 'ant-design:delete-outlined',
              type: 'button',
              color: 'error',
              placement: 'left',
              auth: ['post:delete'],
              popConfirm: {
                title: '是否确认删除',
                confirm: handleDelete.bind(null, record.id),
              },
            },
          ]"
        />
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

  import { deleteItem, getList } from './api';
  import { columns } from './data';
  import { message } from 'ant-design-vue';

  export default defineComponent({
    name: 'Crontab',
    components: { BasicTable, Drawer, TableAction },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      // const { createMessage } = useMessage();
      const { hasPermission } = usePermission();
      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        title: '任务定时',
        maxHeight: 210,
        useSearchForm: false,
        showTableSetting: true,
        tableSetting: {
          // 是否显示刷新按钮
          redo: true,
          // 是否显示尺寸调整按钮
          size: false,
          // 是否显示字段调整按钮
          setting: false,
          // 是否显示全屏按钮
          fullScreen: false,
        },
        bordered: true,
        showIndexColumn: false,
        actionColumn: {
          width: 80,
          title: '操作',
          dataIndex: 'action',
          slots: { customRender: 'action' },
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

      async function handleDelete(id: number) {
        await deleteItem(id);
        message.success('删除成功');
        await reload();
      }

      function handleSuccess() {
        message.success('请求成功');
        reload();
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        hasPermission,
      };
    },
  });
</script>
