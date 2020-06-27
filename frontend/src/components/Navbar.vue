<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link to='/' class="navbar-brand">QuestionTime</router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <router-link to='/' class="btn btn-sm btn-outline-primary">Home</router-link>
                    </li>
                    <li class="nav-item mx-1">
                        <router-link to='/about' class="btn btn-sm btn-outline-secondary">About</router-link>

                    </li>
                    
                    <li class="nav-item">
                        <a class="btn btn-sm btn-outline-danger" href="/accounts/logout">Logout</a>
                    </li>
                </ul>
                
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavbarComponent'
}
</script>

<style scoped>
.my-navbar{
    border: 1px solid #ddd;
}
.navbar-brand{
    font-weight: bold;
    font-size: 130%;
}
.navbar-brand:hover{
    color: royalblue;
}
</style>