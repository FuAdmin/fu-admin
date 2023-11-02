<template>
  <PageWrapper dense contentFullHeight contentClass="flex">
    <DeptTree class="w-1/4 xl:w-1/5" @select="handleSelect" />
    <BasicTable @register="registerTable" class="w-3/4 xl:w-4/5" :searchInfo="searchInfo">
      <template #tableTitle>
        <Space style="height: 40px">
          <a-button
            type="primary"
            v-auth="['user:add']"
            preIcon="ant-design:plus-outlined"
            @click="handleCreate"
          >
            {{ t('common.addText') }}
          </a-button>

          <a-button
            type="error"
            v-auth="['user:delete']"
            preIcon="ant-design:delete-outlined"
            @click="handleBulkDelete"
          >
            {{ t('common.delText') }}
          </a-button>
        </Space>
      </template>
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <TableAction
            :actions="[
              {
                type: 'button',
                icon: 'clarity:note-edit-line',
                color: 'primary',
                auth: ['user:update'],
                disabled: record.id === 1,
                onClick: handleEdit.bind(null, record),
              },
              {
                icon: 'ant-design:delete-outlined',
                type: 'button',
                color: 'error',
                placement: 'left',
                auth: ['user:delete'],
                disabled: record.id === 1,
                popConfirm: {
                  title: t('common.delHintText'),
                  confirm: handleDelete.bind(null, record.id),
                },
              },
              {
                type: 'button',
                icon: 'ant-design:key-outlined',
                color: 'warning',
                auth: ['user:update'],
                tooltip: t('common.account.resetPassword'),
                disabled: record.id === 1,
                popConfirm: {
                  title: t('common.account.resetPasswordHit'),
                  confirm: rePassword.bind(null, record.id),
                },
              },
            ]"
          />
        </template>
      </template>
    </BasicTable>
    <AccountModal @register="registerDrawer" @success="handleSuccess" />
  </PageWrapper>
</template>
<script lang="ts">
  import { defineComponent, reactive } from 'vue';

  import { BasicTable, useTable, TableAction } from '/@/components/Table';
  import { PageWrapper } from '/@/components/Page';

  import { useDrawer } from '/@/components/Drawer';
  import AccountModal from './AccountDrawer.vue';
  import DeptTree from './DeptTree.vue';
  import { columns, searchFormSchema } from './account.data';
  import { useGo } from '/@/hooks/web/usePage';
  import { getList, deleteItem, repassword, resetPassword } from './account.api';
  import { message, Space } from 'ant-design-vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { useI18n } from '/@/hooks/web/useI18n';
  export default defineComponent({
    name: 'AccountManagement',
    components: { BasicTable, PageWrapper, AccountModal, TableAction, Space, DeptTree },
    setup() {
      const { t } = useI18n();
      const go = useGo();
      const [registerDrawer, { openDrawer }] = useDrawer();
      const { createConfirm } = useMessage();
      const searchInfo = reactive<Recordable>({});
      const [registerTable, { reload, updateTableDataRecord, getSelectRows }] = useTable({
        api: getList,
        rowKey: 'id',
        columns,
        formConfig: {
          labelWidth: 80,
          schemas: searchFormSchema,
          autoSubmitOnEnter: true,
        },
        useSearchForm: true,
        tableSetting: { fullScreen: true },
        showTableSetting: true,
        bordered: true,
        handleSearchInfoFn(info) {
          return info;
        },
        rowSelection: {
          type: 'checkbox',
          getCheckboxProps(record: Recordable) {
            // Demo: 第一行（id为0）的选择框禁用
            if (record.id === 1) {
              return { disabled: true };
            } else {
              return { disabled: false };
            }
          },
        },
        actionColumn: {
          width: 200,
          title: t('common.operationText'),
          dataIndex: 'action',
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
        await reload();
      }

      async function rePassword(id: number) {
        await resetPassword(id);
        message.success(t('common.successText'));
      }

      function handleBulkDelete() {
        if (getSelectRows().length == 0) {
          message.warning(t('common.batchDelHintText'));
        } else {
          createConfirm({
            iconType: 'warning',
            title: t('common.hintText'),
            content: t('common.delHintText'),
            async onOk() {
              for (const item of getSelectRows()) {
                await deleteItem(item.id);
              }
              message.success(t('common.successText'));
              await reload();
            },
          });
        }
      }

      function handleSuccess({ isUpdate, values }) {
        if (isUpdate) {
          // 演示不刷新表格直接更新内部数据。
          // 注意：updateTableDataRecord要求表格的rowKey属性为string并且存在于每一行的record的keys中
          const result = updateTableDataRecord(values.id, values);
          console.log(result);
        } else {
          reload();
        }
      }

      function handleSelect(deptIds) {
        console.log(deptIds);
        searchInfo.dept_ids = deptIds;
        JSON.stringify();
        reload();
      }

      function handleView(record: Recordable) {
        go('/system/account_detail/' + record.id);
      }

      return {
        registerTable,
        registerDrawer,
        handleCreate,
        handleEdit,
        handleDelete,
        handleSuccess,
        handleSelect,
        handleView,
        searchInfo,
        handleBulkDelete,
        rePassword,
        t,
      };
    },
  });
</script>
