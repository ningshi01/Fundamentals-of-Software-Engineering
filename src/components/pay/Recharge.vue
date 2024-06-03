<template>
    <h2>请输入您要充值的金额：</h2>
    <input type="text" v-model="rechargePrice" placeholder="充值金额应为0-5000元">
    <button @click="submitRecharge(rechargePrice)">提交</button>
</template>

<script>
import { ElMessageBox } from 'element-plus'
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Recharge',
    data(){
        return{
            rechargePrice:0
        }
    },
    methods: {
        submitRecharge(rechargePrice){
            if (!isValidAmount(rechargePrice)) {
                ElMessageBox.alert('输入金额不正确', '充值失败', {
                    confirmButtonText: '确定',
                    showClose:false
                })
            } else {

                //bus.emit('pay', rechargePrice);
                this.$router.push({
                    name: 'payMethod',
                    params: { price: rechargePrice }
                })
            }
        }
    }

}
function isValidAmount(amount) {
    // 判断是否为数字
    if (isNaN(amount)) {
        return false;
    }
    // 判断是否为正数
    if (amount <= 0) {
        return false;
    }
    // 判断是否超出范围
    if (amount > 5000) {
        return false;
    }
    // 判断小数位数是否合法
    const decimalPlaces = (amount.toString().split('.')[1] || '').length;
    if (decimalPlaces > 2) {
        return false;
    }
    // 如果通过了所有的判定条件，则认为金额数合法
    return true;
}
</script>

<style scoped>
button {
    background-color: lightblue;
    /* 按钮背景颜色 */
    border-radius: 6px;
    /* 圆角半径 */
    border: none;
    /* 去掉边框 */
    color: #fff;
    /* 文字颜色 */
    cursor: pointer;
    /* 光标样式 */
    font-size: 16px;
    /* 字体大小 */
    padding: 12px 24px;
    /* 按钮内边距 */
    text-align: center;
    /* 文字居中 */
    text-decoration: none;
    /* 去掉下划线 */
    display: inline-block;
    /* 将按钮设置为块级元素 */
    margin-left: 5px;
}

button:hover {
    background-color: #0069d9;
    /* 悬浮时的背景颜色 */
    color: #fff;
    /* 悬浮时的文字颜色 */
}

button:active {
    background-color: #005cbf;
    /* 按下时的背景颜色 */
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
    /* 按下时的阴影效果 */
}

input {
    height: 40px;
    border-radius: 6px;
    /* 圆角半径 */
}
</style>