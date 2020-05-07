<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">
        Home
        <t></t>
      </router-link>|
      <router-link to="/create">Create</router-link>
    </div>
    <router-view />
  </div>
</template>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* background: #2c3e50; */
  position: relative;
}

#nav {
  margin-bottom: 15px;
}
.upnav {
  position: relative;
}
#nav a {
  font-weight: bold;
  color: #42b983;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.container {
  position: relative;
}
body {
  width: 100%;
  height: 100%;
  position: absolute;
  background: #181a1b;
}
</style>
