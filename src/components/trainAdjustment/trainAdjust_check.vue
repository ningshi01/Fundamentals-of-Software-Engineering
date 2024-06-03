<template>
    <div class="mycon">
    <div class="blur-background"></div>
    <fornav msg1=车次调控 msg2=主页 msg3=个人信息 msg4=列车信息 msg5=设置
        href1=#/trainAdjust1 href2=#/trainAdjust2 href3=#/trainAdjust3 href4=#/trainAdjust4 href5=#/ ></fornav>
    <div class="hcon">
        <img src="../../assets/cat.png" alt="" class="flg">
        <img src="../../assets/logo.png" alt="" class="lg">
        <br><h1>车次调控</h1><br>
    </div>
    <div style="text-align:center;vertical-align:middel;">
        <el-input class="input3" v-model="message" clearable placeholder="请输入相应信息进行查询" float="left" size="large">
            <template #prepend>
                <el-select v-model="select" placeholder="筛选方式" style="width: 115px">
                <el-option label="车次信息" value="1" />
                <el-option label="列车类型" value="2" />
                </el-select>
            </template>

            <template #append>
                <el-button-group>
                    <el-button :icon="Search" type="primary" float="left" @click="asSearch" width="10%">查询</el-button>
                    <el-button :icon="Search" type="primary" float="left" @click="asAdd" width="10%">添加</el-button>
                </el-button-group>
                <!-- 添加表单弹出 -->
                <el-dialog v-model="asAddFlag" title="录入车次信息">
                    <el-form :model="form"  label-width="50" label-position="left" size="large">
                        <el-form-item label="车次" :label-width="formLabelWidth">
                            <el-input v-model="form.train_name" autocomplete="off"/>
                        </el-form-item>
                        <el-form-item label="列车类型" :label-width="formLabelWidth">
                            <el-select v-model="form.train_type" placeholder="Please select a type" float="right">
                                <el-option label="普快" value="REG" />
                                <el-option label="高铁" value="HSR" />
                            </el-select>
                        </el-form-item>
                        <!-- 动态添加的站点表单项 -->
                        <el-form-item v-for="(stop, index) in form.stops" :key="index" :label="'站点 ' + (index + 1)">
                            <el-row>
                                <!-- <el-col :span="6">
                                  <el-form-item label="序号">
                                    <el-input v-model="stop.sequence" autocomplete="off" />
                                  </el-form-item>
                                </el-col> -->
                                <!-- 可能得需要实现站名自适应搜素补全 -->
                                <el-col :span="6">
                                  <el-form-item label="站名">
                                    <!-- <el-input v-model="stop.station_name" autocomplete="off" /> -->
                                    <el-autocomplete 
                                        v-model="stop.station_name" 
                                        :fetch-suggestions="query => searchElements(query, index)" 
                                        placeholder="请输入站名" 
                                        @select="selectedItem => handleSelect(selectedItem, index)">
                                        <template v-slot="{ item }">
                                            {{ item }}
                                        </template>
                                    </el-autocomplete>
                                  </el-form-item>
                                </el-col>
                                <el-col :span="6">
                                  <el-form-item label="到达点">
                                    <el-input v-model="stop.arrival_time" autocomplete="off" />
                                  </el-form-item>
                                </el-col>
                                <el-col :span="6">
                                  <el-form-item label="停留">
                                    <el-input v-model="stop.duration" autocomplete="off" />
                                  </el-form-item>
                                </el-col>
                              </el-row>
                        </el-form-item>
                        <!-- 动态添加的车厢表单项 -->
                        <el-form-item v-for="(carriage, index) in form.carriages" :key="'carriage' + index" :label="'车厢 ' + (index + 1)">
                            <el-row>
                                <!-- <el-col :span="12">
                                  <el-form-item label="车厢号">
                                    <el-input v-model="carriage.carriage_num" autocomplete="off" />
                                  </el-form-item>
                                </el-col> -->
                                <el-col :span="12" class="col-center">
                                  <el-form-item label="类型">
                                    <el-select v-model="carriage.carriage_type" placeholder="车厢类型" autocomplete="off" float="right">
                                        <el-option label="商务舱" value="BUS" />
                                        <el-option label="一等舱" value="FST" />
                                        <el-option label="二等舱" value="SND" />
                                        <el-option label="软卧" value="SOF" />
                                        <el-option label="硬卧" value="HAW" />
                                        <el-option label="硬座" value="HAZ" />
                                    </el-select>
                                  </el-form-item>
                                </el-col>
                                <el-col :span="12">
                                  <el-form-item label="座位数">
                                    <el-input v-model="carriage.total_num" autocomplete="off" />
                                  </el-form-item>
                                </el-col>
                                <el-col :span="12">
                                  <el-form-item label="价格">
                                    <el-input v-model="carriage.price" autocomplete="off" />
                                  </el-form-item>
                                </el-col>
                              </el-row>
                        </el-form-item>
                        <el-button-group>
                            <el-button @click="addStop" type="primary" width="10%" border>添加站点</el-button>
                            <el-button @click="removeStop" type="primary" width="10%" border>删除站点</el-button>
                            <el-button @click="addCarriage" type="primary" width="10%" border>添加车厢</el-button>
                            <el-button @click="removeCarriage" type="primary" width="10%" border>删除车厢</el-button>
                        </el-button-group>
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
    <div class="table1"
    z-index="-1">
        <el-form :model="searchForm"  ref="searchForm">
        </el-form>
        <el-table :data="tableData" border style="width: 100%" 
        height="530px"
        :row-style="{height:'75px'}"
        :cell-style="{padding:'20px', whiteSpace: 'nowrap'}"
        :header-cell-style="{'text-align':'center',background:'rgb(15, 73, 137,.2)',color:'#333333','font-size': '14px','font-family': 'PingFang SC','font-weight': '700','border-color': '#CFDBFB'}"
        :row-hover-color="'#fde2e2'"
        class="custom-table"
        highlight-current-row	
        empty-text="猫猫正在努力寻找数据"
        >
            <el-table-column prop="train_name" label="车次">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.train_name }}</span>
                </template>
            </el-table-column>
            <el-table-column property="train_type" label="列车类型">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.train_type }}</span>
                </template>
            </el-table-column>
            <el-table-column property="carriages" label="车厢数">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.carriages.length }}</span>
                </template>
            </el-table-column>
            <el-table-column property="stops" label="始发站">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.stops[0].station_name }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="stops" label="终点站">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.stops[scope.row.stops.length - 1].station_name }}</span>
                </template>
              </el-table-column>
            <el-table-column property="stops" label="开车时间">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.stops[0].arrival_time }}</span>
                </template>
            </el-table-column>
            <el-table-column property="stops" label="到达时间">
                <template #default="scope">
                  <span v-if="true">{{ scope.row.stops[scope.row.stops.length - 1].arrival_time }}</span>
                </template>
            </el-table-column>
            <el-table-column fixed="right" label="操作">
                <template #default="scope">
                    <el-button-group>
                        <el-button link type="primary" size="large" @click="asDelete(scope.row)">删除</el-button>
                    </el-button-group>
                </template>
            </el-table-column>
        </el-table>
        <!-- 页面跳转 -->
        <div class="Pagination" style="text-align: left;margin-top: 10px;">
            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-size="limit"
                layout="total, prev, pager, next, jumper"
                :total="count">
            </el-pagination>


            <el-button type="primary" size="large" @click="addTicket">添加车票</el-button>
            <!-- 添加表单弹出 -->
            <el-dialog v-model="TicketFlag" title="添加车票">
                <el-form :model="Tform"  label-width="50" label-position="left" size="large">
                    <el-form-item label="车次" :label-width="formLabelWidth">
                        <el-input v-model="Tform.train_name" autocomplete="off"/>
                    </el-form-item>
                    <el-form-item label="起始日期" :label-width="formLabelWidth">
                        <el-input v-model="Tform.start_date" autocomplete="off" placeholder="请输入日期格式为:XXXX-XX-XX" />
                    </el-form-item>
                    <el-form-item label="截止日期" :label-width="formLabelWidth">
                        <el-input v-model="Tform.end_date" autocomplete="off" placeholder="请输入日期格式为:XXXX-XX-XX" />
                    </el-form-item>
                </el-form>
                <template #footer>
                <span class="dialog-footer" z-index="1">
                    <el-button-group>
                        <el-button type="primary" @click="TicketCancel">取消</el-button>
                        <el-button type="primary" @click="TicketConfirm">确认</el-button>
                    </el-button-group>
                </span>
                </template>
            </el-dialog>


            <div class="input-mycon">
                <el-input class="input2" v-model="this.city" clearable placeholder="请输入城市名" float="right" size="large"></el-input>
                <el-input class="input2" v-model="this.state" clearable placeholder="请输入站名" float="left" size="large">
                  <template #append>
                    <el-button type="primary" size="large" @click="updateStopData()">添加站点</el-button>
                  </template>
                </el-input>
            </div>
              
        </div>
    </div>
    </div>
</template>


<script scoped>
import fornav from './fornav.vue'
import { ElMessage } from 'element-plus'
import { ref } from 'vue'
import axios from 'axios'
import { mapState } from 'vuex'
import router from '@/router'

const asAddFlag = ref(false);
const TicketFlag = ref(false);
const formLabelWidth = '140px';
export default {
    computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
    name: "My_trainAdjust_check",
    created() {
        this.getTrainData();
        this.getStopData();
    },
    data() {
        return {
            message:'',
            city:'',
            state:'',
            tableData:[],
            stopData:[],
            asAddFlag,
            TicketFlag,
            formLabelWidth,
            form:{
                train_name: '',
                train_type: '',
                stops: [
                {
                    sequence: '',
                    station_name: '',
                    arrival_time: '',
                    duration: ''
                },{
                sequence: '',
                station_name: '',
                arrival_time: '',
                duration: '',
                }],
                carriages: [
                {
                    carriage_num: '',
                    carriage_type: '',
                    total_num: '',
                    price: ''
                },{
                    carriage_num: '',
                    carriage_type: '',
                    total_num: '',
                    price: ''
                },{
                    carriage_num: '',
                    carriage_type: '',
                    total_num: '',
                    price: ''
                },],
            },
            Tform:{
                train_name:'',
                start_date: '',
                end_date: '',
            },
            searchForm:
                {
                    train_number: ''
                }
            ,
            currentRow: null,
            offset: 0,
            limit:20 ,
            count: 0,
            currentPage: 1,
            select:'',
        }
    },
    props: {},
    watch: {
        message(newValue) {
            console.log(newValue);
            this.getTrainData();
        }
    },
    methods:{
        getStopData(){
            axios.get('/api/train/get_station_list/',{
                     headers:{
                        "Authorization":this.token
                     }
                })
                .then((res)=>{
                    console.log(res);
                    this.stopData=res.data.stations;
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
        getTrainData(){
            axios.post('/api/train/get_train_list/',{},{
                     headers:{
                        "Authorization":this.token
                     }
                })
                .then((res)=>{
                    console.log(res);
                    this.tableData=res.data.data;
                    this.tableData.sort((a, b) => {
                        const train_name1 = a.train_name;
                        const train_name2 = b.train_name;
                        const compareResult = train_name1.localeCompare(train_name2);
                        if (compareResult !== 0) {
                            return compareResult;
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
        // 删除按钮点击事件处理程序
        asDelete(row) {
            console.log(row);
            // 删除车次
            axios.post('/api/train/remove_train/',{
                train_name:row.train_name,
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
            }).catch((e)=>{
                ElMessage.error(e);
                console.log(e);
            })
            setTimeout(() => {
                this.getTrainData();
            }, 1000);
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
                case '1': // 车次信息
                this.data = this.tableData.filter(item => item.train_name.toString().includes(this.message));
                break;
                case '2': // 列车类型
                this.data = this.tableData.filter(item => item.train_type.toString().includes(this.message));
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
            this.form.carriages.forEach((carriage, index) => {
                carriage.carriage_num = index + 1;
            });
            this.form.stops.forEach((stop, index) => {
                stop.sequence = index + 1;
            });
            this.asAddFlag=true;
        },
        formCancel(){
            this.asAddFlag=false;
            ElMessage('取消添加');
        },
        formConfirm(){
                axios.post('/api/train/add_train/',this.form,{
                     headers:{
                        "Authorization":this.token
                     }
                })
                .then((res)=>{
                    console.log(res);
                    ElMessage.success("添加车次成功！");
                })
                .catch((error)=>{
                    ElMessage.error("添加好像出了什么问题:"+error);
                });
                setTimeout(() => {
                    this.getTrainData();
                }, 1000);
                this.asAddFlag=false;
        },
        addTicket(){
            this.TicketFlag=true;
        },
        TicketCancel(){
            this.TicketFlag=false;
            ElMessage('取消添加车票');
        },
        TicketConfirm(){
            axios.post('/api/train/add_ticket/',this.Tform,{
                     headers:{
                        "Authorization":this.token
                     }
                })
            .then((res)=>{
                console.log(res);
                ElMessage({
                    message: '添加车票成功！',
                    type: 'success',
                });
            })
            .catch((error)=>{
                console.log(error);
                ElMessage.error("添加好像出了什么问题:"+error);
            });
            this.TicketFlag=false;
        },
        addStop(){
            this.form.stops.push({
                sequence: '',
                station_name: '',
                arrival_time: '',
                duration: '',
            });
            this.form.stops.forEach((stop, index) => {
                stop.sequence = index + 1;
            });
        },
        removeStop(){
            if(this.form.stops.length>2)
                this.form.stops.pop();
            else{
                ElMessage({
                    message:'至少需要添加起点站和终点站！',
                    type:'error',
                })
            }
        },
        addCarriage(){
            this.form.carriages.push({
                carriage_num:'',
                type:'',
                total_num:'',
                price:'',
            });
            this.form.carriages.forEach((carriage, index) => {
                carriage.carriage_num = index + 1;
            });
        },
        removeCarriage(){
            if(this.form.carriages.length>3)
                this.form.carriages.pop();
            else{
                ElMessage({
                    message:'至少需要添加三个车厢！',
                    type:'error',
                })
            }
        },
        searchElements(query, index) {
            const results = this.stopData.filter(element => element.includes(query));
            console.log(index);
            console.log(this.form.stops[0].station_name);
            return results;
        },
        handleSelect(item, index) {
            console.log("Selected Item:", item);
            console.log("Index:", index);
            this.form.stops[index].station_name = item;
        },
        updateStopData(){
            //添加车站
            if(this.city !== '' && this.state !== ''){
                console.log(this.city),
                console.log(this.state),
                axios.post('/api/train/add_station/', {
                    station_name:this.state,
                    city:this.city,
                },{
                     headers:{
                        "Authorization":this.token
                     }
                }).then((response) => {
                        console.log(response.data);
                        ElMessage.success("添加成功！");
                        this.city='';
                        this.state='';
                })
                .catch((error) => {
                    console.log(error);
                    ElMessage.error("好像有什么问题呢")
                });
                setTimeout(() => {
                    this.getStopData();
                }, 1000);
                }
            else{
                ElMessage.error("不要空着表单！");
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
.input-mycon {
    display: flex;
  }
.input2{
    width:16%;
    flex: 1;
    margin-right: 10px; /* 可调整输入框之间的间距 */
}
.table1{
    padding: 0 4rem 0 8.75rem;
    text-align: center;
}
.Pagination {
    display: flex;
    justify-content: space-between; /* 或其他适当的对齐方式 */
    align-items: center; /* 或其他适当的对齐方式 */
  }
  .col-center {
    display: flex;
    justify-content:left;
    align-items:center;
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
.el-table-columnas {
    position: relative;
    z-index: 1;
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