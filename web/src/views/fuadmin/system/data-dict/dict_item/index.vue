<template>
  <BasicDrawer v-bind="$attrs" @register="registerDrawerMenu" :title="getTitle" width="50%">
    <BasicTable @register="registerTable">
      <template #tableTitle>
        <a-button type="primary" @click="handleCreate"> 新增 </a-button>
      </template>
      <template #action="{ record }">
        <TableAction
          :actions="[
            {
              type: 'button',
              icon: 'clarity:note-edit-line',
              color: 'primary',
              onClick: handleEdit.bind(null, record),
            },
            {
              icon: 'ant-design:delete-outlined',
              type: 'button',
              color: 'error',
              placement: 'left',
              popConfirm: {
                title: '是否确认删除',
                confirm: handleDelete.bind(null, record.id),
              },
            },
          ]"
        />
      </template>
    </BasicTable>
    <DictItemDrawer @register="registerDrawer" @success="handleSuccess" />
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, ref, unref } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';

  import { BasicDrawer, useDrawer, useDrawerInner } from '/@/components/Drawer';
  import { deleteItem, getList } from './dict_item.api';
  import { columns } from './dict_item.data';
  import DictItemDrawer from './DictItemDrawer.vue';

  export default defineComponent({
    name: 'AddMenuButton',
    components: { BasicTable, DictItemDrawer, BasicDrawer, TableAction },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const dictId = ref(0);
      const [registerDrawerMenu] = useDrawerInner(async (data) => {
        dictId.value = data.id;
        await reload();
      });
      const getTitle = '字典列表';

      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        showTableSetting: true,
        bordered: true,
        immediate: false,
        showIndexColumn: false,
        searchInfo: {
          dict_id: dictId,
        },
        actionColumn: {
          width: 50,
          title: '操作',
          dataIndex: 'action',
          slots: { customRender: 'action' },
          fixed: 'right',
        },
      });

      function handleCreate() {
        openDrawer(true, {
          isUpdate: false,
          dictId: unref(dictId),
        });
      }

      function handleEdit(record: Recordable) {
        openDrawer(true, {
          record,
          isUpdate: true,
          dictId: unref(dictId),
        });
      }

      async function handleDelete(id: number) {
        await deleteItem(id);
        await reload();
      }

      function handleSuccess() {
        reload();
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        registerDrawerMenu,
        getTitle,
      };
    },
  });
</script>
