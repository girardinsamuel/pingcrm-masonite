<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">
      <inertia-link
        class="text-indigo-400 hover:text-indigo-600"
        :href="route('users')"
        >Users</inertia-link
      >
      <span class="font-medium text-indigo-400">/</span> Create
    </h1>
    <div class="max-w-3xl overflow-hidden bg-white rounded shadow">
      <form @submit.prevent="submit">
        <div class="flex flex-wrap p-8 -mb-8 -mr-6">
          <text-input
            v-model="form.first_name"
            :errors="errors.first_name"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="First name"
          />
          <text-input
            v-model="form.last_name"
            :errors="errors.last_name"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Last name"
          />
          <text-input
            v-model="form.email"
            :errors="errors.email"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Email"
          />
          <text-input
            v-model="form.password"
            :errors="errors.password"
            class="w-full pb-8 pr-6 lg:w-1/2"
            type="password"
            autocomplete="new-password"
            label="Password"
          />
          <select-input
            v-model="form.owner"
            :errors="errors.owner"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Owner"
          >
            <option :value="true">Yes</option>
            <option :value="false">No</option>
          </select-input>
          <file-input
            v-model="form.photo"
            :errors="errors.photo"
            class="w-full pb-8 pr-6 lg:w-1/2"
            type="file"
            accept="image/*"
            label="Photo"
          />
        </div>
        <div
          class="flex items-center justify-end px-8 py-4 bg-gray-100 border-t border-gray-200"
        >
          <loading-button :loading="sending" class="btn-indigo" type="submit"
            >Create User</loading-button
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
import FileInput from "@/Shared/FileInput";

export default {
  metaInfo: { title: "Create User" },
  layout: Layout,
  components: {
    LoadingButton,
    SelectInput,
    TextInput,
    FileInput,
  },
  props: {
    errors: Object,
  },
  remember: "form",
  data() {
    return {
      sending: false,
      form: {
        first_name: null,
        last_name: null,
        email: null,
        password: null,
        owner: false,
        photo: null,
      },
    };
  },
  methods: {
    submit() {
      this.sending = true;

      var data = new FormData();
      data.append("first_name", this.form.first_name || "");
      data.append("last_name", this.form.last_name || "");
      data.append("email", this.form.email || "");
      data.append("password", this.form.password || "");
      data.append("owner", this.form.owner ? "1" : "0");
      data.append("photo", this.form.photo || "");

      this.$inertia
        .post(this.route("users.store"), data)
        .then(() => (this.sending = false));
    },
  },
};
</script>
