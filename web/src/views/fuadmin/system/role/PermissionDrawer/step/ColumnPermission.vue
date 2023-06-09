<template>
  <BasicTree
    :treeData="buttonTreeData"
    :fieldNames="{ title: 'title', key: 'id' }"
    :checkedKeys="checkedKeys"
    v-model:value="checkTreeData"
    checkable
    show-icon
    title="列表权限"
    :selectable = false
    toolbar
    @check="check"
    ref="treeRef"
  />
</template>
<script lang="ts">
  import { defineComponent, nextTick, onMounted, ref, toRefs, unref, watch } from 'vue';
  import { BasicTree, TreeActionType, TreeItem } from '/@/components/Tree';
  import { getMenuColumnList } from '../../role.api';
  import XEUtils from 'xe-utils';

  export default defineComponent({
    name: 'ColumnPermission',
    components: { BasicTree },
    props: {
      menuIds: {
        type: Array,
        default: null,
      },
      checkedKeys: {
        type: Array,
        default: null,
      },
    },
    emits: ['success', 'register', 'columData'],
    setup(props, { emit }) {
      const checkTreeData = ref([]);
      //树的选中的节点信息
      const buttonTreeData = ref<TreeItem[]>([]);
      const treeRef = ref<Nullable<TreeActionType>>(null);
      const propsData = toRefs(props);

      // onMounted(async () => {
      //   buttonTreeData.value = await getMenuColumnList();
      //   buttonTreeData.value = XEUtils.toArrayTree(buttonTreeData.value, {
      //     parentKey: 'parent_id',
      //     strict: true,
      //   });
      //   nextTick(() => {
      //     unref(treeRef)?.expandAll(true);
      //   });
      // });

      async function loadData() {
        buttonTreeData.value = await getMenuColumnList();
        buttonTreeData.value = XEUtils.toArrayTree(buttonTreeData.value, {
          parentKey: 'parent_id',
          strict: true,
        });
        nextTick(() => {
          unref(treeRef)?.expandAll(true);
        });
      }

      function check(val) {
        nextTick(() => {
          emit('columData', val);
        });
      }

      return {
        checkTreeData,
        buttonTreeData,
        treeRef,
        check,
        loadData,
      };
    },
  });
</script>
