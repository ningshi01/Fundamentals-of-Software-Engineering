<template>
    <div class="container">
    <div class="blur-background"></div>
    <fornav msg1=信息管理 msg2=主页 msg3=个人信息 msg4=信息查询 msg5=设置
        href1=#/mesdeal1 href2=#/mesdeal2 href3=#/mesdeal3 href4=#/mesdeal4 href5=#/ ></fornav>

    <h1>检索用户</h1>
    <div style="text-align:center;vertical-align:middel;">

        <el-input class="input3" v-model="message" clearable placeholder="请输入相应信息进行查询" float="left" size="large">
            <template #prepend>
                <el-select v-model="select" placeholder="筛选方式" style="width: 205px">
                <el-option label="用户ID" value="1" />
                <el-option label="用户名" value="2" />
                <el-option label="用户类型" value="3" />
                </el-select>
            </template>

            <template #append>
                <el-button-group>
                    <el-button :icon="Search" type="primary" float="left" @click="asSearch" width="10%">查询</el-button>
                    <el-button :icon="Search" type="primary" float="left" @click="asAdd" width="10%">添加</el-button>
                </el-button-group>
                <!-- 添加表单弹出 -->
                <el-dialog v-model="asAddFlag" title="录入新用户" class="form1">
                    <el-form :model="form"  label-width="50" label-position="left" size="large">
                        <el-form-item label="用户类型" :label-width="formLabelWidth">
                            <el-select v-model="form.user_type" placeholder="请选定新用户类型" float="right">
                                <el-option label="普通用户" value="user" />
                                <el-option label="系统管理员" value="system_admin" />
                                <el-option label="铁路系统员" value="railway_admin" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="用户名" :label-width="formLabelWidth">
                            <el-input v-model="form.username" autocomplete="off"/>
                        </el-form-item>
                        <el-form-item label="密码" :label-width="formLabelWidth">
                            <el-input v-model="form.password" autocomplete="off"/>
                        </el-form-item>
                        <el-form-item label="邮箱" :label-width="formLabelWidth">
                            <el-input v-model="form.email" autocomplete="off"/>
                        </el-form-item>
                    </el-form>
                    <template #footer>
                        <span class="dialog-footer">
                            <el-button-group>
                                <el-button type="primary" @click="formCancel">取消</el-button>
                                <el-button type="primary" @click="formConfirm">确认</el-button>
                            </el-button-group>
                        </span>
                    </template>
                </el-dialog>
            </template>
            
        </el-input>
    </div>
    <div class="table1" z-index="-1">
        <!-- 查询结果表单 -->
        <el-table :data="tableData" border style="width: 100%" 
        height="550px"
        :row-style="{height:'75px'}"
        :cell-style="{padding:'20px', whiteSpace: 'nowrap'}"
        :header-cell-style="{'text-align':'center',background:'rgb(15, 73, 137,.2)',color:'#333333','font-size': '14px','font-family': 'PingFang SC','font-weight': '700','border-color': '#CFDBFB'}"
        :row-hover-color="'#fde2e2'"
        :class="custom-table"
        highlight-current-row	
        empty-text="猫猫正在努力寻找数据"
        >

            <el-table-column prop="id" label="用户ID">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.id }}</span>
                  <el-input v-else v-model="scope.row.id" size="large"></el-input>
                </template>
            </el-table-column>
            <el-table-column prop="usertype" label="用户类型">
                <template #default="scope">
                    <span v-if="true">{{ scope.row.usertype }}</span>
                    <el-input v-else v-model="scope.row.usertype" size="large"></el-input>
                </template>
            </el-table-column>
            <el-table-column prop="username" label="用户名">
                <template #default="scope">
                  <span v-if="!scope.row.editable">{{ scope.row.username }}</span>
                  <el-input v-else v-model="scope.row.username" size="large"></el-input>
                </template>
            </el-table-column>
            <el-table-column prop="password" label="密码">
                <template #default="scope">
                  <span v-if="!scope.row.editable">{{ maskedPassword() }}</span>
                  <el-input v-else v-model="tmp_password" size="large"></el-input>
                </template>
            </el-table-column>
            <!-- <el-table-column prop="abstractuser_ptr_id" label="Abstractuser_ptr_id">
                <template #default="scope">
                  <span v-if="!scope.row.editable">{{ scope.row.abstractuser_ptr_id }}</span>
                  <el-input v-else v-model="scope.row.abstractuser_ptr_id" size="large"></el-input>
                </template>
            </el-table-column> -->
            <el-table-column prop="email" label="用户邮箱">
                <template #default="scope">
                  <span v-if="!scope.row.editable">{{ scope.row.email }}</span>
                  <el-input v-else v-model="scope.row.email" size="large"></el-input>
                </template>
            </el-table-column>
            <el-table-column prop="balance" label="用户余额">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.balance }}</span>
                </template>
            </el-table-column>
            <el-table-column fixed="right" label="操作" class="custom-action-column">
                <template #default="scope">
                    <el-button-group >
                        <el-button v-if="!scope.row.editable" link type="primary" size="small" @click="asEdit(scope.row)">编辑</el-button>
                        <el-button v-else link type="success" size="small" @click="asSave(scope.row)">保存</el-button>
                        <el-button link type="info" size="small" @click="asDelete(scope.row)">删除</el-button>
                        <el-button link type="success" size="small" @click="openT(scope.row)">编辑乘车人</el-button>
                    </el-button-group>
                </template>
            </el-table-column>
        </el-table>
            
            <el-drawer
                v-model="this.table"
                title="乘车人信息"
                direction="rtl"
                size="1000px"
            >
                <el-table :data="passengerData">
                    <el-table-column property="id" label="乘车人ID"></el-table-column>
                    <el-table-column property="name" label="乘车人姓名"></el-table-column>
                    <el-table-column property="id_type" label="证件类型" ></el-table-column>
                    <el-table-column property="phone_region" label="号码归属地" ></el-table-column>
                    <el-table-column property="phone_number" label="电话号码" ></el-table-column>
                    <el-table-column fixed="right">
                        <template #default="scope">
                            <el-button type="danger" size="small" @click="deletePassenger(scope.row)">删除乘车人</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <el-row style="margin-top: 10px;background-color: #b1b3b8;" >
                    <el-col :span="24" style="text-align: center;" @click="addPassenger">
                        <el-icon>
                            <Plus />
                        </el-icon>
                    </el-col>
                </el-row>
                <el-drawer
                    v-model="innerDrawer"
                    title="添加乘车人"
                    :append-to-body="true"
                    :before-close="handleClose"
                    size="50%"
                >
                <el-form :model="Pform"  label-width="50" label-position="top" size="large">
                    <el-form-item label="证件类型">
                        <el-select v-model="Pform.id_type" placeholder="请选定证件类型" float="right">
                            <el-option label="中国居民身份证" value="CIC" />
                            <el-option label="港澳居民来往内地通行证" value="HTP" />
                            <el-option label="台湾居民来往大陆通行证" value="TTP" />
                            <el-option label="护照" value="PSP" />
                            <el-option label="外国人永久居留身份证" value="FRI" />
                            <el-option label="港澳台居民居住证" value="HMT" />
                        </el-select>
                    </el-form-item>
                    <el-form-item label="乘车人姓名">
                    <el-input v-model="Pform.name" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="证件号码">
                    <el-input v-model="Pform.id_number" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="票种类型">
                        <el-select v-model="Pform.ticket_type" placeholder="请选定票种" float="right">
                            <el-option label="成人" value="ADU" />
                            <el-option label="儿童" value="CHI" />
                            <el-option label="学生" value="STU" />
                            <el-option label="残疾军人" value="DOM" />
                        </el-select>
                    </el-form-item>
                    <el-form-item label="号码归属地">
                        <el-select v-model="Pform.phone_region" placeholder="请选择号码归属地" float="right">
                            <el-option label="+86" value="86" />
                            <el-option label="+852" value="852" />
                            <el-option label="+853" value="853" />
                            <el-option label="+886" value="886" />
                        </el-select>
                    </el-form-item>
                    <el-form-item label="电话号码">
                    <el-input v-model="Pform.phone_number" autocomplete="off"></el-input>
                    </el-form-item>
                </el-form>
                <!-- 确认添加 -->
                <el-row style="margin-top: 10px;background-color: #b3e19d;" >
                    <el-col :span="24" style="text-align: center;" @click="PformCommit">
                        <el-icon><CircleCheck /></el-icon>
                    </el-col>
                </el-row>
                <!-- 取消添加 -->
                <el-row style="margin-top: 10px;background-color: #dedfe0;" >
                    <el-col :span="24" style="text-align: center;" @click="PformCancel">
                        <el-icon><CircleClose /></el-icon>
                    </el-col>
                </el-row>
                </el-drawer>
            </el-drawer>

    </div>
    </div>
</template>


<script scoped>
import fornav from './fornav.vue';
import { ElMessage } from 'element-plus'
import { reactive,ref } from 'vue'
import axios from 'axios';
import { mapState } from "vuex";
import router from "@/router"; // 导入Vue.js路由器

const asAddFlag = ref(false);
const formLabelWidth = '140px';
const form = reactive({
    user_type: '',
    username: '',
    password: '',
    email: '',
});
const Pform = reactive({
    user_id:'',
    id_type:'',
    name:'',
    id_number:'',
    ticket_type:'',
    phone_region:'',
    phone_number:'',
})
export default {
    computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
    name: "My_mesdeal_check",
    created() {
        this.getTableData();
    },
    data() {
        return {
            tmp_password:"************",
            currut_id:'',
            passengerData:[],
            table:false,
            innerDrawer:false,
            data:'',
            message:'',
            userlist:[],
            system_adminlist:[],
            railway_adminlist:[],
            tableData:[],
            newTableData:[],
            asAddFlag,
            forPDFlag:false,
            formLabelWidth,
            form,
            Pform,
            select:'',
        }
    },
    props: {},
    watch: {
        message(newValue) {
            console.log(newValue);
            this.getTableData();
        }
    },
    methods:{
        getTableData(){
            //获取用户列表
            axios.get('/api/user/get_user_list/',{
                     headers:{
                         "Authorization":this.token
                     }
                }).then((response) => {
                this.userlist=response.data.users;
                this.userlist = this.userlist.map(item => {
                    return { ...item, usertype: 'user' };
                });
                this.system_adminlist=response.data.system_admins;
                this.system_adminlist = this.system_adminlist.map(item => {
                    return { 
                        ...item, 
                        usertype: 'system_admin',
                        email: '隐藏',
                        balance:'inf',
                    };
                });
                this.railway_adminlist=response.data.railway_admins;
                this.railway_adminlist = this.railway_adminlist.map(item => {
                    return { 
                        ...item, 
                        usertype: 'railway_admin',
                        email: '隐藏',
                        balance:'inf',
                    };
                });
                this.tableData=[...this.userlist,...this.system_adminlist,...this.railway_adminlist];
                this.tableData = this.tableData.map(item => {
                    return { ...item, list: [] };
                });
                this.tableData.sort((a, b) => {
                const userType1 = a.usertype;
                const userType2 = b.usertype;
                // 按照 user_type 进行比较
                const compareResult = userType1.localeCompare(userType2);
                if (compareResult !== 0) {
                    return -compareResult;
                }
                // 如果 user_type 相等，则按照 id 进行比较
                const id1 = a.id;
                const id2 = b.id;
                if (id1 < id2) {
                    return -1; // 返回负数表示 a 排在 b 前面
                } else if (id1 > id2) {
                    return 1; // 返回正数表示 a 排在 b 后面
                }
                return 0; // 返回 0 表示 a 和 b 相等
                });
            }).catch((error) => {
                console.log(error);
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
        },
        PformCommit(){
            this.Pform.user_id=this.currut_id;
            console.log(this.Pform);
            axios.post('/api/user/add_passenger/',this.Pform,{
                     headers:{
                         "Authorization":this.token
                     }
                })
            .then((res)=>{
                console.log(res);
                ElMessage.success("添加乘车人成功");
            }).catch((error)=>{
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
            this.innerDrawer=false;
            this.getPassengerData(this.currut_id);
        },
        PformCancel(){
            this.innerDrawer=false;
        },
        addPassenger(){
            this.innerDrawer=true;
        },
        
        deletePassenger(row){
            axios.post('/api/user/remove_passenger/',{
                user_id:this.currut_id,
                passenger_id:row.id,
            },{
                     headers:{
                         Authorization:this.token
                     }
                }).then((res)=>{
                console.log(res);
                ElMessage.success("删除成功！");
            }).catch((error) => {
                console.log(error);
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
        },
        openT(row){
            this.asForPassenger(row);
            this.table=true;
            this.currut_id=row.id;
        },
        asForPassenger(row){
            this.getPassengerData(row.id);
        },
        getPassengerData(id){
            axios.post('/api/user/get_passenger_list/',{
                user_id:id,
            },{
                     headers:{
                         "Authorization":this.token
                     }
                }).then((res)=>{
                this.passengerData=res.data.passenger_list;
            }).catch((error) => {
                console.log(error);
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
        },
        maskedPassword() {
            // 返回 "******" 以代替实际密码
            return "************";
        },
        asEdit(row) {
            row.editable = true; // 将行的 editable 属性设置为 true，使其可编辑
        },
        // 保存按钮点击事件处理程序
        asSave(row) {
            row.editable = false; // 将行的 editable 属性设置为 false，使其不可编辑
            // 更改用户信息
            axios.post('/api/user/update_user_info_system_admin/',{
                    user_id:row.id,
                    user_type:row.usertype,
                    username:row.username,
                    email:row.email,
                },{
                     headers:{
                         "Authorization":this.token
                     }
                }).then((res)=>{
                ElMessage.success("成功修改！");
                console.log(res);
                this.getTableData();
            }).catch((error) => {
                console.log(error);
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
        },
        // 删除按钮点击事件处理程序
        asDelete(row) {
            console.log(row);
            // 删除用户
            axios.post('/api/user/remove_user/',{
                user_id:row.id,
                user_type:row.usertype,
            },{
                     headers:{
                         "Authorization":this.token
                     }
                }).then((res)=>{
                console.log(res);
                ElMessage({
                    message: '删除成功',
                    type: 'success',
                })
                this.getTableData();
            }).catch((error) => {
                console.log(error);
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
        },
        async asSearch(){
            this.forSearch();
        },
        forSearch(){
            if(this.message === ''){
                ElMessage.warning("请输入查询信息！");
                return;
            }
            switch (this.select) {
                case '1': // 用户ID
                this.data = this.tableData.filter(item => item.id.toString().includes(this.message));
                break;
                case '2': // 用户名
                this.data = this.tableData.filter(item => item.username.includes(this.message));
                break;
                case '3': // 用户类型
                this.data = this.tableData.filter(item => item.usertype.includes(this.message));
                break;
                default:
                ElMessage.warning("请选择查询类型！");
                this.data = this.tableData;
                return;
            }
            this.tableData=this.data;
            ElMessage({
                message: '查询成功！',
                type: 'success',
            });
        },
        asAdd(){
            this.asAddFlag=true;
        },
        formCancel(){
            this.asAddFlag=false;
            ElMessage('取消添加');
        },
        formConfirm(){
            if (this.form.user_type !== '' &&
            this.form.username !== '' &&
            this.form.password !== '' &&
            this.form.email !== ''){
                    axios.post('/api/user/add_user/',this.form,{
                     headers:{
                         "Authorization":this.token
                     }
                })
                    .then((res)=>{
                        console.log(res.data.message);
                        Object.keys(form).forEach((key) => {form[key] = '';});
                    })
                    .catch((error) => {
                        console.log(error);
                        if(error.response.status==401 || this.isLogin==false)
                        {
                            router.push({ path: "/Login" });
                            ElMessage({
                            showClose: true,
                            message: '登录失效,请重新登录',
                            type: 'error',
                        })
                        }
                    });
                    this.getTableData();
                    this.asAddFlag=false;
                    location.reload();
                    ElMessage({
                        message: '添加成功！',
                        type: 'success',
                    });}
            else{
                ElMessage.error("未填写完表单！");
            }
        }
    },
    components: {
        fornav,
    }
}
</script>

<style scoped>

.input3{
    padding: 0 6rem 0 8.75rem;
    width: 102%;
}
.table1{
    padding: 0 4rem 0 8.75rem;
    z-index: -1;
}
</style>

<style>

.input1{
    padding: 0 2rem 0 6.75rem;
    width: 102%;
    opacity: 0.7; /* 设置透明度，调整参数以控制透明程度 */
}
.custom-table {
    border-radius: 10px; /* 设置圆角半径 */
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); /* 添加阴影效果 */
    overflow: hidden; /* 确保阴影不会溢出 */
    opacity: 0.7; /* 设置透明度，调整参数以控制透明程度 */
}
.custom-table .el-table__body td {
    background-color: rgb(244, 244, 244);
    border-color: rgb(153, 201, 201);
    border-width: 0.1ch;
    color: linear-gradient(to right, orange, purple);
}
.custom-action-column .custom-cell {
    background-color: rgb(154, 167, 233);
  }
</style>