<template>
  <Layout :style="{ height: '83vh' }">
    <LayoutContent>
      <Card title="查询条件" :bordered="false">
        <BasicTable @register="registerSearchTable" />
      </Card>
      <Card title="列表字段" :bordered="false">
        <BasicTable @register="registerColumnTable" />
      </Card>
    </LayoutContent>
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
          <Tab-pane key="1" tab="查询条件">
            <Row style="height: 30px">
              <Col :span="20">
                <div> 查询条件 </div>
              </Col>
              <Col :span="4">
                <Checkbox
                  v-model:checked="queryCheckAll"
                  :indeterminate="queryIndeterminate"
                  @change="onQueryCheckAllChange"
                />
              </Col>
            </Row>
            <!--            <CheckboxGroup v-model:value="queryList" :options="queryOptions" />-->
            <CheckboxGroup style="width: 100%" v-model:value="queryList">
              <div v-for="item in queryOptions" :key="item.value" style="height: 30px">
                <Row>
                  <Col :span="20">
                    <div>
                      {{ item.label }}
                    </div>
                  </Col>
                  <Col :span="4">
                    <Checkbox :value="item.value" />
                  </Col>
                </Row>
              </div>
            </CheckboxGroup>
          </Tab-pane>
          <Tab-pane key="2" tab="列表字段" force-render>
            <Row style="height: 30px">
              <Col :span="20">
                <div> 列表字段 </div>
              </Col>
              <Col :span="4">
                <Checkbox
                  v-model:checked="columnCheckAll"
                  :indeterminate="columnIndeterminate"
                  @change="onColumnCheckAllChange"
                />
              </Col>
            </Row>
            <CheckboxGroup style="width: 100%" v-model:value="columnList">
              <div v-for="item in queryOptions" :key="item.value" style="height: 30px">
                <Row>
                  <Col :span="20">
                    <div>
                      {{ item.label }}
                    </div>
                  </Col>
                  <Col :span="4">
                    <Checkbox :value="item.value" />
                  </Col>
                </Row>
              </div>
            </CheckboxGroup>
          </Tab-pane>
          <Tab-pane key="3" tab="列表属性">Content of Tab Pane 3</Tab-pane>
        </Tabs>
      </div>
    </LayoutSider>
  </Layout>
</template>

<script lang="ts">
  import 'codemirror/mode/javascript/javascript';

  import { ref, defineComponent, computed, reactive, toRefs, watch } from 'vue';
  import {
    Col,
    Layout,
    LayoutContent,
    LayoutSider,
    Row,
    Tabs,
    TabPane,
    CheckboxGroup,
    Checkbox,
    Card,
  } from 'ant-design-vue';

  import { useDesign } from '/@/hooks/web/useDesign';
  import { isArray } from '/@/utils/is';
  import BasicTable from '/@/components/Table/src/BasicTable.vue';
  import { useTable } from '/@/components/Table';
  import {
    columnFieldsColumns,
    searchColumns,
  } from '/@/views/fuadmin/system/code-generator/template/design/table-design/data';

  export default defineComponent({
    name: 'TableDesign',
    components: {
      BasicTable,
      CheckboxGroup,
      Layout,
      LayoutContent,
      LayoutSider,
      Row,
      Col,
      Tabs,
      TabPane,
      Checkbox,
      Card,
    },
    props: {
      templateInfo: { type: Object },
      tableData: Object,
    },
    emits: ['tableInfo'],
    setup(props, { emit }) {
      const { prefixCls } = useDesign('form-design');
      const queryState = reactive({
        queryIndeterminate: false,
        queryCheckAll: false,
        queryList: [],
      });

      const columnState = reactive({
        columnIndeterminate: false,
        columnCheckAll: false,
        columnList: [],
      });

      let queryOptions = computed(() => {
        const schemas = props.templateInfo.formConfigInfo.schemas;
        if (isArray(schemas)) {
          return schemas.map((item) => {
            return {
              value: item.label + '-' + item.field,
              label: item.label,
            };
          });
        } else return [];
      });

      const onQueryCheckAllChange = (e: any) => {
        Object.assign(queryState, {
          queryList: e.target.checked ? queryOptions.value.map((item) => item.value) : [],
          queryIndeterminate: false,
        });
      };

      const onColumnCheckAllChange = (e: any) => {
        Object.assign(columnState, {
          columnList: e.target.checked ? queryOptions.value.map((item) => item.value) : [],
          columnIndeterminate: false,
        });
      };

      watch(
        () => queryState.queryList,
        (val) => {
          console.log(val.length, val, queryOptions.value);
          queryState.queryIndeterminate = !!val.length && val.length < queryOptions.value.length;
          queryState.queryCheckAll = val.length === queryOptions.value.length;

          let queryFieldDatas = [];
          val.forEach((item) => {
            const queryFieldData = {
              column_name: item.split('-')[0],
              field_name: item.split('-')[1],
              type: '',
              is_check: true,
            };
            queryFieldDatas.push(queryFieldData);
          });
          // console.log(queryFieldDatas, 5555, val)
          setSearchTableData(queryFieldDatas);
        },
      );

      watch(
        () => columnState.columnList,
        (val) => {
          console.log(val.length, val, queryOptions.value);
          columnState.columnIndeterminate = !!val.length && val.length < queryOptions.value.length;
          columnState.columnCheckAll = val.length === queryOptions.value.length;

          let columnFieldDatas = [];
          val.forEach((item, index) => {
            const columnFieldData = {
              column_name: item.split('-')[0],
              field_name: item.split('-')[1],
              sort: index + 1,
              freeze: 'none',
              align: 'left',
              width: 80,
            };
            columnFieldDatas.push(columnFieldData);
          });
          // console.log(queryFieldDatas, 5555, val)
          setColumnTableData(columnFieldDatas);
        },
      );

      function resetList() {
        queryState.queryCheckAll = false;
        queryState.queryIndeterminate = false;
        columnState.columnIndeterminate = false;
        columnState.columnCheckAll = false;
      }

      const [
        registerSearchTable,
        { setTableData: setSearchTableData, getDataSource: getSearchData },
      ] = useTable({
        columns: searchColumns,
        pagination: false,
        maxHeight: 300,
      });

      const [
        registerColumnTable,
        { setTableData: setColumnTableData, getDataSource: getColumnData },
      ] = useTable({
        columns: columnFieldsColumns,
        pagination: false,
        maxHeight: 300,
      });

      watch(
        () => props.tableData,
        (val) => {
          if (val != undefined) {
            const tableInfoObj = val;
            const searchInfo = tableInfoObj.searchInfo;
            const columnInfo = tableInfoObj.columnInfo;
            setSearchTableData(searchInfo);
            setColumnTableData(columnInfo);
            if (isArray(searchInfo) && isArray(columnInfo)) {
              queryState.queryList = searchInfo.map((item) => {
                return item.column_name + '-' + item.field_name;
              });
              columnState.columnList = columnInfo.map((item) => {
                return item.column_name + '-' + item.field_name;
              });
            }
          }
        },
        { deep: true },
      );

      function tableInfo() {
        const searchData = getSearchData();

        // const searchSchemaList = [];
        // searchData.forEach((item) => {
        //   const searchSchema = {
        //     field: item.field_name,
        //     label: item.column_name,
        //     component: 'Input',
        //     colProps: { span: 6 },
        //   };
        //   searchSchemaList.push(searchSchema);
        // });

        const columnData = getColumnData();
        // const columnSchemaList = [];
        // columnData.forEach((item) => {
        //   const columnSchema = {
        //     title: item.column_name,
        //     dataIndex: item.field_name,
        //     width: item.width,
        //   };
        //   columnSchemaList.push(columnSchema);
        // });

        emit('tableInfo', {
          searchInfo: searchData,
          columnInfo: columnData,
        });
      }

      return {
        activeKey: ref('1'),
        prefixCls,
        ...toRefs(queryState),
        onQueryCheckAllChange,
        onColumnCheckAllChange,
        queryOptions,
        tableInfo,
        registerSearchTable,
        registerColumnTable,
        ...toRefs(columnState),
        resetList,
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
