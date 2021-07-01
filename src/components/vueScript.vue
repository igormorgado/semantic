<script>
import axios from 'axios'

export default {
  name: 'text',
  props: {
    msg: String
  },
  data() {
    return {
      queries: [ 'birds', 'scatt' ],
      description: 'Tropical birds scattered as Drake veered the Jeep' ,
      form: {
        text: ''
      },
      show: true,
      payload: {'text': " " }
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
