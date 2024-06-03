import { createRouter, createWebHashHistory } from 'vue-router'



const Home = () => import('../components/Home.vue');
const Login = () => import('../components/Login.vue');
const page1 = () => import('../components/WELCOME.vue');
const TicketInquiry = () => import('../components/TicketInquiry.vue')
const TicketOrder = () => import('../components/TicketOrder.vue')
const HistoryOrders = () => import('../components/orders/HistoryOrders.vue')
const NoPayOrderList = () => import('../components/orders/NoPayOrderList.vue')
const NoTripOrderList = () => import('../components/orders/NoTripOrderList.vue')
const SelfCenter = () => import('../components/self/SelfCenter.vue')
const Recharge = () => import('../components/pay/Recharge.vue')
const PayMethod = () => import('../components/pay/PayMethod.vue')
const mesdeal_home = () => import('../components/mesdeal/mesdeal_home.vue')
const mesdeal_check = () => import('../components/mesdeal/mesdeal_check.vue')
const mesdeal_message = () => import('../components/mesdeal/mesdeal_message.vue')
const mesdeal_setting = () => import('../components/mesdeal/mesdeal_setting.vue')
const trainAdjust_home = () => import('../components/trainAdjustment/trainAdjust_home.vue')
const trainAdjust_check = () => import('../components/trainAdjustment/trainAdjust_check.vue')
const trainAdjust_message = () => import('../components/trainAdjustment/trainAdjust_message.vue')
const trainAdjust_setting = () => import('../components/trainAdjustment/trainAdjust_setting.vue')
const TicketChange = () => import('../components/TicketChange.vue')

const routes= [
  {
    path: "/TicketOrder/:temp",
    name: "TicketOrder",
    component: TicketOrder,
    meta: {
      title: "车票订购"
    },
  },
    {
      path:'/Login',
      name: 'Login',
      component:Login,
    },
    {
      path:'/',
      name:'First',
      redirect: {name: "Login"},
    },
    {
      path : '/Home',
      name:'Home',
      component:Home,
      redirect: {name: "WELCOME"},
      children:[
        {
          path: "/TicketInquiry",
          name: "TicketInquiry",
          component: TicketInquiry,
          meta: {
            title: "车票查询"
          }
        },
        {
          path: "/WELCOME",
          name: "WELCOME",
          component:page1,
          meta:{
              title:"欢迎 "
          }
        },
        {
          path:'/mesdeal_home',
          name: 'mesdeal_home',
          component:mesdeal_home,
          meta:{
            title:""
        }
        },
        {
          path: '/mesdeal_message',
          name:'mesdeal_message',
          component:mesdeal_message,
          meta:{
            title:""
        }
        },
        {
          path: '/mesdeal_check',
          name:'mesdeal_check',
          component:mesdeal_check,
          meta:{
            title:""
        }
        },
        {
          path: '/mesdeal_setting',
          name:'mesdeal_setting',
          component:mesdeal_setting,
          meta:{
            title:""
        }
        },
        {
          path: '/historyOrders',
          name: 'historyOrders',
          component: HistoryOrders,
          meta: {
            title: "历史订单"
          },
        },
        {
          path: '/noPayOrderList',
          name: 'noPayOrderList',
          component: NoPayOrderList,
          meta: {
            title: "未支付订单"
          },
        },
        {
          path: '/noTripOrderList',
          name: 'noTripOrderList',
          component: NoTripOrderList,
          meta: {
            title: "未出行订单"
          },
        },
        {
          path: '/selfCenter',
          name: 'selfCenter',
          component:SelfCenter, 
          meta: {
            title: "个人中心"
          }
        },
        {
          path: '/recharge',
          name: 'recharge',
          component:Recharge, 
          meta: {
            title: "充值界面"
          }
        },
        {
          path: '/payMethod/:price',
          name: 'payMethod',
          component:PayMethod, 
          meta: {
            title: "选择充值方式"
          }
        },
        {
          path: "/TicketChange/:order",
          name: "TicketChange",
          component: TicketChange,
          meta: {
            title: "车票改签"
          }
        },
      ],
    },
    //信息管理
    {
      path:'/mesdeal1',
      name: 'mesdeal_home',
      component:mesdeal_home,
    },
    {
      path: '/mesdeal2',
      name:'mesdeal_message',
      component:mesdeal_message,
    },
    {
      path: '/mesdeal3',
      name:'mesdeal_check',
      component:mesdeal_check,
    },
    {
      path: '/mesdeal4',
      name:'mesdeal_setting',
      component:mesdeal_setting,
    },
    //车次调控
    {
      path:'/trainAdjust1',
      name: 'trainAdjust_home',
      component:trainAdjust_home,
    },
    {
      path: '/trainAdjust2',
      name:'trainAdjust_message',
      component:trainAdjust_message,
    },
    {
      path: '/trainAdjust3',
      name:'trainAdjust_check',
      component:trainAdjust_check,
    },
    {
      path: '/trainAdjust4',
      name:'trainAdjust_setting',
      component:trainAdjust_setting,
    },

]
const router = createRouter({
  history: createWebHashHistory(),
  routes
})
 
export default router
