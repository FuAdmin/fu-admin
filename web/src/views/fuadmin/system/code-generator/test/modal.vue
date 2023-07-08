<template>
  <BasicModal v-bind="$attrs" @register="registerModal" defaultFullscreen :canFullscreen=false
              :title="getTitle"
              @ok="handleSubmit">

    <BasicForm v-bind="attrs" @register="registerForm" />
  </BasicModal>
</template>
<script lang="ts">
import { defineComponent, ref, computed, unref, reactive } from "vue";
import { BasicModal, useModalInner } from "/@/components/Modal";
import { Steps } from "ant-design-vue";
import BasicSetting from "/@/views/fuadmin/system/code-generator/template/design/basic-setting/index.vue";
import FormDesign from "/@/views/fuadmin/system/code-generator/template/design/form-design/index.vue";
import { BasicForm, useForm } from "/@/components/Form";
import { createOrUpdate } from "/@/views/demo/api";
import { IFormConfig } from "/@/views/sys/form-design/typings/v-form-component";
import { formConfigData } from "/@/views/fuadmin/system/code-generator/test/data";

export default defineComponent({
  name: "Modal",
  components: {
    BasicForm,
    FormDesign,
    BasicSetting,
    BasicModal, [Steps.name]: Steps,
    [Steps.Step.name]: Steps.Step
  },
  emits: ["success", "register"],
  setup(_, { emit }) {



    const isUpdate = ref(true);

    const [registerForm, { resetFields, setFieldsValue, validate }] = useForm();

    const state = reactive<{
      visible: boolean;
      formConfig: IFormConfig;
    }>({
      formConfig: {} as IFormConfig,
      visible: false,
    });

    const attrs = computed(() => {
      return {
        ...state.formConfig,
      } as Recordable;
    });


    const [registerModal, { setModalProps, closeModal }] = useModalInner(async (data) => {

      state.formConfig = formConfigData;

      await resetFields();
      setModalProps({ confirmLoading: false });
      isUpdate.value = !!data?.isUpdate;

      if (unref(isUpdate)) {
        await setFieldsValue({
          ...data.record,
        });
      }


    });

    const getTitle = computed(() => (!unref(isUpdate) ? "新增模板" : "编辑模板"));

    async function handleSubmit() {
      try {
        const values = await validate();
        setModalProps({ confirmLoading: true });
        await createOrUpdate(values, unref(isUpdate));
        closeModal();
        emit('success');
      } finally {
        setModalProps({ confirmLoading: false });
      }
    }

    return { registerModal, getTitle, handleSubmit, registerForm, attrs};
  }
});
</script>
