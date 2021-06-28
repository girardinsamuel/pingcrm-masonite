<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">
      <inertia-link
        class="text-indigo-400 hover:text-indigo-600"
        :href="route('organizations')"
        >Organizations</inertia-link
      >
      <span class="font-medium text-indigo-400">/</span>
      {{ form.name }}
    </h1>
    <trashed-message
      v-if="organization.deleted_at"
      class="mb-6"
      @restore="restore"
    >
      This organization has been deleted.
    </trashed-message>
    <div class="max-w-3xl overflow-hidden bg-white rounded shadow">
      <form @submit.prevent="submit">
        <div class="flex flex-wrap p-8 -mb-8 -mr-6">
          <text-input
            v-model="form.name"
            :error="errors.name"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Name"
          />
          <text-input
            v-model="form.email"
            :error="errors.email"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Email"
          />
          <text-input
            v-model="form.phone"
            :error="errors.phone"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Phone"
          />
          <text-input
            v-model="form.address"
            :error="errors.address"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Address"
          />
          <text-input
            v-model="form.city"
            :error="errors.city"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="City"
          />
          <text-input
            v-model="form.region"
            :error="errors.region"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Province/State"
          />
          <select-input
            v-model="form.country"
            :error="errors.country"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Country"
          >
            <option :value="null" />
            <option value="CA">Canada</option>
            <option value="US">United States</option>
          </select-input>
          <text-input
            v-model="form.postal_code"
            :error="errors.postal_code"
            class="w-full pb-8 pr-6 lg:w-1/2"
            label="Postal code"
          />
        </div>
        <div
          class="flex items-center px-8 py-4 bg-gray-100 border-t border-gray-200"
        >
          <button
            v-if="!organization.deleted_at"
            class="text-red-600 hover:underline"
            tabindex="-1"
            type="button"
            @click="destroy"
          >
            Delete Organization
          </button>
          <loading-button
            :loading="sending"
            class="ml-auto btn-indigo"
            type="submit"
            >Update Organization</loading-button
          >
        </div>
      </form>
    </div>
    <h2 class="mt-12 text-2xl font-bold">Contacts</h2>
    <div class="mt-6 overflow-x-auto bg-white rounded shadow">
      <table class="w-full whitespace-no-wrap">
        <tr class="font-bold text-left">
          <th class="px-6 pt-6 pb-4">Name</th>
          <th class="px-6 pt-6 pb-4">City</th>
          <th class="px-6 pt-6 pb-4" colspan="2">Phone</th>
        </tr>
        <tr
          v-for="contact in organization.contacts"
          :key="contact.id"
          class="hover:bg-gray-100 focus-within:bg-gray-100"
        >
          <td class="border-t">
            <inertia-link
              class="flex items-center px-6 py-4 focus:text-indigo-500"
              :href="route('contacts.edit', contact.id)"
            >
              {{ contact.name }}
              <icon
                v-if="contact.deleted_at"
                name="trash"
                class="flex-shrink-0 w-3 h-3 ml-2 fill-gray-400"
              />
            </inertia-link>
          </td>
          <td class="border-t">
            <inertia-link
              class="flex items-center px-6 py-4"
              :href="route('contacts.edit', contact.id)"
              tabindex="-1"
            >
              {{ contact.city }}
            </inertia-link>
          </td>
          <td class="border-t">
            <inertia-link
              class="flex items-center px-6 py-4"
              :href="route('contacts.edit', contact.id)"
              tabindex="-1"
            >
              {{ contact.phone }}
            </inertia-link>
          </td>
          <td class="w-px border-t">
            <inertia-link
              class="flex items-center px-4"
              :href="route('contacts.edit', contact.id)"
              tabindex="-1"
            >
              <icon name="cheveron-right" class="block w-6 h-6 fill-gray-400" />
            </inertia-link>
          </td>
        </tr>
        <tr v-if="organization.contacts.length === 0">
          <td class="px-6 py-4 border-t" colspan="4">No contacts found.</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import Icon from "@/Shared/Icon";
import Layout from "@/Shared/Layout";
import LoadingButton from "@/Shared/LoadingButton";
import SelectInput from "@/Shared/SelectInput";
import TextInput from "@/Shared/TextInput";
import TrashedMessage from "@/Shared/TrashedMessage";

export default {
  metaInfo() {
    return { title: this.form.name };
  },
  layout: Layout,
  components: {
    Icon,
    LoadingButton,
    SelectInput,
    TextInput,
    TrashedMessage,
  },
  props: {
    errors: Object,
    organization: Object,
  },
  remember: "form",
  data() {
    return {
      sending: false,
      form: {
        name: this.organization.name,
        email: this.organization.email,
        phone: this.organization.phone,
        address: this.organization.address,
        city: this.organization.city,
        region: this.organization.region,
        country: this.organization.country,
        postal_code: this.organization.postal_code,
      },
    };
  },
  methods: {
    submit() {
      this.sending = true;
      this.$inertia
        .put(
          this.route("organizations.update", this.organization.id),
          this.form
        )
        .then(() => (this.sending = false));
    },
    destroy() {
      if (confirm("Are you sure you want to delete this organization?")) {
        this.$inertia.delete(
          this.route("organizations.destroy", this.organization.id)
        );
      }
    },
    restore() {
      if (confirm("Are you sure you want to restore this organization?")) {
        this.$inertia.put(
          this.route("organizations.restore", this.organization.id)
        );
      }
    },
  },
};
</script>
