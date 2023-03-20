<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Vue.js</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  </head>
  <body>
    <div id="app">
      <p v-if="testif">조건문</p>
    </div>
    <br />
    
    <script>
      var vm = new Vue({
        el: '#app',
        data: {
          testif: false
        }
      });
    </script>
  </body>
</html>