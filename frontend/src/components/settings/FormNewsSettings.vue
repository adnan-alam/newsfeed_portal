<template>
  <div>
    <b-form @submit.prevent="onSubmit">
      <b-form-group label="Country of news">
        <Select2
          v-model="form.country"
          :options="countryOptions"
          :settings="{
            width: '100%',
            placeholder: 'Select Country',
            multiple: true
          }"
        />
      </b-form-group>
      <b-form-group label="Source of news">
        <Select2
          v-model="form.source"
          :options="sourceOptions"
          :settings="{
            width: '100%',
            placeholder: 'Select Source',
            multiple: true
          }"
        />
      </b-form-group>
      <b-form-group label="Keywords">
        <b-form-tags
          v-model="form.keywords"
          separator=" "
          placeholder="Enter keywords separated by space"
          remove-on-delete
          no-add-on-enter
        ></b-form-tags>
      </b-form-group>

      <div class="my-4">
        <b-button type="submit" variant="primary">Save</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
import Select2 from "v-select2-component";

export default {
  components: { Select2 },

  data() {
    return {
      newsSourceList: [],
      settingsId: null,

      form: {
        country: [],
        source: [],
        keywords: []
      }
    };
  },

  created() {
    this.fetchNewsSourceListWithoutPagination();
    this.fetchUserNewsSettings();
  },

  computed: {
    countryOptions() {
      let options = [];
      let countryList = [];

      this.newsSourceList.forEach(element => {
        if (element.country && !countryList.includes(element.country)) {
          countryList.push(element.country);
        }
      });

      countryList.sort();

      countryList.forEach(element => {
        options.push({
          id: element,
          text: element
        });
      });

      return options;
    },

    sourceOptions() {
      let options = [];
      let sourceList = [];

      this.newsSourceList.forEach(element => {
        if (element.name && !sourceList.includes(element.name)) {
          sourceList.push(element.name);
        }
      });

      sourceList.sort();

      sourceList.forEach(element => {
        options.push({
          id: element,
          text: element
        });
      });

      return options;
    }
  },

  methods: {
    fetchNewsSourceListWithoutPagination() {
      this.$store
        .dispatch("news/getNewsSourceListWithoutPagination")
        .then(resp => {
          if (resp.status == 200) {
            this.newsSourceList = resp.data;
          }
        });
    },

    fetchUserNewsSettings() {
      this.$store.dispatch("news/getUserNewsSettings").then(resp => {
        if (resp.status == 200) {
          let settingsObj = resp.data[0];
          this.settingsId = settingsObj.id;
          this.form.country = settingsObj.country;
          this.form.source = settingsObj.source;
          this.form.keywords = settingsObj.keywords;
        }
      });
    },

    onSubmit() {
      this.$store.dispatch("news/updateNewsSettings", {
        settingsId: this.settingsId,
        data: this.form
      });
    }
  }
};
</script>
