<template>
  <BasicDrawer
    v-bind="$attrs"
    @register="registerDrawer"
    showFooter
    :title="getTitle"
    width="50%"
    @ok="handleSubmit"
  >
    <Row :gutter="8">
      <Col :span="12">
        <BasicTree
          :treeData="treeData"
          :fieldNames="{ title: 'title', key: 'id' }"
          :checkedKeys="checkedKeys"
          :selectedKeys="selectedKeys"
          v-model:value="checkTreeData"
          checkable
          checkStrictly
          :defaultExpandAll="true"
          show-icon
          title="菜单权限"
          toolbar
          @select="onTreeNodeSelect"
        />
      </Col>

      <Col :span="12">
        <div class="vben-tree-header flex px-2 py-1.5 items-center">
          <span class="vben-basic-title" data-v-606afdb4="">数据权限</span>
        </div>
        <BasicForm style="padding-top: 16px" @register="registerForm" />
      </Col>
    </Row>
    <!--        <BasicForm @register="registerForm">-->
    <!--        </BasicForm>-->

    <!--    <Table-->
    <!--      :columns="columns"-->
    <!--      :defaultExpandAllRows="true"-->
    <!--      :dataSource="treeData"-->
    <!--    >-->
    <!--      <template #menu="{ record }">-->
    <!--        <Checkbox v-model:checked="record.checked">-->
    <!--          {{ record.title }}-->
    <!--        </Checkbox>-->
    <!--      </template>-->
    <!--      <template #button="{ record }">-->
    <!--        <span v-for="item in record.menu_button" :key="item.id">-->
    <!--          <Checkbox v-model:checked="item.checked">-->
    <!--            {{ item.name }}-->
    <!--          </Checkbox>-->
    <!--        </span>-->
    <!--      </template>-->
    <!--    </Table>-->
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, reactive, ref, unref } from 'vue';
  import { BasicDrawer, useDrawerInner } from '/@/components/Drawer';
  import { BasicTree, TreeItem } from '/@/components/Tree';
  import { BasicForm, useForm } from '/@/components/Form';

  import { createOrUpdate, getMenuList } from './role.api';
  import { Row, Col } from 'ant-design-vue';
  import XEUtils from 'xe-utils';
  import { formPermissionSchema } from '/@/views/fuadmin/system/role/role.data';
  import { getDeptList } from '/@/views/fuadmin/system/dept/dept.api';

  export default defineComponent({
    name: 'PermissionDrawer',
    components: { BasicDrawer, BasicForm, BasicTree, Col, Row },
    emits: ['success', 'register'],
    setup(_, { emit }) {
      const checkTreeData = ref([]);
      let treeData = ref<TreeItem[]>([]);
      //树的选择节点信息
      let checkedKeys = ref([]);
      //树的选中的节点信息
      const selectedKeys = ref([]);
      const isUpdate = ref(true);
      let thisRoledata = reactive({});
      const [registerForm, { resetFields, updateSchema, setFieldsValue, getFieldsValue }] = useForm(
        {
          labelWidth: 80,
          schemas: formPermissionSchema,
          showActionButtonGroup: false,
          baseColProps: { lg: 24, md: 24 },
        },
      );

      /**
       * 点击选中
       */
      function onCheck(o) {
        console.log(o);
        checkTreeData.value = o.checked ? o.checked : o;
      }

      /**
       * 选中节点
       */
      function onTreeNodeSelect(key) {
        if (key && key.length > 0) {
          selectedKeys.value = key;
        }
      }

      const [registerDrawer, { setDrawerProps, closeDrawer, changeLoading }] = useDrawerInner(
        async (data) => {
          changeLoading(true);
          await resetFields();
          setDrawerProps({ confirmLoading: false });
          isUpdate.value = !!data?.isUpdate;

          treeData.value = await getMenuList();

          treeData.value = XEUtils.toArrayTree(treeData.value, {
            parentKey: 'parent_id',
            strict: true,
          });
          const treeDeptData = await getDeptList();
          await updateSchema([
            {
              field: 'dept',
              componentProps: { treeData: treeDeptData },
            },
          ]);
          thisRoledata = data.record;
          const menu = thisRoledata.menu;
          const button = thisRoledata.permission.map((item) => {
            return 'b' + item;
          });
          checkedKeys.value = menu.concat(button);
          await setFieldsValue({
            ...data.record,
          });
          changeLoading(false);
        },
      );

      const getTitle = '权限分配';

      async function handleSubmit() {
        try {
          setDrawerProps({ confirmLoading: true });
          // TODO custom api
          let menu_ids = [];
          let button_ids = [];
          console.log(thisRoledata, unref(checkTreeData));
          const treeValue = unref(checkTreeData).checked
            ? unref(checkTreeData).checked
            : unref(checkTreeData);
          treeValue.forEach((item) => {
            if (item.toString().search('b')) {
              menu_ids.push(item);
            } else {
              button_ids.push(Number(item.slice(1)));
            }
          });
          const dataPermission = getFieldsValue();

          await createOrUpdate(
            {
              ...thisRoledata,
              menu: menu_ids,
              permission: button_ids,
              dept: dataPermission.dept,
              data_range: dataPermission.data_range,
            },
            unref(isUpdate),
          );

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
        treeData,
        registerForm,
        checkTreeData,
        checkedKeys,
        onCheck,
        selectedKeys,
        onTreeNodeSelect,
      };
    },
  });
</script>
