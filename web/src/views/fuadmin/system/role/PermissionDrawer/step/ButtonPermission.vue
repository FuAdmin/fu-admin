<template>
  <BasicTree
    :treeData="buttonTreeData"
    :fieldNames="{ title: 'title', key: 'id' }"
    :checkedKeys="checkedKeys"
    v-model:value="checkTreeData"
    checkable
    show-icon
    title="按钮权限"
    toolbar
    @check="check"
    ref="treeRef"
  />
</template>
<script lang="ts">
  import { defineComponent, nextTick, onMounted, onUpdated, ref, toRefs, unref, watch } from 'vue';
  import { BasicTree, TreeActionType, TreeItem } from '/@/components/Tree';
  import { getMenuButtonList } from '../../role.api';
  import XEUtils from 'xe-utils';

  export default defineComponent({
    name: 'ButtonPermission',
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
    emits: ['success', 'register', 'buttonData'],
    setup(props, { emit }) {
      const checkTreeData = ref([]);
      //树的选中的节点信息
      const buttonTreeData = ref<TreeItem[]>([]);
      const treeRef = ref<Nullable<TreeActionType>>(null);
      const propsData = toRefs(props);

      // onMounted(async () => {
      //   buttonTreeData.value = await getMenuButtonList();
      //   buttonTreeData.value = XEUtils.toArrayTree(buttonTreeData.value, {
      //     parentKey: 'parent_id',
      //     strict: true,
      //   });
      //   nextTick(() => {
      //     unref(treeRef)?.expandAll(true);
      //   });
      // });

      async function loadData() {
        buttonTreeData.value = await getMenuButtonList();
        buttonTreeData.value = XEUtils.toArrayTree(buttonTreeData.value, {
          parentKey: 'parent_id',
          strict: true,
        });
        nextTick(() => {
          unref(treeRef)?.expandAll(true);
        });
      }

      // onUpdated(() => {
      //   emit('buttonData', checkTreeData);
      // });

      // watch(
      //   () => checkTreeData.value,
      //   (checkTreeData) => {
      //     console.log(111, checkTreeData);
      //     nextTick(() => {
      //       emit('buttonData', checkTreeData);
      //     });
      //   },
      //   { immediate: false },
      // );

      function check(val) {
        nextTick(() => {
          emit('buttonData', val);
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
