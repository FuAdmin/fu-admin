<template>
  <div class="m-4 mr-0 overflow-hidden bg-white">
    <BasicTree
      v-if="treeData.length"
      toolbar
      search
      showLine
      :clickRowToExpand="false"
      :treeData="treeData"
      defaultExpandAll
      :fieldNames="{ key: 'id', title: 'name' }"
      @select="handleSelect"
    />
  </div>
</template>
<script lang="ts">
  import { defineComponent, onMounted, ref } from 'vue';
  import { getDeptList } from '../dept/dept.api';

  import { BasicTree, TreeItem } from '/@/components/Tree';
  import XEUtils from 'xe-utils';

  export default defineComponent({
    name: 'DeptTree',
    components: { BasicTree },

    emits: ['select'],
    setup(_, { emit }) {
      const treeData = ref<TreeItem[]>([]);

      async function fetch() {
        treeData.value = (await getDeptList({})) as unknown as TreeItem[];
      }

      function handleSelect(keys, event) {
        console.log(keys);
        const data = XEUtils.toTreeArray(event.selectedNodes);
        let dept_ids: number[] = [];
        data.forEach((item) => {
          return dept_ids.push(item.id);
        });
        if (dept_ids.length) emit('select', dept_ids);
      }

      onMounted(() => {
        fetch();
      });
      return { treeData, handleSelect };
    },
  });
</script>
