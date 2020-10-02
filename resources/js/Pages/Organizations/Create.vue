<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">
      <inertia-link
        class="text-indigo-400 hover:text-indigo-600"
        :href="route('organizations')"
        >Organizations</inertia-link
      >
      <span class="font-medium text-indigo-400">/</span> Create
    </h1>
    <div class="max-w-3xl overflow-hidden bg-white rounded shadow">
      <form @submit.prevent="submit">
        <div class="flex flex-wrap p-8 -mb-8 -mr-6">
          <text-input
            v-model="form.name"
            :errors="errors.name"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Name"
          />
          <text-input
            v-model="form.email"
            :errors="errors.email"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Email"
          />
          <text-input
            v-model="form.phone"
            :errors="errors.phone"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Phone"
          />
          <text-input
            v-model="form.address"
            :errors="errors.address"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Address"
          />
          <text-input
            v-model="form.city"
            :errors="errors.city"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="City"
          />
          <text-input
            v-model="form.region"
            :errors="errors.region"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Province/State"
          />
          <select-input
            v-model="form.country"
            :errors="errors.country"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Country"
          >
            <option :value="null" />
            <option value="CA">Canada</option>
            <option value="US">United States</option>
          </select-input>
          <text-input
            v-model="form.postal_code"
            :errors="errors.postal_code"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Postal code"
          />
        </div>
        <div
          class="flex items-center justify-end px-8 py-4 bg-gray-100 border-t border-gray-200"
        >
          <loading-button :loading="sending" class="btn-indigo" type="submit"
            >Create Organization</loading-button
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Layout from "@/Shared/Layout";
import LoadingButton from "@/Shared/LoadingButton";
import SelectInput from "@/Shared/SelectInput";
import TextInput from "@/Shared/TextInput";

export default {
  metaInfo: { title: "Create Organization" },
  layout: Layout,
  components: {
    LoadingButton,
    SelectInput,
    TextInput,
  },
  props: {
    errors: Object,
  },
  remember: "form",
  data() {
    return {
      sending: false,
      form: {
        name: null,
        email: null,
        phone: null,
        address: null,
        city: null,
        region: null,
        country: null,
        postal_code: null,
      },
    };
  },
  methods: {
    submit() {
      this.sending = true;
      this.$inertia
        .post(this.route("organizations.store"), this.form)
        .then(() => (this.sending = false));
    },
  },
};
</script>
