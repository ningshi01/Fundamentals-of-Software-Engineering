<template>
    <div class="center-main" id="informationView">
        <form id="modifyUserForm">
            <div class="panel-border" id="js-minHeight">
                <!-- 基本信息 -->
                <CM></CM>
                <div class="line-dashed"></div>
                <!-- 附加信息 -->
                <PA></PA>
                
                <!-- 学生资质查询 -->
                <div class="line-dashed"></div>
                <!-- 选择车站下拉框 -->
            </div>
        </form>
    </div>
</template>


<script>
    import CM from './SelfComponents/ContactMethod'
    import PA from './SelfComponents/Passengers'
    export default{
        name:'SelfCenter',
        components:{
            CM,
            PA
        }
    }
</script>



<style scoped>
* {
    margin: 0;
    padding: 0;
}

.center-main {
    color: #333;
    -webkit-text-size-adjust: 100%;
    font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    font-size: 14px;
    line-height: 1.5;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    width: 90%;
    margin-right: 6%;
    float: right;
}

.panel-border {
    color: #333;
    -webkit-text-size-adjust: 100%;
    font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    font-size: 14px;
    line-height: 1.5;
    box-sizing: border-box;
    margin: 0;
    border: 1px solid #dedede;
    padding: 20px;
}

.line-dashed {
    height: 1px;
    border-top: 1px dashed #383535;
    margin: 15px 0;
}





</style>