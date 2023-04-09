<template>
  <div>
    <div class="vben-tree-header flex px-2 py-1.5 items-center">
      <span class="vben-basic-title" data-v-606afdb4="">数据权限</span>
    </div>
    <BasicForm style="padding-top: 16px" @register="registerForm" />
  </div>
</template>
<script lang="ts">
  import { defineComponent, nextTick, onMounted, ref, toRefs, unref, watch } from 'vue';

  import { getDeptList } from '../../../dept/dept.api';
  import { formPermissionSchema } from '../../role.data';
  import { BasicForm, useForm } from '/@/components/Form';

  export default defineComponent({
    name: 'DataPermission',
    components: { BasicForm },
    props: {
      menuIds: {
        type: Array,
        default: null,
      },
      recordData: {
        type: Object,
        default: null,
      },
    },
    emits: ['success', 'register', 'dataPerData'],
    setup(props, { emit }) {
      const { recordData } = toRefs(props);
      const [registerForm, { resetFields, updateSchema, setFieldsValue, getFieldsValue }] = useForm(
        {
          labelWidth: 80,
          schemas: formPermissionSchema,
          showActionButtonGroup: false,
          baseColProps: { lg: 24, md: 24 },
        },
      );
      // onMounted(async () => {
      //   const treeDeptData = await getDeptList({});
      //   await updateSchema([
      //     {
      //       field: 'dept',
      //       componentProps: { treeData: treeDeptData },
      //     },
      //   ]);
      //   setFieldsValue({ ...propsData.recordData });
      // });

      async function loadData() {
        const treeDeptData = await getDeptList({});
        await updateSchema([
          {
            field: 'dept',
            componentProps: { treeData: treeDeptData },
          },
        ]);

        nextTick(() => {
          console.log(111, props.recordData)
          setFieldsValue({ ...props.recordData });
        });
      }

      function getPerData() {
        const dataPermission = getFieldsValue();
        emit('dataPerData', dataPermission);
      }

      return {
        getPerData,
        registerForm,
        loadData,
      };
    },
  });
</script>
