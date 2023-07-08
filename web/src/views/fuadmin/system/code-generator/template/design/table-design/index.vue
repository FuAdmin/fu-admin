<template>
  <Layout :style="{ height: '83vh' }">
    <LayoutContent> </LayoutContent>
    <LayoutSider
      :class="`right ${prefixCls}-sider`"
      :reverseArrow="true"
      collapsedWidth="0"
      width="270"
      style="background: #fff"
      :zeroWidthTriggerStyle="{ 'margin-top': '-70px', 'background-color': 'gray' }"
      breakpoint="lg"
    >
      <div style="padding: 0 10px">
        <Tabs v-model:activeKey="activeKey">
          <Tab-pane key="1" tab="查询字段">
            <Row style="height: 30px">
              <Col :span="20">
                <div>
                  查询字段
                </div>
              </Col>
              <Col :span="4">
                <Checkbox
                  v-model:checked="queryCheckAll"
                  :indeterminate="indeterminate"
                  @change="onCheckAllChange"
                >
                </Checkbox>
              </Col>
            </Row>
            <!--            <CheckboxGroup v-model:value="queryList" :options="queryOptions" />-->
            <CheckboxGroup style="width: 100%" v-model:value="queryList">
              <div v-for="item in queryOptions" style="height: 30px">
                <Row>
                  <Col :span="20">
                    <div>
                      {{ item.label }}
                    </div>
                  </Col>
                  <Col :span="4">
                    <Checkbox :value="item.value"></Checkbox>
                  </Col>
                </Row>
              </div>

            </CheckboxGroup>
          </Tab-pane>
          <Tab-pane key="2" tab="列表字段" force-render>Content of Tab Pane 2</Tab-pane>
          <Tab-pane key="3" tab="列表属性">Content of Tab Pane 3</Tab-pane>
        </Tabs>
      </div>
    </LayoutSider>
  </Layout>
</template>

<script lang="ts">
  import 'codemirror/mode/javascript/javascript';

  import { ref, provide, Ref, defineComponent, computed, reactive, toRefs, watch } from 'vue';
  import {
    Col,
    Layout,
    LayoutContent,
    LayoutSider,
    Row,
    Tabs,
    TabPane,
    CheckboxGroup,
    Input,
    FormItem,
    Form,
    Checkbox,
  } from 'ant-design-vue';

  import { useDesign } from '/@/hooks/web/useDesign';
  import { isArray } from '/@/utils/is';

  export default defineComponent({
    name: 'tableDesign',
    components: {
      Form,
      FormItem,
      Input,
      CheckboxGroup,
      Layout,
      LayoutContent,
      LayoutSider,
      Row,
      Col,
      Tabs,
      TabPane,
      Checkbox,
    },
    props: {
      templateInfo: { type: Object },
    },
    setup(props, { emit }) {
      const { prefixCls } = useDesign('form-design');
      const queryState = reactive({
        indeterminate: false,
        queryCheckAll: false,
        queryList: [],
      });

      let queryOptions = computed(() => {
        const schemas = props.templateInfo.formConfigInfo.schemas;
        if (isArray(schemas)) {
          console.log(schemas, 1111);
          return schemas.map((item) => {
            return {
              value: item.field,
              label: item.label,
            };
          });
        } else return [];
      });

      const onCheckAllChange = (e: any) => {
        Object.assign(queryState, {
          queryList: e.target.checked ? queryOptions.value.map((item) => item.value) : [],
          indeterminate: false,
        });
      };
      watch(
        () => queryState.queryList,
        (val) => {
          console.log(val.length, queryOptions.value);
          queryState.indeterminate = !!val.length && val.length < queryOptions.value.length;
          queryState.queryCheckAll = val.length === queryOptions.value.length;
        },
      );

      return {
        activeKey: ref('1'),
        prefixCls,
        ...toRefs(queryState),
        onCheckAllChange,
        queryOptions,
        props,
      };
    },
  });

  // endregion
</script>

<style lang="less" scoped>
  @prefix-cls: ~'@{namespace}-form-design';

  [datTheme='dark'] {
    .@{prefix-cls}-sider{
      background-color: #1f1f1f;
    }}

  [datTheme='light'] {
    .@{prefix-cls}-sider{
      background-color: #fff;
    }
  }
</style>
