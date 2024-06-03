<template>
    <div>
        <meta  http-equiv="Cache-Control" content="no-cache,no-store,must-revlidate">
        <meta  http-equiv="Expires" content="O">
        <meta http-equiv="Pragma" content="no-cache">
        <el-button @click="check">测试按钮</el-button>
        <el-steps :active="active" align-center style="margin-top: 10px">
            <el-step title="添加乘客" ></el-step>
            <el-step title="选择座位" ></el-step>
            <el-step title="付款" ></el-step>
            <el-step title="订票成功" ></el-step>
        </el-steps>
        <el-table :data="passenger_data" v-show="show_passenger" style="width: 1000px;margin-left: 80px;margin-top: 20px">

            <el-table-column property="passenger_real_name" label="乘客姓名" ></el-table-column>
            <el-table-column property="passenger_phone_number" label="乘客电话号码" ></el-table-column>
            <el-table-column property="passenger_id_number" label="身份证号"></el-table-column>
            <el-table-column label="操作" width="100">
                <template v-slot:default="scope">
                    <el-button size="mini" type="danger" @click="deletepassenger(scope.row.passenger_phone_number)">删除</el-button>
                </template>
            </el-table-column>

        </el-table>

        <el-table :data="passenger_data" v-show="show_passenger_ticket" style="width: 1000px;margin-left: 80px;margin-top: 20px">

            <el-table-column property="passenger_real_name" label="乘客姓名" ></el-table-column>
            <el-table-column property="passenger_phone_number" label="乘客电话号码" ></el-table-column>
            <el-table-column property="passenger_id_number" label="身份证号"></el-table-column>
            <el-table-column property="carriage_no" label="车厢号"></el-table-column>
            <el-table-column property="seat_type" label="座位类型"></el-table-column>
            <el-table-column property="seat_no" label="座位号"></el-table-column>

        </el-table>

        <div v-show="active === 1 && dialogTableVisible" style="margin-top: 40px ;margin-left: 80px">
            <el-button @click="choose1">软卧</el-button>
            <el-button @click="choose2">硬卧</el-button>
            <el-button @click="choose3">硬座</el-button>
            <el-table :data="high_seat" align="left" v-show="choose_seat === 0" >

                <el-table-column property="carriage_number" label="剩余座位" width="100"></el-table-column>
                <el-table-column property="seat_type" label="座位类型" width="100"></el-table-column>
                <el-table-column property="upper_price" label="上铺" width="200"></el-table-column>
                <el-table-column property="lower_price" label="下铺" width="200"></el-table-column>
                <el-table-column label="操作" width="200">
                        <el-checkbox-group v-model="checkList" :max=passenger_count>
                            <el-checkbox label="上" />
                            <el-checkbox label="下" />
                          </el-checkbox-group>
                </el-table-column>

            </el-table>
            <el-table :data="medium_seat" align="left" v-show="choose_seat === 1">

                <el-table-column property="carriage_number" label="剩余座位" width="100"></el-table-column>
                <el-table-column property="seat_type" label="座位类型" width="100"></el-table-column>
                <el-table-column property="upper_price" label="上铺" width="130"></el-table-column>
                <el-table-column property="middle_price" label="中铺" width="130"></el-table-column>
                <el-table-column property="lower_price" label="下铺" width="130"></el-table-column>
                <el-table-column label="操作" width="300">
                    <el-checkbox-group v-model="checkList" :max=passenger_count>
                        <el-checkbox label="上" />
                        <el-checkbox label="中" />
                        <el-checkbox label="下" />
                      </el-checkbox-group>
                </el-table-column>
            </el-table>
            <el-table :data="low_seat" align="left" v-show="choose_seat === 2">

                <el-table-column property="carriage_number" label="剩余座位" width="70"></el-table-column>
                <el-table-column property="seat_type" label="座位类型" width="70"></el-table-column>
                <el-table-column property="A_price" label="A座" width="55"></el-table-column>
                <el-table-column property="B_price" label="B座" width="55"></el-table-column>
                <el-table-column property="C_price" label="C座" width="55"></el-table-column>
                <el-table-column property="D_price" label="D座" width="55"></el-table-column>
                <el-table-column property="E_price" label="E座" width="55"></el-table-column>
                <el-table-column property="F_price" label="F座" width="55"></el-table-column>
                <el-table-column label="操作" width="500">
                </el-table-column>
            </el-table>

        </div>
        <div v-show="active === 1 && dialogTableVisible_GD" style="margin-top: 40px ;margin-left: 80px;">
            <el-button @click="choose1">商务座</el-button>
            <el-button @click="choose2">一等座</el-button>
            <el-button @click="choose3">二等座</el-button>
            <el-table :data="high_seat_GD" align="left" v-show="choose_seat === 0">

                <el-table-column property="carriage_number" label="剩余座位" width="100"></el-table-column>
                <el-table-column property="seat_type" label="座位类型" width="100"></el-table-column>
                <el-table-column property="A_price" label="A座" width="150"></el-table-column>
                <el-table-column property="B_price" label="B座" width="150"></el-table-column>
                <el-table-column property="C_price" label="C座" width="150"></el-table-column>
                <el-table-column label="操作" width="200">
                    <el-checkbox-group v-model="checkList" :max=passenger_count>
                        <el-checkbox label="A" />
                        <el-checkbox label="B" />
                        <el-checkbox label="C" />
                      </el-checkbox-group>
                </el-table-column>
            </el-table>
            <el-table :data="medium_seat_GD" align="left" v-show="choose_seat === 1">

                <el-table-column property="carriage_number" label="剩余座位" width="100"></el-table-column>
                <el-table-column property="seat_type" label="座位类型" width="100"></el-table-column>
                <el-table-column property="A_price" label="A座" width="115"></el-table-column>
                <el-table-column property="B_price" label="B座" width="115"></el-table-column>
                <el-table-column property="C_price" label="C座" width="115"></el-table-column>
                <el-table-column property="D_price" label="D座" width="115"></el-table-column>
                <el-table-column label="操作" width="250">
                    <el-checkbox-group v-model="checkList" :max=passenger_count>
                        <el-checkbox label="A" />
                        <el-checkbox label="B" />
                        <el-checkbox label="C" />
                        <el-checkbox label="D" />
                      </el-checkbox-group>
                </el-table-column>
            </el-table>
            <el-table :data="low_seat_GD" align="left" v-show="choose_seat === 2">

                <el-table-column property="carriage_number" label="剩余座位" width="100"></el-table-column>
                <el-table-column property="seat_type" label="座位类型" width="100"></el-table-column>
                <el-table-column property="A_price" label="A座" width="90"></el-table-column>
                <el-table-column property="B_price" label="B座" width="90"></el-table-column>
                <el-table-column property="C_price" label="C座" width="90"></el-table-column>
                <el-table-column property="D_price" label="D座" width="90"></el-table-column>
                <el-table-column property="E_price" label="F座" width="90"></el-table-column>
                <el-table-column label="操作" width="300">
                    <el-checkbox-group v-model="checkList" :max=passenger_count>
                        <el-checkbox label="A" />
                        <el-checkbox label="B" />
                        <el-checkbox label="C" />
                        <el-checkbox label="D" />
                        <el-checkbox label="F" />
                      </el-checkbox-group>
                </el-table-column>
            </el-table>

        </div>

        <el-row  v-show="active === 0" >
            <div >
                <el-card class="box-card"  v-for="(tableData, index) in tableDatas" :key="index" style="width: 1000px;margin-left: 80px;margin-top: 20px">
                    <template #header>
                    <div class="clearfix">
                        <span>{{tableData.passenger_real_name}}</span>
                        <el-button style="float: right; padding: 3px 0"  @click="AddPassengerInfo(tableData.id,tableData.name,tableData.phone_number,tableData.id_number)" type="text">添加</el-button>
                    </div>
                </template>
                    <div  class="text item">
                        <span>姓名：</span><span>{{tableData.name}}</span>
                    </div>
                    <div  class="text item">
                        <span>电话号码：</span><span>{{tableData.phone_number}}</span>
                    </div>
                    <div v-if="(tableData.ticket_type== 'ADU')" class="text item">
                        <span>用户类型：</span><span>成人</span>
                    </div>
                    <div v-if="(tableData.ticket_type== 'CHI')" class="text item">
                        <span>用户类型：</span><span>儿童</span>
                    </div>
                    <div v-if="(tableData.ticket_type== 'DOM')" class="text item">
                        <span>用户类型：</span><span>残军</span>
                    </div>
                    <div  v-else class="text item">
                        <span>用户类型：</span><span>学生</span>
                    </div>
                    <div  class="text item">
                        <span>身份证号：</span><span>{{tableData.id_number}}</span>
                    </div>

                </el-card>
            </div>
        </el-row>
        <el-row  v-show="active === 2" >
            <el-table :data="order_data" v-show="show_order_list" style="width: 1000px;margin-left: 80px;margin-top: 20px">
                <el-table-column property="passenger_name" label="乘客姓名" ></el-table-column>
                <el-table-column property="ticket_type" label="车票类型" ></el-table-column>
                <el-table-column property="seat_location" label="座位位置"></el-table-column>
                <el-table-column property="price" label="车票价格"></el-table-column>
            </el-table>
            <el-table :data="order" v-show="show_order_list" style="width: 1000px;margin-left: 80px;margin-top: 20px">
                <el-table-column property="order_id" label="订单号" ></el-table-column>
                <el-table-column property="departure_time" label="出发时间" ></el-table-column>
                <el-table-column property="train_name" label="车次"></el-table-column>
                <el-table-column property="total_price" label="总价"></el-table-column>
            </el-table>
            
            <el-button type="primary" @click="pay_success()"  style="margin-left: 500px">确认支付</el-button>

        </el-row>
        <el-row   v-show="active === 3" >
            <div style="margin-top: 30px; margin-left: 50px;margin-right: 50px">
                <el-alert
                    title="恭喜您支付成功，请在未出行订单列表中查看"
                    type="success"
                    effect="dark">
                </el-alert>
            </div>
        </el-row>

        <el-button type="primary" round @click="next" style="margin-left: 500px;margin-top: 30px" v-show="active != 2">下一步</el-button>
    </div>
</template>


<script>
import axios from 'axios';
import router from "@/router"; // 导入Vue.js路由器
import { mapState } from "vuex";
import { ElMessage } from 'element-plus';

    export default {
        computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
        name: "TicketOrder",
        data() {
            return {
                order:[],
                checkList:[],
                temp:{},
                datetime:"",
                train_no:"",
                start_no:"",
                end_no:"",
                train_number:"",
                high_seat_price:"",
                medium_seat_price:"",
                low_seat_price:"",
                active:0,
                choose_seat:0,
                dialogTableVisible: false,
                dialogTableVisible_GD: false,
                show_passenger:false,
                show_passenger_ticket:false,
                show_order_list:false,
                passenger_count:0,
                high_seat:[],
                medium_seat:[],
                low_seat:[],
                high_seat_GD:[],
                medium_seat_GD:[],
                low_seat_GD:[],
                tableDatas:[],
                passenger_data:[],
                order_data:[],
                ticket_data: [],
                dialogFormVisible_wx:false,
                dialogFormVisible_zfb:false,
                passengerIds:[],
            };
        },

        methods: {
            choose1(){this.choose_seat=0},
            choose2(){this.choose_seat=1},
            choose3(){this.choose_seat=2},
            check(){
                console.log(this.checkList)
            },
            next() {
                this.active ++;
                if(this.active == 1)
                {
                    console.log("到达1")
                    this.getTicketCount();
                }
                if(this.active == 2)
                {
                    console.log("到达2")
                    this.handle();
                }
                if(this.active == 4)
                {
                    router.push({ path: "/historyOrders" });
                }
            },
            async getTicketCount(){
                axios.post('/api/train/query_ticket/',{
                    train_name:this.train_number,
                    date:this.datetime
                },{
                headers:{
                   "Authorization":this.token
                     }
                }).then((response) => {
                    console.log(response)
                    if(this.train_no=="HSR")
                    {
                        this.high_seat_GD = [];
                        this.medium_seat_GD = [];
                        this.low_seat_GD = [];


                                let high_temp = {};
                                high_temp.carriage_number = response.data.data.BUS.count;
                                high_temp.seat_type = "特等座";
                                high_temp.A_price = response.data.data.BUS.price;
                                high_temp.B_price = response.data.data.BUS.price;
                                high_temp.C_price = response.data.data.BUS.price;
                                this.high_seat_GD.push(high_temp);
                            

                                let high_temp1 = {};
                                high_temp1.carriage_number = response.data.data.FST.count;
                                high_temp1.seat_type = "一等座";
                                high_temp1.A_price = response.data.data.FST.price;
                                high_temp1.B_price = response.data.data.FST.price;
                                high_temp1.C_price = response.data.data.FST.price;
                                high_temp1.D_price = response.data.data.FST.price;
                                this.medium_seat_GD.push(high_temp1);
                                console.log(this.medium_seat_GD)
                                let high_temp2 = {};
                                high_temp2.carriage_number = response.data.data.SND.count;
                                high_temp2.seat_type = "二等座";
                                high_temp2.A_price = response.data.data.SND.price;
                                high_temp2.B_price = response.data.data.SND.price;
                                high_temp2.C_price = response.data.data.SND.price;
                                high_temp2.D_price = response.data.data.SND.price;
                                high_temp2.E_price = response.data.data.SND.price;
                                this.low_seat_GD.push(high_temp2);
                                console.log(this.low_seat_GD)
                        this.dialogTableVisible_GD = true
                 }
                 else{
                        this.high_seat = []
                        this.medium_seat = []
                        this.low_seat = []


                                let high_temp = {};
                                high_temp.carriage_number = response.data.data.SOF.count;
                                high_temp.seat_type = "软卧";
                                high_temp.upper_price = response.data.data.SOF.price;
                                high_temp.lower_price = response.data.data.SOF.price;
                                this.high_seat.push(high_temp);
                            

                                let high_temp1 = {};
                                high_temp1.carriage_number =  response.data.data.HAW.count;
                                high_temp1.seat_type = "硬卧";
                                high_temp1.upper_price = response.data.data.HAW.price;
                                high_temp1.middle_price = response.data.data.HAW.price;
                                high_temp1.lower_price = response.data.data.HAW.price;
                                this.medium_seat.push(high_temp1);
                            

                                let high_temp2 = {};
                                high_temp2.carriage_number = response.data.data.HAZ.count;
                                high_temp2.seat_type = "硬座";
                                high_temp2.A_price = response.data.data.HAZ.price;
                                high_temp2.B_price = response.data.data.HAZ.price;
                                high_temp2.C_price = response.data.data.HAZ.price;
                                high_temp2.D_price = response.data.data.HAZ.price;
                                high_temp2.E_price = response.data.data.HAZ.price;
                                high_temp2.F_price = response.data.data.HAZ.price;
                                this.low_seat.push(high_temp2);
                            
                        
                        this.dialogTableVisible = true
                 }
                 this.$message({
                        type: 'message',
                        message: '查询成功'
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
            async getPassenger()
            {
                console.log(this.token)
                axios.post('/api/user/get_user_info/',{user_id:4},{
             headers:{
                   "Authorization":this.token
                     }
                }).then((response) => {
                    console.log(response)
                    this.$message({
                        type: 'success',
                        message: '成功'
                    });
                    this.tableDatas = response.data.passengers;
                    console.log(this.tableDatas)
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
            AddPassengerInfo(passenger_id,passenger_real_name,passenger_phone_number,passenger_id_number)
            {
                if(this.passenger_data.some(p => p.passenger_id_number === passenger_id_number) ){
                    this.$message({
                    message: "重复添加"+passenger_real_name,
                    type: 'error'
                });
                }
                else{
                let passenger_d = {};
                passenger_d.passenger_real_name = passenger_real_name;
                passenger_d.passenger_phone_number = passenger_phone_number;
                passenger_d.passenger_id_number = passenger_id_number;
                this.passenger_data.push(passenger_d);
                this.passenger_count ++;
                this.passengerIds.push(passenger_id)
                this.$message({
                    message: '当前添加了'+this.passenger_count+"位乘客",
                    type: 'success'
                });
                this.show_passenger = true;
            }
            },
            handle()
            {
                console.log(this.passengerIds);
                console.log(this.checkList);
                if(this.train_no=='HSR')
                {
                    const seatType="BUS";
                    if(this.choose_seat==0)
                    this.seatType="BUS";
                    else if(this.choose_seat==1)
                    this.seatType="FST";
                    else
                    this.seatType="SND"
                    axios.post('/api/train/create_order/',{
                        user_id:4,
                        train_name:this.train_number,
                        carriage_type:seatType,
                        date:this.datetime,
                        start_stop_id:this.start_no,
                        end_stop_id:this.end_no,
                        passenger_ids:this.passengerIds,
                        seat_locations:this.checkList,
                    },{
             headers:{
                   "Authorization":this.token
                     }
                }).then((response) => {
                        console.log(response)
                        for(let i=0;i<response.data.data.passenger_order_data.length;i++)
                        {
                            let temp_passenger_data={};
                            temp_passenger_data.passenger_name=response.data.data.passenger_order_data[i].passenger_name;
                            temp_passenger_data.ticket_type=response.data.data.passenger_order_data[i].ticket_type;
                            temp_passenger_data.seat_location=response.data.data.passenger_order_data[i].seat_location;
                            temp_passenger_data.price=response.data.data.passenger_order_data[i].price;
                            this.order_data.push(temp_passenger_data)
                        }
                        console.log(this.order_data)
                        let order1={};
                        order1.order_id=response.data.data.order_id;
                        order1.arrival_station_name=response.data.data.arrival_station_name;
                        order1.arrival_time=response.data.data.arrival_time;
                        order1.create_time=response.data.data.create_time;
                        order1.date=response.data.data.date;
                        order1.departure_station_name=response.data.data.departure_station_name;
                        order1.departure_time=response.data.data.departure_time;
                        order1.total_price=response.data.data.total_price;
                        order1.train_name=response.data.data.train_name;
                        this.order.push(order1);
                        console.log(order1)
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
                    this.show_order_list=true;
                }
                else{
                    if(this.train_no=='REG')
                    {
                        const seatType="SOF";
                        if(this.choose_seat==0)
                        this.seatType="SOF";
                        else if(this.choose_seat==1)
                        this.seatType="HAW";
                        else
                        this.seatType="HAZ"
                        axios.post('/api/train/create_order/',{
                        user_id:4,
                        train_name:this.train_number,
                        carriage_type:seatType,
                        date:this.datetime,
                        start_stop_id:this.start_no,
                        end_stop_id:this.end_no,
                        passenger_ids:this.passengerIds,
                        seat_locations:this.checkList,
                    },{
             headers:{
                   "Authorization":this.token
                     }
                }).then((response) => {
                        console.log(response)
                        for(let i=0;i<response.data.data.passenger_order_data.length;i++)
                        {
                            let temp_passenger_data={};
                            temp_passenger_data.passenger_name=response.data.data.passenger_order_data[i].passenger_name;
                            temp_passenger_data.ticket_type=response.data.data.passenger_order_data[i].ticket_type;
                            temp_passenger_data.seat_location=response.data.data.passenger_order_data[i].seat_location;
                            temp_passenger_data.price=response.data.data.passenger_order_data[i].price;
                            this.order_data.push(temp_passenger_data)
                        }
                        console.log(this.order_data)
                        let order1={};
                        order1.order_id=response.data.data.order_id;
                        order1.arrival_station_name=response.data.data.arrival_station_name;
                        order1.arrival_time=response.data.data.arrival_time;
                        order1.create_time=response.data.data.create_time;
                        order1.date=response.data.data.date;
                        order1.departure_station_name=response.data.data.departure_station_name;
                        order1.departure_time=response.data.data.departure_time;
                        order1.total_price=response.data.data.total_price;
                        order1.train_name=response.data.data.train_name;
                        this.order.push(order1);
                        console.log(order1)
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
                    this.show_order_list=true;
                    }}
            },
            deletepassenger(passenger_phone_number)
            {
                for(let i = 0 ; i<this.passenger_data.length ; i++)
                {
                    if(this.passenger_data[i].passenger_phone_number == passenger_phone_number)
                    {
                        this.passenger_data.splice(i,1);
                    }
                }
                this.passenger_count --;
            },
          async  pay_success()
            {
                console.log(this.order[0].order_id)
                axios.post('/api/train/pay_order/',{
                    order_id:this.order[0].order_id,
                    user_id:4
                },{
             headers:{
                   "Authorization":this.token
                     }
                }).then((response) => {
                    console.log(response)
                    this.active=3

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
            }

        },
        created(){
            this.temp=JSON.parse(this.$route.params.temp)
            console.log(this.$route.params.temp)
            console.log(this.temp.start_no)
            if(this.temp.datetime == null || this.temp.train_no == null)

            {
                this.$message({
                    message: '请先选择一趟列车',
                    type: 'warning'
                });
            }else
            {
                this.datetime = this.temp.datetime;
                this.train_no= this.temp.train_no;
                this.start_no= this.temp.start_no;
                this.end_no= this.temp.end_no;
                this.train_number = this.temp.train_number;
                this.high_seat_price= this.temp.high_seat_price;
                this.medium_seat_price= this.temp.medium_seat_price;
                this.low_seat_price= this.temp.low_seat_price;
            }

        },

        mounted() {
            this.getPassenger();
        }


    }
</script>

<style lang="less" scoped>
    @import '../assets/mixin.less';
    .explain_text{
        margin-top: 20px;
        text-align: center;
        font-size: 20px;
        color: #333;
    }
    .admin_set{
        width: 60%;
        background-color: #F9FAFC;
        min-height: 400px;
        margin: 20px auto 0;
        border-radius: 10px;
        ul > li{
            padding: 20px;
            span{
                color: #666;
            }
        }
    }
    .admin_title{
        margin-top: 20px;
        font-size: 24px;
        color: #666;
        text-align: center;
    }
    .avatar-uploader .el-upload {
        border: 1px dashed #d9d9d9;
        margin-top: 10px;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    .avatar-uploader .el-upload:hover {
        border-color: #20a0ff;
    }
    .avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 120px;
        height: 120px;
        line-height: 120px;
        text-align: center;
    }
    .avatar {
        width: 120px;
        height: 120px;
        display: block;
    }
    .text {
        font-size: 14px;
    }

    .item {
        margin-bottom: 18px;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }
    .clearfix:after {
        clear: both
    }

    .box-card {
        width: 480px;
    }
</style>
