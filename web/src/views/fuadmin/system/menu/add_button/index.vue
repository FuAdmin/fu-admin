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
    <MenuButtonDrawer @register="registerDrawer" @success="handleSuccess" />
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, ref, unref } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';

  import { BasicDrawer, useDrawer, useDrawerInner } from '/@/components/Drawer';
  import { deleteItem, getList } from './menu_button.api';
  import { columns } from './menu_button.data';
  import MenuButtonDrawer from '/@/views/fuadmin/system/menu/add_button/MenuButtonDrawer.vue';

  export default defineComponent({
    name: 'AddMenuButton',
    components: { BasicTable, MenuButtonDrawer, BasicDrawer, TableAction },
    setup() {
      const [registerDrawer, { openDrawer }] = useDrawer();
      const menuId = ref(0);
      const [registerDrawerMenu] = useDrawerInner(async (data) => {
        menuId.value = data.id;
        await reload();
      });
      const getTitle = '添加菜单按钮';

      const [registerTable, { reload }] = useTable({
        api: getList,
        columns,
        showTableSetting: true,
        bordered: true,
        immediate: false,
        showIndexColumn: false,
        searchInfo: {
          menu_id: menuId,
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
          menuId: unref(menuId),
        });
      }

      function handleEdit(record: Recordable) {
        openDrawer(true, {
          record,
          isUpdate: true,
          menuId: unref(menuId),
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
