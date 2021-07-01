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
