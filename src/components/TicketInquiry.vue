<template>
    <div class="fillcontain">
        <meta  http-equiv="Cache-Control" content="no-cache,no-store,must-revlidate">
        <meta  http-equiv="Expires" content="O">
        <meta http-equiv="Pragma" content="no-cache">

        <el-form :model="searchForm"  ref="searchForm">
            <el-row :gutter="20" style="margin-left: 180px;margin-top: 10px;width: 1000px">
                <el-col :span="6"><div class="grid-content bg-purple">
                    <el-autocomplete
                        class="inline-input"
                        v-model="searchForm.start_station"
                        :fetch-suggestions="query  => searchElements(query,index)"
                        placeholder="请输入始发站"
                        :trigger-on-focus="true"
                        @select="selectedItem => handleSelect(selectedItem,index)"
                    ><template v-slot="{item}">
                        {{item}}
                    </template></el-autocomplete>
                </div></el-col>
                <el-col :span="6"><div class="grid-content bg-purple" style="margin-left: 20px">
                    <el-autocomplete
                        class="inline-input"
                        v-model="searchForm.end_station"
                        :fetch-suggestions="query  => searchElements2(query,index)"
                        placeholder="请输入终点站"
                        :trigger-on-focus="true"
                        @select="selectedItem => handleSelect2(selectedItem,index)"
                    >
                    <template v-slot="{item}">
                        {{item}}
                    </template>
                </el-autocomplete>
                </div></el-col>
                <el-col :span="6"><div class="grid-content bg-purple" style="margin-left: 20px">
                    <div class="block">
                        <el-date-picker
                            v-model="searchForm.datetime"
                            type="date"
                            placeholder="选择日期">
                        </el-date-picker>
                    </div>
                </div></el-col>
                <el-col :span="6"><div class="grid-content bg-purple">
                    <!-- 点击时调用submitForm函数并传递 searchForm参数-->
                    <el-button type="primary" round  @click="submitForm('searchForm')">搜索</el-button>
                </div></el-col>
                <el-switch
                    style="margin-top: 30px;margin-left: 20px"
                    v-model="value1"
                    @click.self="handelUpdate()"
                    inactive-text="按开车时间排序"
                    active-text="按运行时间排序">
                </el-switch>
            </el-row>
        </el-form>
        <div class="table_container">
            <el-table
                :data="tableData"
                style="width: 100%"
                row-key="train_number">

                <el-table-column
                    label="车次"
                    prop="train_number">
                </el-table-column>
                <el-table-column
                    label="出发站"
                    prop="start_station">
                </el-table-column>
                <el-table-column
                    label="到达站"
                    prop="end_station">
                </el-table-column>
                <el-table-column
                    label="出发时间"
                    prop="start_time">
                </el-table-column>
                <el-table-column
                    label="到达时间"
                    prop="arrive_time">
                </el-table-column>
                <el-table-column
                    label="特等座/软卧"
                    prop="high_seat_count">
                </el-table-column>
                <el-table-column
                    label="一等座/硬卧"
                    prop="medium_seat_count">
                </el-table-column>
                <el-table-column
                    label="二等座/硬座"
                    prop="low_seat_count">
                </el-table-column>
                <el-table-column label="操作" width="200">
                    <template v-slot:default="scope">
                        <el-button
                            size="mini"
                            type="Success"
                            @click="check(scope.$index,searchForm.datetime,scope.row.train_no,scope.row.start_no,scope.row.end_no,
                            scope.row.train_number,scope.row.high_seat_price,scope.row.medium_seat_price,scope.row.low_seat_price)">预定
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <!-- Table -->

        </div>
        <el-button @click="check1">点我点我</el-button>
        <el-button @click="check2">123</el-button>
    </div>
</template>
<script>
    import axios from "axios";
    import { ElMessage } from 'element-plus'
    import router from "@/router";
    import { mapState } from "vuex";
    export default {
        computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },

        data(){
            return {
                value1: false,
                tableData: [
                ],
                selectTable: {},
                searchForm:
                    {
                        start_station: '',
                        end_station:'',
                        datetime:''

                    },
                high_seat:[
                    {
                        carriage_number:"1",
                        seat_type:"2",
                        upper_num:"3",
                        lower_num:"4"
                    }
                ],
                medium_seat:[
                    {
                        carriage_number:"1",
                        seat_type:"2",
                        upper_num:"3",
                        middle_num:"5",
                        lower_num:"4"
                    }
                ],
                low_seat:[
                    {
                        carriage_number:"1",
                        seat_type:"2",
                        A_num:"3",
                        B_num:"5",
                        C_num:"4",
                        D_num:"4",
                        E_num:"4",
                        F_num:"4"
                    }
                ],
                high_seat_GD:[
                    {
                        carriage_number:"1",
                        seat_type:"2",
                        A_num:"3",
                        B_num:"5",
                        C_num:"4"
                    }
                ],
                medium_seat_GD:[
                    {
                        carriage_number:"1",
                        seat_type:"2",
                        A_num:"3",
                        B_num:"5",
                        C_num:"4",
                        D_num:"4"
                    }
                ],
                low_seat_GD:[
                    {
                        carriage_number:"1",
                        seat_type:"2",
                        A_num:"3",
                        B_num:"5",
                        C_num:"4",
                        D_num:"4",
                        E_num:"4"
                    }
                ],
                dialogTableVisible: false,
                dialogTableVisible_GD: false,
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                formLabelWidth: '120px',
                stationData:["阿克苏", "阿拉善", "阿勒泰", "阿图什", "安康", "安庆", "鞍山", "安顺", "安溪", "安阳", "巴彦淖尔", "巴音郭楞蒙古自治州", "巴中", "白城", "百色", "白山", "白银", "蚌埠", "保定", "宝鸡", "保山", "包头", "北海", "北京", "本溪", "毕节", "璧山", "滨州", "博乐", "亳州", "沧州", "长春", "常德", "昌吉", "昌江", "长沙", "长寿", "长汀", "长治", "常州", "潮州", "郴州", "承德", "成都", "澄迈", "赤峰", "池州", "崇仁", "崇左", "楚雄", "滁州", "达川", "大理", "大连", "大庆", "大同", "达州", "大足", "丹东", "儋州", "德令哈", "德阳", "德州", "垫江", "定西", "东方", "东莞", "东营", "都匀", "鄂尔多斯", "峨山", "鄂州", "恩施", "二连浩特", "防城港", "丰都", "奉节", "凤阳", "佛山", "涪陵", "富平", "抚顺", "莆田", "阜新", "阜阳", "抚州", "福州", "赣州", "岗嘎", "格尔木", "个旧", "贡嘎", "固原", "广安", "广元", "广州", "贵港", "桂林", "贵阳", "哈尔滨", "哈密", "海北州", "海东", "海口", "海西州", "海晏", "邯郸", "汉中", "杭州", "鹤壁", "河池", "合川", "合肥", "鹤岗", "和田", "河源", "菏泽", "贺州", "黑河", "衡水", "衡阳", "呼和浩特", "葫芦岛", "呼伦贝尔", "湖州", "桦南", "华阴", "淮安", "淮北", "怀化", "淮南", "桓台", "黄冈", "黄山", "黄石", "惠州", "吉安", "吉林", "济南", "济宁", "吉首", "鸡西", "济源", "加查", "加格达奇", "佳木斯", "嘉兴", "嘉峪关", "建宁", "江边村", "江津", "江门", "焦作", "揭阳", "金昌", "晋城", "金华", "晋中", "锦州", "景德镇", "景洪", "荆门", "荆州", "九江", "酒泉", "喀什", "开封", "凯里", "克拉玛依", "库尔勒", "昆明", "拉萨", "来宾", "莱芜", "来舟", "兰州", "琅勃拉邦", "廊坊", "朗县", "老挝万荣", "乐东", "乐山", "丽江", "丽水", "连云港", "梁平", "聊城", "辽阳", "辽源", "临沧", "临川", "临汾", "临高", "林口", "临沂", "林芝", "陵水", "灵武", "六安", "六盘水", "柳州", "陇南", "龙岩", "娄底", "芦溪", "泸州", "洛阳", "吕梁", "马鞍山", "马桥河", "麦园", "茫崖", "茂名", "眉山", "梅州", "勐腊", "蒙自", "米林", "绵阳", "磨丁", "墨江", "牡丹江", "那曲", "南昌", "南充", "南涧", "南京", "南宁", "南平", "南通", "南阳", "内江", "宁波", "宁德", "宁洱", "盘锦", "攀枝花", "彭水", "平顶山", "平凉", "萍乡", "蒲城", "普洱", "濮阳", "蕲春", "綦江", "齐齐哈尔", "七台河", "潜江", "黔江", "秦皇岛", "钦州", "青岛", "青铜峡", "庆阳", "清远", "琼海", "曲靖", "衢州", "泉州", "日喀则", "日照", "荣昌", "三门峡", "三明", "三亚", "桑日", "厦门", "沙县", "山南", "汕头", "汕尾", "上海", "上杭", "商洛", "商丘", "上饶", "邵东", "韶关", "绍兴", "邵阳", "神农架", "沈阳", "深圳", "石河子", "石家庄", "十堰", "石柱", "石柱县", "石嘴山", "双鸭山", "朔州", "四平", "松原", "宿迁", "苏州", "宿州", "绥化", "遂宁", "随州", "塔城", "漯河", "泰安", "太原", "泰州", "台州", "唐山", "天津", "天门", "天水", "铁岭", "铜川", "通化", "通辽", "铜陵", "潼南", "铜仁", "吐鲁番", "万宁", "万象", "万州", "潍坊", "威海", "渭南", "文昌", "文山", "温州", "乌海", "武汉", "芜湖", "乌兰察布", "武隆", "乌鲁木齐", "巫山", "武威", "无锡", "武穴", "吴忠", "梧州", "西安", "西昌", "锡林郭勒", "西宁", "浠水", "咸宁", "仙桃", "咸阳", "香港", "湘潭", "襄阳", "孝感", "新乡", "信阳", "新余", "忻州", "兴安", "邢台", "兴义", "秀山", "许昌", "徐州", "宣城", "雅安", "延安", "延边", "盐城", "烟台", "阳江", "漾濞", "阳泉", "扬州", "宜宾", "宜昌", "伊春", "宜春", "伊宁", "益阳", "仪征", "银川", "营口", "鹰潭", "永川", "永平", "永州", "酉阳", "于都", "榆林", "玉林", "玉门", "玉溪", "元江", "岳阳", "运城", "云浮", "云阳", "枣庄", "扎囊", "湛江", "张家界", "张家口", "张掖", "漳州", "肇庆", "昭通", "朝阳", "镇江", "郑州", "重庆", "中山", "中卫", "周口", "珠海", "驻马店", "株洲", "淄博", "自贡", "资溪", "资阳", "遵义"],
            }
        },
        methods: {
            check2(){
                console.log(this.token);
            },
            

            check1(){
                axios.post('/api/user/get_user_info/',{
                     headers:{
                        "Authorization":this.token
                     }
                }).then((response) => {
                    console.log(response);
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
            TrainRank()
            {
                if(this.value1 === false)
                {
                    for(let i = 0 ; i < this.tableData.length ; i++)
                    {
                        for(let j = 0 ; j <this.tableData.length - i -1 ; j++ )
                        {
                            if(this.transferTime(this.tableData[j].start_time) >this.transferTime(this.tableData[j+1].start_time))
                            {
                                let temp = this.tableData[j];
                                this.tableData[j] = this.tableData[j+1];
                                this.tableData[j+1] = temp;
                            }
                        }
                    }
                }
                else
                {
                    for(let i = 0 ; i < this.tableData.length ; i++)
                    {
                        for(let j = 0 ; j <this.tableData.length - i -1 ; j++ )
                        {
                            if(this.transferTime(this.tableData[j].running_time) >this.transferTime(this.tableData[j+1].running_time))
                            {
                                let temp = this.tableData[j];
                                this.tableData[j] = this.tableData[j+1];
                                this.tableData[j+1] = temp;
                            }
                        }
                    }
                }
            },
            check(index,datetime,train_no,start_no,end_no,train_number,high_seat_price,medium_seat_price,low_seat_price)
            {           
                        
                const date1 = new Date(this.searchForm.datetime)
                        const year = date1.getFullYear()
                        const month = String(date1.getMonth() + 1).padStart(2, '0')
                        const day = String(date1.getDate()).padStart(2, '0')
                        const datetime2=`${year}-${month}-${day}`
                        const Object={
                        datetime: datetime2,
                        train_no: train_no,
                        start_no:start_no,
                        end_no:end_no,
                        train_number:train_number,
                        high_seat_price:high_seat_price,
                        medium_seat_price:medium_seat_price,
                        low_seat_price:low_seat_price
                        }
                        const Temp = JSON.stringify(Object)
                        this.$router.push({
                            name: "TicketOrder",
                            params: {
                            temp: Temp
                            }
                        })
            },
            checkTime: (i) => {
                    if (i < 10) {
                        i = '0' + i;
                    }
                    return i;
                 },

            // queryString是用户在输入框中输入的文本字符串，用于进行搜索。cb是一个回调函数，用于在搜索完成时将搜索结果传递给自动完成组件。
            //从"stationData"属性中获取所有的车站数据列表，存储在"houseNumberList"变量中。
            //根据用户输入的queryString字符串，通过调用"createFilter"方法创建一个过滤函数，用于过滤出符合条件的车站数据列表。
            
            //先调用this.$refs[formName].validate方法验证表单数据的有效性,有效再进行操作
            
            async submitForm(formName) {
                this.$refs[formName].validate(async (valid) => {
                    if (valid) {
                        const date1 = new Date(this.searchForm.datetime)
                        const year = date1.getFullYear()
                        const month = String(date1.getMonth() + 1).padStart(2, '0')
                        const day = String(date1.getDate()).padStart(2, '0')
                        this.tableData = [];
                        //调用异步请求方法queryTrainTicket，根据表单中填写的出发地、目的地和日期时间等信息，从后端API获取符合条件的列车信息。
                        axios.post('/api/train/query_train/', {            
                        departure_city:this.searchForm.start_station,
                        arrival_city:this.searchForm.end_station,
                        date:`${year}-${month}-${day}`,
                    },{
             headers:{
                   "Authorization":this.token
                     }
                }) 
                    .then((response) => {
                                if(response.status==200){
                                console.log("查询成功");
                                }
                                this.$message({
                                    type: 'success',
                                    message: '查询成功'
                                });
                                this.tableData = [];
                                console.log(response.data.data)
                                for(let i = 0 ; i < response.data.data.length ; i++ )
                                {
                                    if(response.data.data[i].train_type=='HSR'){
                                    const tableData = {};
                                    console.log(response.data.data[i].ticket.BUS)
                                    tableData.train_no = response.data.data[i].train_type;
                                    tableData.train_number = response.data.data[i].train_name;
                                    tableData.start_station =response.data.data[i].departure_station_name;
                                    tableData.end_station = response.data.data[i].arrival_station_name;
                                    tableData.start_time =response.data.data[i].departure_time;
                                    tableData.arrive_time = response.data.data[i].arrival_time;
                                    tableData.high_seat_price = response.data.data[i].ticket.SND.price;
                                    tableData.medium_seat_price= response.data.data[i].ticket.FST.price ;
                                    tableData.low_seat_price = response.data.data[i].ticket.BUS.price;
                                    console.log("下面是御座")
                                    console.log(response.data.data[i].ticket.SND.count)
                                    tableData.high_seat_count = response.data.data[i].ticket.SND.count;
                                    tableData.medium_seat_count = response.data.data[i].ticket.FST.count ;
                                    tableData.low_seat_count = response.data.data[i].ticket.BUS.count;
                                    tableData.end_no = response.data.data[i].end_stop_id
                                    tableData.start_no =response.data.data[i].start_stop_id;
                                    this.tableData.push(tableData);
                                    }
                                    else{
                                    const tableData = {};

                                    tableData.train_no = response.data.data[i].train_type;
                                    tableData.train_number = response.data.data[i].train_name;
                                    tableData.start_station =response.data.data[i].departure_station_name;
                                    tableData.end_station = response.data.data[i].arrival_station_name;
                                    tableData.start_time =response.data.data[i].departure_time;
                                    tableData.arrive_time = response.data.data[i].arrival_time;
                                    tableData.high_seat_price = response.data.data[i].ticket.HAW.price;
                                    tableData.medium_seat_count = response.data.data[i].ticket.HAZ.price ;
                                    tableData.low_seat_count = response.data.data[i].ticket.SOF.price;

                                    tableData.high_seat_count = response.data.data[i].ticket.HAW.count;
                                    tableData.medium_seat_count = response.data.data[i].ticket.HAZ.count ;
                                    tableData.low_seat_count = response.data.data[i].ticket.SOF.count;
                                    tableData.end_no = response.data.data[i].end_stop_id
                                    tableData.start_no =response.data.data[i].start_stop_id;
                                    this.tableData.push(tableData);
                                    }
                                }
                                console.log(this.tableData)
                                this.TrainRank();
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

                });
            },
                                
            searchElements(query,index){
                const result = this.stationData.filter(element => element.includes(query));
                console.log(index)
                return result;
            },
            handleSelect(selectedItem) {
             this.searchForm.start_station = selectedItem;
        },
        searchElements2(query,index){
                const result = this.stationData.filter(element => element.includes(query));
                console.log(index)
                return result;
            },
        handleSelect2(selectedItem) {
             this.searchForm.end_station = selectedItem;
        }
        

        },
        //对查询的信息进行排序

            handelUpdate()
            {
                this.TrainRank();

            },
           

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
    .table_container{
        padding: 20px;
    }
    .Pagination{
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