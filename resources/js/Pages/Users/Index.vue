<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">Users</h1>
    <div class="flex items-center justify-between mb-6">
      <search-filter
        v-model="form.search"
        class="w-full max-w-md mr-4"
        @reset="reset"
      >
        <label class="block text-gray-700">Role:</label>
        <select v-model="form.role" class="w-full mt-1 form-select">
          <option :value="null" />
          <option value="user">User</option>
          <option value="owner">Owner</option>
        </select>
        <label class="block mt-4 text-gray-700">Trashed:</label>
        <select v-model="form.trashed" class="w-full mt-1 form-select">
          <option :value="null" />
          <option value="with">With Trashed</option>
          <option value="only">Only Trashed</option>
        </select>
      </search-filter>
      <inertia-link class="btn-indigo" :href="route('users.create')">
        <span>Create</span>
        <span class="hidden md:inline">User</span>
      </inertia-link>
    </div>
    <div class="overflow-x-auto bg-white rounded shadow">
      <table class="w-full whitespace-no-wrap">
        <tr class="font-bold text-left">
          <th class="px-6 pt-6 pb-4">Name</th>
          <th class="px-6 pt-6 pb-4">Email</th>
          <th class="px-6 pt-6 pb-4" colspan="2">Role</th>
        </tr>
        <tr
          v-for="user in users"
          :key="user.id"
          class="hover:bg-gray-100 focus-within:bg-gray-100"
        >
          <td class="border-t">
            <inertia-link
              class="flex items-center px-6 py-4 focus:text-indigo-500"
              :href="route('users.edit', user.id)"
            >
              <img
                v-if="user.photo"
                class="block w-5 h-5 mr-2 -my-2 rounded-full"
                :src="user.photo"
              />
              {{ user.name }}
              <icon
                v-if="user.deleted_at"
                name="trash"
                class="flex-shrink-0 w-3 h-3 ml-2 fill-gray-400"
              />
            </inertia-link>
          </td>
          <td class="border-t">
            <inertia-link
              class="flex items-center px-6 py-4"
              :href="route('users.edit', user.id)"
              tabindex="-1"
            >
              {{ user.email }}
            </inertia-link>
          </td>
          <td class="border-t">
            <inertia-link
              class="flex items-center px-6 py-4"
              :href="route('users.edit', user.id)"
              tabindex="-1"
            >
              {{ user.owner ? "Owner" : "User" }}
            </inertia-link>
          </td>
          <td class="w-px border-t">
            <inertia-link
              class="flex items-center px-4"
              :href="route('users.edit', user.id)"
              tabindex="-1"
            >
              <icon name="cheveron-right" class="block w-6 h-6 fill-gray-400" />
            </inertia-link>
          </td>
        </tr>
        <tr v-if="users.length === 0">
          <td class="px-6 py-4 border-t" colspan="4">No users found.</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import Icon from "@/Shared/Icon";
import Layout from "@/Shared/Layout";
import mapValues from "lodash/mapValues";
import pickBy from "lodash/pickBy";
import SearchFilter from "@/Shared/SearchFilter";
import throttle from "lodash/throttle";

export default {
  metaInfo: { title: "Users" },
  layout: Layout,
  components: {
    Icon,
    SearchFilter,
  },
  props: {
    users: Array,
    filters: Object,
  },
  data() {
    return {
      form: {
        search: this.filters.search,
        role: this.filters.role,
        trashed: this.filters.trashed,
      },
    };
  },
  watch: {
    form: {
      handler: throttle(function() {
        let query = pickBy(this.form);
        this.$inertia.replace(
          this.route(
            "users",
            Object.keys(query).length ? query : { remember: "forget" }
          )
        );
      }, 150),
      deep: true,
    },
  },
  methods: {
    reset() {
      this.form = mapValues(this.form, () => null);
    },
  },
};
</script>
