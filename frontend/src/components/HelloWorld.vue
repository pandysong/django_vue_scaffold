<template>
  <div class="hello">
    <h2>Essential Links</h2>

      <form>
        <input type="file" name="file" @change="handleFile">
        <div class="submit">
        <button type="submit" @click="submitFile">submit</button>
        </div>
      </form>
      <p v-if='filesize'> file size: {{ filesize }} </p>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a
          href="http://vuejs-templates.github.io/webpack/"
          target="_blank"
        >
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
        >
          awesome-vue
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true

export default {
  name: 'HelloWorld',
  data: () => ({
    file: '',
    filesize: 0
  }),
  components: {
  },
  methods: {
    submitFile () {
      // send a GET request to backend and get teh csrftoken from cookie
      // we will cover it more in the backend parts
      fetch('http://localhost:8080/api/csrf')

      // The csrftoken is embedded in the cookie
      const csrfToken = this.getCookie('csrftoken')
      // console.log(csrfToken)
      let formData = new FormData()
      formData.append('file', this.file)
      console.log('>> formData >> ', formData)

      var comp = this

      // You should have a server side REST API
      axios.post('http://localhost:8000/api/upload',
        formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': csrfToken
          }
        })
        .then(function (response) {
          console.log('SUCCESS!! with response', response.data)
          console.log(comp)
          comp.filesize = response.data['filesize']
        })
        .catch(function () {
          console.log('FAILURE!!')
        })
    },
    handleFile (event) {
      this.file = event.target.files[0]
      console.log('>>>> 1st element in files array >>>> ', this.file)
    },
    getCookie (name) {
      var value = '; ' + document.cookie
      var parts = value.split('; ' + name + '=')
      if (parts.length === 2) return parts.pop().split(';').shift()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
