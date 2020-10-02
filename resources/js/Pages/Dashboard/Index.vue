<template>
  <div>
    <h1 class="mb-8 text-3xl font-bold">Dashboard</h1>
    <p class="mb-8 leading-normal">
      Hey there! Welcome to Ping CRM, a demo app designed to help illustrate how
      <a
        class="text-indigo-500 underline hover:text-orange-600"
        href="https://inertiajs.com"
        >Inertia.js</a
      >
      works.
    </p>
    <p class="mb-8 leading-normal">
      This demo is using
      <a
        class="text-indigo-500 underline hover:text-orange-600"
        href="https://docs.masoniteproject.com/"
        >MasoniteFramework</a
      >
      and
      <a
        class="text-indigo-500 underline hover:text-orange-600"
        href="https://github.com/girardinsamuel/masonite-inertia"
        >masonite-inertia</a
      >
      Inertia server-side adapter!
    </p>
    <div class="flex mb-8">
      <inertia-link class="btn-indigo" href="/500">500 error</inertia-link>
      <inertia-link class="ml-1 btn-indigo" href="/404">404 error</inertia-link>
    </div>
    <p class="leading-normal">
      👆 These links are intended to be broken to illustrate how error handling
      works with Inertia.js.
    </p>
  </div>
</template>

<script>
import Layout from "@/Shared/Layout";

export default {
  metaInfo: { title: "Dashboard" },
  layout: Layout,
};
</script>
