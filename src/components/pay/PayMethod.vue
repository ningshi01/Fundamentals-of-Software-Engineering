<template>
    <h2>请选择支付方式</h2>
    <div class="bank">
        <div class="bank1">
            <img src="../../assets/bank_wx.gif" width="130" height="52" title="微信支付" @click="Success(price)" style=""
                alt="微信支付">
        </div>
        <div class="bank2">
            <img src="../../assets/bank_zfb.gif" width="130" height="52" title="支付宝" @click="Success" style="" alt="支付宝">
        </div>
    </div>
    <pay-time />
    <div class="footer1">
        <div class="f_desc">
            <ul>
                <li>
                    "请您选择支付方式。如果您使用微信账户支付，
                    请点击“微信支付”按钮;如果您使用支付宝支付，
                    请点击“支付宝”按钮。"
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { ElMessageBox} from 'element-plus'
import PayTime from './PayTime'
import axios from 'axios'
import { mapState } from "vuex";
export default {
    computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
    name: 'PaymentMethod',
    data() {
        return {
            price: 5
        }
    },
    methods: {
        Success() {
            axios.post('/api/user/recharge/', {
                user_id: 4,
                amount:this.price
            }, {
                     headers:{
                         "Authorization":this.token
                     }
                })
                .then((response) => {
                    console.log(response.data);
                    let data = response.data;
                    this.userName = data.username;
                    this.balance = data.balance;
                    this.realName = data.passengers[0].name;
                    this.IDtype = data.passengers[0].id_type;
                    this.IDnumber = data.passengers[0].id_number;
                })
                .catch((error) => {
                console.log(error);
            });
            ElMessageBox.alert('您已成功充值' + this.price + '元', '充值成功', {
                confirmButtonText: '确定',
                showClose:false
            })
            this.$router.push({ name: 'Home' })
        }
    },
    components: {
        PayTime
    },
    created() {
        this.price = parseFloat(this.$route.params.price)
    }
}
</script>

<style scoped>
.bank {
    height: 180px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.bank1 {
    float: left;
    width: 200px;
}

.bank2 {
    float: right;
    width: 200px;
}

.footer1 {
    border-top: 1px dashed #BEBEBE;
    border-bottom: 1px dashed #BEBEBE;
    background-color: #F3F3F3;
    width: 100%;
    float: left;
}

.f_desc {
    width: 76%;
    line-height: 20px;
    padding-left: 46px;
    padding-bottom: 10px;
    padding-top: 10px;
    color: #666;
}

ul {
    display: block;
    list-style-type: disc;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
}

li {
    display: list-item;
    text-align: -webkit-match-parent;
}
</style>