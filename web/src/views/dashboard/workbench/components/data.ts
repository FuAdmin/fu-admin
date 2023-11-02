
export interface GroupItem {
  title: string;
  icon: string;
  desc: string;
  date: string;
  group: string;
  path: string;
  type: string;
  size: Size;
}

interface  Size {
  width: string | number;
  height: string | number;
}

interface NavItem {
  title: string;
  icon: string;
  color: string;
}

interface DynamicInfoItem {
  avatar: string;
  name: string;
  date: string;
  desc: string;
}

export const navItems: NavItem[] = [
  {
    title: '首页',
    icon: 'ion:home-outline',
    color: '#1fdaca',
  },
  {
    title: '仪表盘',
    icon: 'ion:grid-outline',
    color: '#bf0c2c',
  },
  {
    title: '组件',
    icon: 'ion:layers-outline',
    color: '#e18525',
  },
  {
    title: '系统管理',
    icon: 'ion:settings-outline',
    color: '#3fb27f',
  },
  {
    title: '权限管理',
    icon: 'ion:key-outline',
    color: '#4daf1bc9',
  },
  {
    title: '图表',
    icon: 'ion:bar-chart-outline',
    color: '#00d8ff',
  },
];

export const dynamicInfoItems: DynamicInfoItem[] = [
  {
    avatar: 'dynamic-avatar-1|svg',
    name: '威廉',
    date: '刚刚',
    desc: `在 <a>开源组</a> 创建了项目 <a>Vue</a>`,
  },
  {
    avatar: 'dynamic-avatar-2|svg',
    name: '艾文',
    date: '1个小时前',
    desc: `关注了 <a>威廉</a> `,
  },
  {
    avatar: 'dynamic-avatar-3|svg',
    name: '克里斯',
    date: '1天前',
    desc: `发布了 <a>个人动态</a> `,
  },
  {
    avatar: 'dynamic-avatar-4|svg',
    name: 'Fu',
    date: '2天前',
    desc: `发表文章 <a>如何编写一个Vite插件</a> `,
  },
  {
    avatar: 'dynamic-avatar-5|svg',
    name: '皮特',
    date: '3天前',
    desc: `回复了 <a>杰克</a> 的问题 <a>如何进行项目优化？</a>`,
  },
  {
    avatar: 'dynamic-avatar-6|svg',
    name: '杰克',
    date: '1周前',
    desc: `关闭了问题 <a>如何运行项目</a> `,
  },
  {
    avatar: 'dynamic-avatar-1|svg',
    name: '威廉',
    date: '1周前',
    desc: `发布了 <a>个人动态</a> `,
  },
  {
    avatar: 'dynamic-avatar-1|svg',
    name: '威廉',
    date: '2021-04-01 20:00',
    desc: `推送了代码到 <a>Github</a>`,
  },
];

export const groupItems: GroupItem[] = [
  {
    title: 'Apply Access',
    icon: 'unlock',
    desc: '不要等待机会，而要创造机会。',
    group: '开源组',
    date: '2021-04-01',
    path: '',
    type: 'model',
    size: {
      width: 50,
      height: 50,
    }
  },
  {
    title: 'My JCI',
    icon: 'jci',
    desc: 'jci home page.',
    group: '算法组',
    date: '2021-04-01',
    path: 'https://my.jci.com',
    type: 'url',
    size: {
      width: 90,
      height: 50,
    }
  },
  {
    title: 'Workday',
    icon: 'workday',
    desc: 'workday home page.',
    group: '上班摸鱼',
    date: '2021-04-01',
    path: 'https://wd5.myworkday.com/jci/d/pex/home.htmld',
    type: 'url',
    size: {
      width: 90,
      height: 50,
    }
  },
  {
    title: 'Concur',
    icon: 'concur',
    desc: 'concur home page.',
    group: 'UI',
    date: '2021-04-01',
    path: 'https://us2.concursolutions.com/home.asp',
    type: 'url',
    size: {
      width: 60,
      height: 60,
    }
  },
  {
    title: 'SharePoint',
    icon: 'sharepoint',
    desc: 'sharepoint home page.',
    group: '技术牛',
    date: '2021-04-01',
    path: 'https://apps.jci.com/_layouts/15/sharepoint.aspx',
    type: 'url',
    size: {
      width: 60,
      height: 60,
    }
  },
  {
    title: 'Servicenow',
    icon: 'servicenow',
    desc: 'service-now home page',
    group: '架构组',
    date: '2021-04-01',
    path: 'https://jci.service-now.com/jcisp?id=jci_index',
    type: 'url',
    size: {
      width: 90,
      height: 50,
    }
  },
];
