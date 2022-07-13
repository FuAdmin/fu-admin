import { resultSuccess, resultError, getRequestToken, requestParams } from '../_util';
import { MockMethod } from 'vite-plugin-mock';
import { createFakeUserList } from './user';

// single
const dashboardRoute = {
  path: '/dashboard',
  name: 'Dashboard',
  component: 'LAYOUT',
  redirect: '/dashboard/analysis',
  meta: {
    title: 'routes.dashboard.dashboard',
    hideChildrenInMenu: true,
    icon: 'bx:bx-home',
  },
  children: [
    {
      path: 'analysis',
      name: 'Analysis',
      component: '/dashboard/analysis/index',
      meta: {
        hideMenu: true,
        hideBreadcrumb: true,
        title: 'routes.dashboard.analysis',
        currentActiveMenu: '/dashboard',
        icon: 'bx:bx-home',
      },
    },
    {
      path: 'workbench',
      name: 'Workbench',
      component: '/dashboard/workbench/index',
      meta: {
        hideMenu: true,
        hideBreadcrumb: true,
        title: 'routes.dashboard.workbench',
        currentActiveMenu: '/dashboard',
        icon: 'bx:bx-home',
      },
    },
  ],
};

const backRoute = {
  path: 'back',
  name: 'PermissionBackDemo',
  meta: {
    title: 'routes.fuadmin.permission.back',
  },

  children: [
    {
      path: 'page',
      name: 'BackAuthPage',
      component: '/fuadmin/permission/back/index',
      meta: {
        title: 'routes.fuadmin.permission.backPage',
      },
    },
    {
      path: 'btn',
      name: 'BackAuthBtn',
      component: '/fuadmin/permission/back/Btn',
      meta: {
        title: 'routes.fuadmin.permission.backBtn',
      },
    },
  ],
};

const authRoute = {
  path: '/permission',
  name: 'Permission',
  component: 'LAYOUT',
  redirect: '/permission/front/page',
  meta: {
    icon: 'carbon:user-role',
    title: 'routes.fuadmin.permission.permission',
  },
  children: [backRoute],
};

const levelRoute = {
  path: '/level',
  name: 'Level',
  component: 'LAYOUT',
  redirect: '/level/menu1/menu1-1',
  meta: {
    icon: 'carbon:user-role',
    title: 'routes.fuadmin.level.level',
  },

  children: [
    {
      path: 'menu1',
      name: 'Menu1Demo',
      meta: {
        title: 'Menu1',
      },
      children: [
        {
          path: 'menu1-1',
          name: 'Menu11Demo',
          meta: {
            title: 'Menu1-1',
          },
          children: [
            {
              path: 'menu1-1-1',
              name: 'Menu111Demo',
              component: '/fuadmin/level/Menu111',
              meta: {
                title: 'Menu111',
              },
            },
          ],
        },
        {
          path: 'menu1-2',
          name: 'Menu12Demo',
          component: '/fuadmin/level/Menu12',
          meta: {
            title: 'Menu1-2',
          },
        },
      ],
    },
    {
      path: 'menu2',
      name: 'Menu2Demo',
      component: '/fuadmin/level/Menu2',
      meta: {
        title: 'Menu2',
      },
    },
  ],
};

const sysRoute = {
  path: '/system',
  name: 'System',
  component: 'LAYOUT',
  redirect: '/system/account',
  meta: {
    icon: 'ion:settings-outline',
    title: 'routes.fuadmin.system.moduleName',
  },
  children: [
    {
      path: 'account',
      name: 'AccountManagement',
      meta: {
        title: 'routes.fuadmin.system.account',
        ignoreKeepAlive: true,
      },
      component: '/fuadmin/system/account/index',
    },
    {
      path: 'account_detail/:id',
      name: 'AccountDetail',
      meta: {
        hideMenu: true,
        title: 'routes.fuadmin.system.account_detail',
        ignoreKeepAlive: true,
        showMenu: false,
        currentActiveMenu: '/system/account',
      },
      component: '/fuadmin/system/account/AccountDetail',
    },
    {
      path: 'role',
      name: 'RoleManagement',
      meta: {
        title: 'routes.fuadmin.system.role',
        ignoreKeepAlive: true,
      },
      component: '/fuadmin/system/role/index',
    },

    {
      path: 'menu',
      name: 'MenuManagement',
      meta: {
        title: 'routes.fuadmin.system.menu',
        ignoreKeepAlive: true,
      },
      component: '/fuadmin/system/menu/index',
    },
    {
      path: 'dept',
      name: 'DeptManagement',
      meta: {
        title: 'routes.fuadmin.system.dept',
        ignoreKeepAlive: true,
      },
      component: '/fuadmin/system/dept/index',
    },
    {
      path: 'changePassword',
      name: 'ChangePassword',
      meta: {
        title: 'routes.fuadmin.system.password',
        ignoreKeepAlive: true,
      },
      component: '/fuadmin/system/password/index',
    },
  ],
};

const linkRoute = {
  path: '/link',
  name: 'Link',
  component: 'LAYOUT',
  meta: {
    icon: 'ion:tv-outline',
    title: 'routes.fuadmin.iframe.frame',
  },
  children: [
    {
      path: 'doc',
      name: 'Doc',
      meta: {
        title: 'routes.fuadmin.iframe.doc',
        frameSrc: 'https://vvbin.cn/doc-next/',
      },
    },
    {
      path: 'https://vvbin.cn/doc-next/',
      name: 'DocExternal',
      component: 'LAYOUT',
      meta: {
        title: 'routes.fuadmin.iframe.docExternal',
      },
    },
  ],
};

export default [
  {
    url: '/basic-api/getMenuList',
    timeout: 1000,
    method: 'get',
    response: (request: requestParams) => {
      const token = getRequestToken(request);
      if (!token) {
        return resultError('Invalid token!');
      }
      const checkUser = createFakeUserList().find((item) => item.token === token);
      if (!checkUser) {
        return resultError('Invalid user token!');
      }
      const id = checkUser.userId;
      let menu: Object[];
      switch (id) {
        case '1':
          dashboardRoute.redirect = dashboardRoute.path + '/' + dashboardRoute.children[0].path;
          menu = [dashboardRoute, authRoute, levelRoute, sysRoute, linkRoute];
          break;
        case '2':
          dashboardRoute.redirect = dashboardRoute.path + '/' + dashboardRoute.children[1].path;
          menu = [dashboardRoute, authRoute, levelRoute, linkRoute];
          break;
        default:
          menu = [];
      }

      return resultSuccess(menu);
    },
  },
] as MockMethod[];
