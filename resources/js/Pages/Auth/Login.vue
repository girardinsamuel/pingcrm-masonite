<template>
  <div class="flex items-center justify-center min-h-screen p-6 bg-indigo-800">
    <div class="w-full max-w-md">
      <logo class="block w-full max-w-xs mx-auto fill-white" height="50" />
      <form
        class="mt-8 overflow-hidden bg-white rounded-lg shadow-xl"
        @submit.prevent="submit"
      >
        <div class="px-10 py-12">
          <h1 class="text-3xl font-bold text-center">Welcome Back!</h1>
          <div class="w-24 mx-auto mt-6 border-b-2" />
          <text-input
            v-model="form.email"
            :error="errors.email"
            class="mt-10"
            label="Email"
            type="email"
            autofocus
            autocapitalize="off"
          />
          <text-input
            v-model="form.password"
            class="mt-6"
            label="Password"
            type="password"
          />
          <label class="flex items-center mt-6 select-none" for="remember">
            <input
              id="remember"
              v-model="form.remember"
              class="mr-1"
              type="checkbox"
            />
            <span class="text-sm">Remember Me</span>
          </label>
        </div>
        <div
          class="flex items-center justify-between px-10 py-4 bg-gray-100 border-t border-gray-200"
        >
          <a class="hover:underline" tabindex="-1" href="#reset-password"
            >Forget password?</a
          >
          <loading-button :loading="sending" class="btn-indigo" type="submit"
            >Login</loading-button
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import LoadingButton from "@/Shared/LoadingButton";
import Logo from "@/Shared/Logo";
import TextInput from "@/Shared/TextInput";

export default {
  metaInfo: { title: "Login" },
  components: {
    LoadingButton,
    Logo,
    TextInput,
  },
  props: {
    errors: Object,
  },
  data() {
    return {
      sending: false,
      form: {
        email: "johndoe@example.com",
        password: "secret",
        remember: null,
      },
    };
  },
  methods: {
    submit() {
      this.sending = true;
      this.$inertia
        .post(this.route("login.attempt"), {
          email: this.form.email,
          password: this.form.password,
          remember: this.form.remember,
        })
        .then(() => (this.sending = false));
    },
  },
};
</script>
