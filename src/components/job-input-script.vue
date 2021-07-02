<template>
  <div>
    <div class="container">
      <h1>{{ msg }}</h1>
      <b-form @submit="getKeywords" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Job Description:"
          label-for="input-1"
          description="Copy and paste in the text you want to work with.">
          <b-form-textarea
            id="input-1"
            v-model="form.text"
            placeholder="Enter your job text here"
            required
            rows=10
            max-rows=100>
          </b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
      <br><br>
      <text-highlight :queries="queries">{{ description }}</text-highlight>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'text',
  props: {
    msg: String
  },
  data() {
    return {
      queries: ['birds', 'scatt'],
      description: 'Tropical birds scattered as Drake veered the Jeep' ,
      form: {
        text: ''
      },
      show: true,
      payload: {'text': ""}
    }
  },
  methods: {
    getKeywords() {

      this.show = false
      this.description = this.form.text
      const path = '/keywords'
      this.payload.text = this.form.text
      axios.post(path, this.payload)
        .then((res) => {
          this.queries = res.data.keywords
          this.show = true
        })
        .catch((error) => {
          // eslint-disable-next line
          console.error(error)
          this.description = "error";
          this.show = true;
        })
    },
    onReset() {
      this.form.text = ""
      this.description = "Tropical birds scattered as Drake veered the jeep"
      this.queries = ['birds', 'scatt']
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>
