<template>
  <div>
    <label v-if="label" class="form-label">{{ label }}:</label>
    <div class="p-0 form-input" :class="{ error: error}">
      <input ref="file" type="file" :accept="accept" class="hidden" @change="change">
      <div v-if="!value" class="p-2">
        <button type="button" class="px-4 py-1 text-xs font-medium text-white bg-gray-500 rounded-sm hover:bg-gray-700" @click="browse">
          Browse
        </button>
      </div>
      <div v-else class="flex items-center justify-between p-2">
        <div class="flex-1 pr-1">{{ value.name }} <span class="text-xs text-gray-500">({{ filesize(value.size) }})</span></div>
        <button type="button" class="px-4 py-1 text-xs font-medium text-white bg-gray-500 rounded-sm hover:bg-gray-700" @click="remove">
          Remove
        </button>
      </div>
    </div>
    <div v-if="error" class="form-error">{{ hasMultipleErrors ? error[0] : error }}</div>
  </div>
</template>

<script>
export default {
  props: {
    value: File,
    label: String,
    accept: String,
    error: {
      type: [String, Array],
      default: null
    },
  },
  watch: {
    value(value) {
      if (!value) {
        this.$refs.file.value = ''
      }
    },
  },
  computed: {
    hasMultipleErrors () {
      return this.error instanceof Array
    }
  },
  methods: {
    filesize(size) {
      var i = Math.floor(Math.log(size) / Math.log(1024))
      return (size / Math.pow(1024, i) ).toFixed(2) * 1 + ' ' + ['B', 'kB', 'MB', 'GB', 'TB'][i]
    },
    browse() {
      this.$refs.file.click()
    },
    change(e) {
      this.$emit('input', e.target.files[0])
    },
    remove() {
      this.$emit('input', null)
    },
  },
}
</script>
