<template>
  <BasicTree
    :treeData="menuTreeData"
    :fieldNames="{ title: 'title', key: 'id' }"
    :checkedKeys="checkedKeys"
    v-model:value="checkTreeData"
    :selectable = false
    checkable
    show-icon
    title="菜单权限"
    @check="check"
    checkStrictly
    ref="treeRef"
  />
</template>
<script lang="ts">
  import { defineComponent, nextTick, onMounted, ref, unref } from 'vue';
  import { BasicTree, TreeActionType, TreeItem } from '/@/components/Tree';
  import { getMenuList } from '/@/views/fuadmin/system/role/role.api';

  export default defineComponent({
    name: 'MenuPermission',
    components: { BasicTree },
    props: {
      checkedKeys: {
        type: Array,
        default: null,
      },
    },
    emits: ['success', 'register', 'menuData'],
    setup(_, { emit }) {
      const checkTreeData = ref([]);
      //树的选中的节点信息
      const selectedKeys = ref([]);

      const menuTreeData = ref<TreeItem[]>([]);
      const treeRef = ref<Nullable<TreeActionType>>(null);

      // onMounted(async () => {
      //   menuTreeData.value = await getMenuList();
      //   nextTick(() => {
      //     console.log(unref(treeRef));
      //     unref(treeRef)?.expandAll(true);
      //   });
      // });

      async function loadData() {
        menuTreeData.value = await getMenuList();
        nextTick(() => {
          console.log(unref(treeRef));
          unref(treeRef)?.expandAll(true);
        });
      }

      // watch(
      //   () => checkTreeData.value,
      //   (checkTreeData) => {
      //     nextTick(() => {
      //       emit('menuData', checkTreeData);
      //     });
      //   },
      // );

      function check(val, e) {
        // const parent = e.halfCheckedKeys;
        // const checkData = val.concat(parent);
        const checkData = val.checked;
        nextTick(() => {
          emit('menuData', { checkChildMenuData: val, checkMenuData: checkData });
        });
      }

      return {
        checkTreeData,
        selectedKeys,
        menuTreeData,
        treeRef,
        loadData,
        check,
      };
    },
  });
</script>
