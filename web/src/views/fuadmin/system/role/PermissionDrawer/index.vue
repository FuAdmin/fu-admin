<template>
  <BasicDrawer
    v-bind="$attrs"
    @register="registerDrawer"
    showFooter
    :title="getTitle"
    width="50%"
    :showOkBtn="false"
    :showCancelBtn="false"
  >
    <template #insertFooter>
      <a-button v-if="current > 0" style="margin-left: 8px" @click="prev">上一步</a-button>
      <a-button v-if="current < 4 - 1" type="primary" @click="next">下一步</a-button>
      <a-button v-if="current == 4 - 1" type="primary" :loading="submitLoad" @click="handleSubmit">
        提交
      </a-button>
    </template>

    <div class="step-form-form" style="padding: 0 35px">
      <a-steps :current="current" >
        <a-step title="菜单权限" />
        <a-step title="按钮权限" />
        <a-step title="列表权限" />
        <a-step title="数据权限" />
      </a-steps>
    </div>

    <div class="mt-5">
      <MenuPermission
        v-show="current === 0"
        @menuData="menuData"
        :checkedKeys="menuCheck"
        ref="RefMenu"
      />
      <ButtonPermission
        v-show="current === 1"
        @buttonData="buttonData"
        :checkedKeys="buttonCheck"
        ref="RefButton"
      />
      <ColumnPermission
        v-show="current === 2"
        @columData="columData"
        :checkedKeys="columnCheck"
        ref="RefColum"
      />
      <DataPermission
        v-show="current === 3"
        @dataPerData="dataPerData"
        :recordData="perData"
        :menuIds="[1, 2, 3]"
        ref="RefPerData"
      />
    </div>
  </BasicDrawer>
</template>
<script lang="ts">
  import { defineComponent, ref, reactive, toRefs, unref } from 'vue';

  import { BasicDrawer, useDrawerInner } from '/@/components/Drawer';

  import { useI18n } from '/@/hooks/web/useI18n';
  import { Steps } from 'ant-design-vue';
  import MenuPermission from './step/MenuPermission.vue';
  import ButtonPermission from './step/ButtonPermission.vue';
  import ColumnPermission from './step/ColumnPermission.vue';
  import DataPermission from './step/DataPermission.vue';
  import { createOrUpdate } from '../role.api';
  export default defineComponent({
    name: 'RolePermissionDrawer',
    components: {
      DataPermission,
      ColumnPermission,
      ButtonPermission,
      MenuPermission,
      BasicDrawer,
      [Steps.name]: Steps,
      [Steps.Step.name]: Steps.Step,
    },
    emits: ['success', 'register'],
    setup: function (_, {emit}) {
      const { t } = useI18n();
      const RefPerData = ref();
      const RefMenu = ref();
      const RefButton = ref();
      const RefColum = ref();
      const submitLoad = ref(false);

      const getTitle = '权限设置';
      const menuDataValue = ref([] as never[]);
      const menuChildDataValue = ref();
      let thisReloData = reactive({});
      const buttonDataValue = ref([] as never[]);
      const columnDataValue = ref([] as never[]);
      const dataPerDataValue = ref();

      let buttonCheck = ref();
      let columnCheck = ref();
      let menuCheck = ref();
      let perData = ref();
      const [registerDrawer, { closeDrawer, changeLoading }] = useDrawerInner(async (record) => {
        try {
          changeLoading(true);
          cleanData();
          submitLoad.value = true;
          current.value = 0;
          perData.value = record;

          await Promise.all([
            RefMenu.value.loadData(),
            RefButton.value.loadData(),
            RefColum.value.loadData(),
            RefPerData.value.loadData(),
          ]);

          thisReloData = record;
          menuCheck.value = record.menu;
          buttonCheck.value = record.permission.map((item) => {
            return 'b' + item;
          });
          columnCheck.value = record.column.map((item) => {
            return 'c' + item;
          });
        } finally {
          changeLoading(false);
          submitLoad.value = false;
        }
      });

      const current = ref<number>(0);
      const next = async () => {
        current.value++;
      };
      const prev = () => {
        current.value--;
      };

      const menuData = (val) => {
        menuDataValue.value = val.checkMenuData;
        menuChildDataValue.value = val.checkChildMenuData;
      };

      const buttonData = (val) => {
        buttonDataValue.value = val;
      };

      const dataPerData = (val) => {
        dataPerDataValue.value = val;
      };

      const columData = (val) => {
        columnDataValue.value = val;
      };

      function cleanData() {
        menuDataValue.value = [];
        buttonDataValue.value = [];
        columnDataValue.value = [];
        dataPerDataValue.value = {};
        buttonCheck.value = [];
        columnCheck.value = [];
        menuCheck.value = [];
        perData.value = [];
      }

      async function handleSubmit() {
        try {
          submitLoad.value = true;
          RefPerData.value.getPerData();

          let menu_ids: never[];
          let button_ids: never[];
          let column_ids: never[];

          if (menuDataValue.value.length !== 0) {
            menu_ids = menuDataValue.value;
          } else {
            menu_ids = menuCheck.value;
          }

          if (columnDataValue.value.length !== 0) {
            column_ids = []
              columnDataValue.value.forEach((item) => {
              if (!item.toString().search('c')) column_ids.push(Number(item.slice(1)));
            });
          } else {
            column_ids = columnCheck.value.map((item) => {
              if (!item.toString().search('c')) return Number(item.slice(1));
            });
          }

          if (buttonDataValue.value.length !== 0) {
            button_ids = []
              buttonDataValue.value.forEach((item) => {
              if (!item.toString().search('b')) button_ids.push(Number(item.slice(1)));
            });
          } else {
            button_ids = buttonCheck.value.map((item) => {
              if (!item.toString().search('b')) return Number(item.slice(1));
            });
          }

          const payload = {
            ...thisReloData,
            menu: menu_ids,
            permission: button_ids,
            column: column_ids,
            dept: dataPerDataValue.value.dept,
            data_range: dataPerDataValue.value.data_range,
          };
          debugger;
          await createOrUpdate(payload, unref(true));
          cleanData();
          closeDrawer();
          emit('success');
        } finally {
          submitLoad.value = false;
        }
      }

      return {
        submitLoad,
        registerDrawer,
        getTitle,
        handleSubmit,
        current,
        next,
        prev,
        menuData,
        buttonData,
        columData,
        dataPerData,
        menuDataValue,
        menuChildDataValue,
        RefPerData,
        buttonCheck,
        columnCheck,
        perData,
        menuCheck,
        RefMenu,
        RefButton,
        RefColum,
      };
    },
  });
</script>
