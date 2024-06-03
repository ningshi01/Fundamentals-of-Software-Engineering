<template>
    <div>
        <el-row>
            <el-col>
                <el-countdown title="剩余支付时间" :value="time" value-style="font-size: 30px;" @finish="
                    finish" />
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { ElMessageBox } from 'element-plus'
import { ref } from 'vue'
export default {
    name: 'PayTime',
    data() {
        return {

        }
    },
    methods: {
        finish() {
            ElMessageBox.alert('充值超时', '充值失败', {
                confirmButtonText: '确定',
                showClose:false
            })
            this.$router.push({
                name: 'Home'
            })
        }
    },
    setup() {
        //const time = ref(Date.now() + 1000 * 60 * 10)
        const time = ref(Date.now() + 1000 * 10);
        return {
            time
        }
    }
}

</script>

<style scoped>
.el-col {
    text-align: center;
}
</style>