<template>
  <BasicModal
    v-bind="$attrs"
    @register="registerModal"
    defaultFullscreen
    :canFullscreen="false"
    :title="getTitle"
    :footer="false"
    :canShowFeature="false"
  >
    <template #insertHeaderRight>
      <div style="padding-top: 12px; padding-right: 80px">
        <Space>
          <a-button v-if="current > 0" style="margin-left: 8px" @click="prev">上一步</a-button>
          <a-button v-if="current < 3 - 1" type="primary" @click="next">下一步</a-button>
          <a-button
            v-if="current == 3 - 1"
            type="primary"
            :loading="handleSubmit"
            @click="handleSubmit"
          >
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
      <FormDesign @designFormConfig="getDesignFormConfig"/>
    </div>

    <div v-show="current === 2">
      <TableDesign :templateInfo="templateInfo"/>
    </div>
  </BasicModal>
</template>
<script lang="ts">
  import { defineComponent, ref, computed, unref, reactive } from 'vue';
  import { BasicModal, useModalInner } from '/@/components/Modal';
  import { Steps, Space } from 'ant-design-vue';
  import BasicSetting from '/@/views/fuadmin/system/code-generator/template/design/basic-setting/index.vue';
  import FormDesign from '/@/views/fuadmin/system/code-generator/template/design/form-design/index.vue';
  import TableDesign from "/@/views/fuadmin/system/code-generator/template/design/table-design/index.vue";
  import { IFormConfig } from '/@/views/sys/form-design/typings/v-form-component';
  import { IAnyObject } from "/@/views/sys/form-design/typings/base-type";

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

      const templateInfo = reactive<{
        basicInfo: Object;
        formConfigInfo: IFormConfig;
        tableInfo: Object;
      }>({
        basicInfo: {},
        formConfigInfo: {} as IFormConfig,
        tableInfo: {},
      });

      const refBasicSetting = ref();

      const [registerModal, { setModalProps, closeModal }] = useModalInner(async (data) => {
        setModalProps({ confirmLoading: false });
        isUpdate.value = !!data?.isUpdate;
      });

      const current = ref<number>(0);
      const next = async () => {
        current.value++;
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

      async function handleSubmit() {
        try {
          setModalProps({ confirmLoading: true });
          // TODO custom api
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
        getBasicInfo,
      };
    },
  });
</script>
