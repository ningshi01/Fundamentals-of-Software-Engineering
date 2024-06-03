<template>
    <div class="fillcontain">
        <meta http-equiv="Cache-Control" content="no-cache,no-store,must-revlidate">
        <meta http-equiv="Expires" content="O">
        <meta http-equiv="Pragma" content="no-cache">

        <head-top></head-top>
        <div class="table_container">
            <el-table size="large" :data="tableData" style="width: 100%" stripe
                :default-sort="{ prop: 'create_time', order: 'descending' }">
                <el-table-column type="expand">
                    <template #default="props">
                        <el-table :data="props.row.passenger_order_data" :border="childBorder">
                            <el-table-column label="乘车人姓名" prop="passenger_name" />
                            <el-table-column label="车厢类型" prop="carriage_type" />
                            <el-table-column label="车厢号" prop="carriage_num" />
                            <el-table-column label="座位号" prop="seat_num" />
                            <el-table-column label="座位位置" prop="seat_location" />
                            <el-table-column label="证件类型" prop="passenger_id_type" />
                            <el-table-column label="优惠类型" prop="ticket_type" />
                            <el-table-column label="车票价格" prop="price" />
                            <el-table-column label="操作" width="200" v-show="is_rebooked">
                                <template #default="props2">
                                    <el-button size="mini" type="success"
                                        @click="handleTicketchanges2(props.row, props2.row, props2.$index)"
                                        v-show='!props2.row.is_rebooked'>改签</el-button>
                                    <el-button size="mini" type="primary"
                                        @click="handleTicketchanges2(props.row, props2.row, props2.$index)"
                                        v-show='props2.row.is_rebooked' disabled>已改签</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </template>
                </el-table-column>
                <el-table-column sortable label="下单时间" prop="create_time">
                </el-table-column>
                <el-table-column label="车次" prop="train_name">
                </el-table-column>
                <el-table-column label="始发站" prop="departure_station_name">
                </el-table-column>
                <el-table-column label="终点站" prop="arrival_station_name">
                </el-table-column>
                <el-table-column label="开车日期" prop="date">
                </el-table-column>
                <el-table-column label="开车时间" prop="departure_time">
                </el-table-column>
                <el-table-column label="到达时间" prop="arrival_time">
                </el-table-column>
                <el-table-column label="订单价格" prop="total_price">
                </el-table-column>
                <el-table-column label="订单状态" prop="order_status">
                </el-table-column>
                <el-table-column label="操作" width="200">
                    <template #default="props">
                        <el-button size="mini" type="success" @click="handleTicketchanges(props.row)">改签</el-button>
                        <el-button size="mini" type="success" @click="handleRefundTicket(props.row)">退票</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="Pagination">
                <el-pagination :hide-on-single-page="true" @size-change="handleSizeChange"
                    @current-change="handleCurrentChange" :current-page="currentPage" background :page-size="page_size"
                    layout="prev, pager, next" :page-count="count">
                </el-pagination>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ElMessageBox, ElMessage } from 'element-plus'
import { mapState } from "vuex";
import router from '@/router';
export default {
    computed: {
        ...mapState(["token"]),
        ...mapState(["isLogin"]),
    },
    data() {
        return {

            tableData: [
            ],
            currentRow: null,
            offset: 0,
            limit: 10,
            count: 0,
            currentPage: 1,
        }
    },
    methods: {
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
        },
        handleCurrentChange(val) {
            this.currentPage = val;
            this.offset = (val - 1) * this.limit;
            this.getLists();
        },
        handleRefundTicket(row) {
            for(let i=0;i<row.passenger_order_data.length;i++){
                if (row.passenger_order_data[i].is_rebooked) {
                    ElMessageBox.alert('订单内已有乘车人改签，无法全部退款', '退款失败', {
                        confirmButtonText: '确定',
                        showClose: false
                    });
                    return;
                }
            }
            let id = row.order_id;
            axios.post('/api/train/return_order/', {
                order_id: id,
            }, {
                headers: {
                    "Authorization": this.token
                }
            })
                .then((response) => {
                    //console.log(response.data.data);
                    ElMessageBox.alert('订单取消成功，钱款已退回余额', '取消成功', {
                        confirmButtonText: '确定',
                        showClose: false
                    })
                    this.getLists();
                })
                .catch(function (error) {
                    console.log(error);
                    if (error.response.status == 401 || this.isLogin == false) {
                        router.push({ path: "/Login" });
                        ElMessage({
                            showClose: true,
                            message: '登录失效,请重新登录',
                            type: 'error',
                        })
                    }
                });
        },
        handleTicketchanges(row) {
            console.log(row)
            let passengers = []
            for (let i = 0; i < row.passenger_order_data.length; i++) {
                if (row.passenger_order_data[i].is_rebooked) {
                    ElMessageBox.alert('订单内已有乘车人改签，无法全部改签', '改签失败', {
                        confirmButtonText: '确定',
                        showClose: false
                    });
                    return;
                }
                passengers.push(row.passenger_order_data[i].passenger_id)
            }
            let order = {
                order_id: row.order_id,
                date: row.date,
                departure_station_name: row.departure_station_name,
                arrival_station_name: row.arrival_station_name,
                passengers: passengers
            }
            let origin_order = JSON.stringify(order)
            this.$router.push({
                name: 'TicketChange',
                params: { order: origin_order }
            })
        },
        handleTicketchanges2(row, row2, index) {
            console.log(row, row2)
            let order = {
                order_id: row.order_id,
                date: row.date,
                departure_station_name: row.departure_station_name,
                arrival_station_name: row.arrival_station_name,
                passengers: [row2.passenger_id],
            }
            let origin_order = JSON.stringify(order)
            this.$router.push({
                name: 'TicketChange',
                params: { order: origin_order }
            })
        },
        async getLists() {
            axios.post('/api/train/get_order_list/', {
                user_id: 4
            }, {
                headers: {
                    "Authorization": this.token
                }
            })
                .then((response) => {
                    console.log(response)
                    this.tableData = [];
                    let data2 = response.data.data;
                    if (data2.length !== 0) {
                        data2.sort(function (a, b) {
                            return b.create_time.localeCompare(a.create_time);
                        });
                    }
                    for (let i = this.offset; i < this.offset + this.limit; i++) {
                        if (i < data2.length) {
                            if (data2[i].order_status === 'PAD') {
                                data2[i].order_status = '已支付';
                            } else {
                                continue;
                            }
                            let pas = data2[i].passenger_order_data
                            for (let j = 0; j < pas.length; j++) {
                                if (pas[j].passenger_id_type === 'CIC') {
                                    data2[i].passenger_order_data[j].passenger_id_type = '中国居民身份证'
                                }
                                else if (pas[j].passenger_id_type === 'HTP') {
                                    data2[i].passenger_order_data[j].passenger_id_type = '港澳居民来往内地通行证'
                                }
                                else if (pas[j].passenger_id_type === 'TTP') {
                                    data2[i].passenger_order_data[j].passenger_id_type = '台湾居民来往大陆通行证'
                                }
                                else if (pas[j].passenger_id_type === 'PSP') {
                                    data2[i].passenger_order_data[j].passenger_id_type = '护照'
                                }
                                else if (pas[j].passenger_id_type === 'FRI') {
                                    data2[i].passenger_order_data[j].passenger_id_type = '外国人永久居留身份在'
                                }
                                else if (pas[j].passenger_id_type === 'HMT') {
                                    data2[i].passenger_order_data[j].passenger_id_type = '港澳台居民居住证'
                                }
                                if (pas[j].ticket_type === 'ADU') {
                                    data2[i].passenger_order_data[j].ticket_type = '成人'
                                }
                                else if (pas[j].ticket_type === 'CHI') {
                                    data2[i].passenger_order_data[j].ticket_type = '儿童'
                                }
                                else if (pas[j].ticket_type === 'STU') {
                                    data2[i].passenger_order_data[j].ticket_type = '学生'
                                }
                                else if (pas[j].ticket_type === 'DOM') {
                                    data2[i].passenger_order_data[j].ticket_type = '残军'
                                }
                                if (pas[j].carriage_type === 'BUS') {
                                    data2[i].passenger_order_data[j].carriage_type = '商务座'
                                }
                                else if (pas[j].carriage_type === 'FST') {
                                    data2[i].passenger_order_data[j].carriage_type = '一等舱'
                                }
                                else if (pas[j].carriage_type === 'SND') {
                                    data2[i].passenger_order_data[j].carriage_type = '二等舱'
                                }
                                else if (pas[j].carriage_type === 'SOF') {
                                    data2[i].passenger_order_data[j].carriage_type = '软卧'
                                }
                                else if (pas[j].carriage_type === 'HAW') {
                                    data2[i].passenger_order_data[j].carriage_type = '硬卧'
                                }
                                else if (pas[j].carriage_type === 'HAZ') {
                                    data2[i].passenger_order_data[j].carriage_type = '硬座'
                                }
                            }
                            this.tableData.push(data2[i]);
                        }

                    }
                    console.log(this.tableData)
                })
                .catch((error) => {
                    console.log(error);
                    if (error.response.status == 401 || this.isLogin == false) {
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
    mounted() {

        axios.post('/api/train/get_order_list/', {
            user_id: 4
        }, {
            headers: {
                "Authorization": this.token
            }
        })
            .then((response) => {
                console.log(response)
                let list = response.data.data.filter(order => order.order_status === 'PAD')
                this.count = Math.ceil(list.length / this.page_size);
                this.getLists();
            })
            .catch((error) => {
                console.log(error);
                if (error.response.status == 401 || this.isLogin == false) {
                    router.push({ path: "/Login" });
                    ElMessage({
                        showClose: true,
                        message: '登录失效,请重新登录',
                        type: 'error',
                    })
                }
            });
    }
}
</script>

<style lang="less" scoped>
.demo-table-expand {
    font-size: 0;
}

.demo-table-expand label {
    width: 90px;
    color: #99a9bf;
}

.demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
}

.table_container {
    padding: 20px;
}

.Pagination {
    display: flex;
    justify-content: flex-start;
    margin-top: 8px;
}

.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
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
</style>
