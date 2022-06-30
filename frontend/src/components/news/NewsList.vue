<template>
  <div class="my-4">
    <b-row v-for="newsObj in news.newsList" :key="newsObj.id">
      <b-col cols="12" class="mx-auto">
        <b-card
          :title="newsObj.headline"
          :img-src="newsObj.thumbnail_url"
          img-alt="Thumbnail"
          img-top
          tag="article"
          class="mb-2"
        >
          <b-card-text>
            <p>Source: {{ newsObj.news_source || "N/A" }}</p>
            <p>Country: {{ newsObj.country || "N/A" }}</p>
          </b-card-text>

          <b-button :href="newsObj.news_url" target="_blanks" variant="primary"
            >View</b-button
          >
        </b-card>
      </b-col>
    </b-row>

    <b-row class="mt-4">
      <b-col cols="12" class="d-flex justify-content-end">
        <b-pagination
          v-model="currentPage"
          :per-page="perPage"
          :total-rows="news.newsCount"
          @change="fetchNewsList"
        >
        </b-pagination>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      perPage: 20,
      currentPage: 1
    };
  },

  created() {
    this.fetchNewsList(1);
  },

  computed: {
    ...mapState(["news"])
  },

  methods: {
    fetchNewsList(currentPage) {
      this.$store.dispatch("news/getNewsList", {
        page: currentPage,
        perPage: this.perPage
      });
    }
  }
};
</script>
