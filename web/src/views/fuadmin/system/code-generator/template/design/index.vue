<template>
  <BasicModal
    v-bind="$attrs"
    @register="registerModal"
    defaultFullscreen
    :canFullscreen="false"
    :title="getTitle"
    :footer="null"
    :canShowFeature="false"
  >
    <template #insertHeaderRight>
      <div style="padding-top: 12px; padding-right: 80px">
        <Space>
          <a-button v-if="current > 0" style="margin-left: 8px" @click="prev">上一步</a-button>
          <a-button v-if="current < 3 - 1" type="primary" @click="next">下一步</a-button>
          <a-button v-if="current == 3 - 1" type="primary" :loading="false" @click="handleSubmit">
            提交
          </a-button>
        </Space>
      </div>
    </template>
    <template #insertHeaderMiddle>
      <div>
        <a-steps type="navigation" :current="current" size="small">
          <a-step title="基础设置" />
          <a-step title="表单设计" />
          <a-step title="列表设计" />
        </a-steps>
      </div>
    </template>

    <div v-show="current === 0">
      <BasicSetting
        @basicInfo="getBasicInfo"
        :basicInfo="templateInfo.basicInfo"
        ref="refBasicSetting"
      />
    </div>
    <div v-show="current === 1">
      <FormDesign @designFormConfig="getDesignFormConfig" :formInfo="templateInfo.formConfigInfo" />
    </div>

    <div v-show="current === 2">
      <TableDesign
        ref="tableDesignRef"
        :templateInfo="templateInfo"
        @tableInfo="getTableInfo"
        :tableData="templateInfo.tableInfo"
      />
    </div>
  </BasicModal>
</template>
<script lang="ts">
  import { defineComponent, ref, computed, unref, reactive } from 'vue';
  import { BasicModal, useModalInner } from '/@/components/Modal';
  import { Steps, Space } from 'ant-design-vue';
  import BasicSetting from '/@/views/fuadmin/system/code-generator/template/design/basic-setting/index.vue';
  import FormDesign from '/@/views/fuadmin/system/code-generator/template/design/form-design/index.vue';
  import TableDesign from '/@/views/fuadmin/system/code-generator/template/design/table-design/index.vue';
  import { createOrUpdate } from '/@/views/fuadmin/system/code-generator/template/api';

  export default defineComponent({
    name: 'DesignModal',
    components: {
      TableDesign,
      FormDesign,
      BasicSetting,
      BasicModal,
      [Steps.name]: Steps,
      [Steps.Step.name]: Steps.Step,
      Space,
    },
    emits: ['success', 'register'],
    setup(_, { emit }) {
      const isUpdate = ref(true);

      let templateInfo = reactive<{
        basicInfo: Object;
        formConfigInfo: Object;
        tableInfo: Object;
      }>({
        basicInfo: {},
        formConfigInfo: {},
        tableInfo: {},
      });

      const refBasicSetting = ref();
      const id = ref();

      const [registerModal, { setModalProps, closeModal }] = useModalInner(async (data) => {
        setModalProps({ confirmLoading: false });
        isUpdate.value = data.isUpdate;
        current.value = 0;
        templateInfo.formConfigInfo = {};
        templateInfo.basicInfo.template_name = undefined;
        templateInfo.basicInfo.template_code = undefined;
        templateInfo.basicInfo.remark = undefined;
        tableDesignRef.value.resetList();
        templateInfo.tableInfo = {};
        if (isUpdate.value) {
          templateInfo.formConfigInfo = JSON.parse(data.record.form_info);
          templateInfo.basicInfo.template_name = data.record.name;
          templateInfo.basicInfo.template_code = data.record.code;
          templateInfo.basicInfo.remark = data.record.remark;
          templateInfo.tableInfo = JSON.parse(data.record.table_info);
          id.value = data.record.id;
        }
      });

      const current = ref<number>(0);
      const next = async () => {
        const validated = await refBasicSetting.value.validateForm();
        console.log(222, validated)
        if (validated) {
          current.value++;
        }
      };
      const prev = () => {
        current.value--;
      };

      const getTitle = computed(() => (!unref(isUpdate) ? '新增模板' : '编辑模板'));

      const getBasicInfo = (val) => {
        templateInfo.basicInfo = val;
      };

      const getDesignFormConfig = (val) => {
        templateInfo.formConfigInfo = val;
      };

      const getTableInfo = (val) => {
        templateInfo.tableInfo = val;
      };

      const tableDesignRef = ref();

      async function handleSubmit() {
        try {
          setModalProps({ confirmLoading: true });
          tableDesignRef.value.tableInfo();
          const payload = {
            name: templateInfo.basicInfo.template_name,
            code: templateInfo.basicInfo.template_code,
            remark: templateInfo.basicInfo.template_des,
            form_info: JSON.stringify(templateInfo.formConfigInfo),
            table_info: JSON.stringify(templateInfo.tableInfo),
            id: id.value,
          };

          await createOrUpdate(payload, unref(isUpdate));

          closeModal();

          emit('success');
        } finally {
          setModalProps({ confirmLoading: false });
        }
      }

      return {
        registerModal,
        getTitle,
        getDesignFormConfig,
        refBasicSetting,
        handleSubmit,
        current,
        next,
        prev,
        templateInfo,
        getTableInfo,
        getBasicInfo,
        tableDesignRef,
      };
    },
  });
</script>
