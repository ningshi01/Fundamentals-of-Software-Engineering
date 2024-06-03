<template>
    <div class="nav_body" id="asbody">
        <div class="l-navbar" id="navbar">
            <nav class="nav" id="nav_1">
                <div>
                    <div class="nav_brand">
                        <!-- <ion-icon name="menu-outline" class="nav_toggle" id="nav_toggle"></ion-icon> -->
                        <ion-icon name="menu-outline" class="nav_toggle" id="nav-toggle"></ion-icon>

                        <a href="#" class="nav_logo">{{msg1}}</a>
                    </div>
                    <div class="nav_list">

                        <a v-bind:href="href1" class="nav_link">
                            <ion-icon name="home-outline" class="nav_icon" ></ion-icon>
                            <span class="nav_name"><b>{{msg2}}</b></span>
                        </a>

                        <a v-bind:href="href2" class="nav_link">
                            <ion-icon name="folder-outline" class="nav_icon" ></ion-icon>
                            <span class="nav_name"><b>{{msg3}}</b></span>
                        </a>

                        <a v-bind:href="href3" class="nav_link">
                            <ion-icon name="chatbubbles-outline" class="nav_icon" ></ion-icon>
                            <span class="nav_name"><b>{{msg4}}</b></span>
                        </a>

                        <a v-bind:href="href4" class="nav_link">
                            <ion-icon name="settings-outline" class="nav_icon" ></ion-icon>
                            <span class="nav_name"><b>{{ msg5 }}</b></span>
                        </a>

                    </div>
                </div>
                <a v-bind:href="href5" class="nav_link">
                    <ion-icon name="log-out-outline" class="nav_icon" ></ion-icon>
                    <span class="nav_name">退出登陆</span>
                </a>
            </nav>
        </div>
    </div>>

</template>

<style scoped>
@import '../../assets/css/style.css';
</style>

<script>

export default {
    name: 'My_fornav',
    data() {
        return {
        }
    },
    props: {
        href1: String,
        href2: String,
        href3: String,
        href4: String,
        href5: String,
        msg1 : String,
        msg2 : String,
        msg3 : String,
        msg4 : String,
        msg5 : String,
    },
    mounted() {
        this.showMenu('nav-toggle', 'navbar', 'asbody');
        this.setupLinkClick();
        this.setupCollapseClick();
    },
    methods: {
        showMenu(toggleId, navbarId, bodyId) {
            const toggle = document.getElementById(toggleId);
            const navbar = document.getElementById(navbarId);
            const bodypadding = document.getElementById(bodyId);

            if (toggle && navbar) {
                toggle.addEventListener('click', () => {
                    navbar.classList.toggle('expander');
                    bodypadding.classList.toggle('body-pd');
                });
            }
        },
        setupLinkClick() {
            const linkColor = document.querySelectorAll(".nav_link");
            linkColor.forEach(l => l.addEventListener('click', this.colorLink));
        },
        colorLink() {
            const linkColor = document.querySelectorAll(".nav_link");
            linkColor.forEach(l => l.classList.remove("active"));
        },
        setupCollapseClick() {
            const linkCollapse = document.getElementsByClassName('collapse__link');
            for (let i = 0; i < linkCollapse.length; i++) {
                linkCollapse[i].addEventListener('click', () => {
                const collapseMenu = linkCollapse[i].nextElementSibling;
                collapseMenu.classList.toggle('showCollapse');

                const rotate = collapseMenu.previousElementSibling;
                rotate.classList.toggle("");
                });
            }
        }
  }
}
</script>
