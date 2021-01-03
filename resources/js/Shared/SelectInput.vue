<template>
  <div>
    <label v-if="label" class="form-label" :for="id">{{ label }}:</label>
    <select
      :id="id"
      ref="input"
      v-model="selected"
      v-bind="$attrs"
      class="form-select"
      :class="{ error: errors.length }"
    >
      <slot />
    </select>
    <div v-if="error" class="form-error">{{ hasMultipleErrors ? error[0] : error }}</div>
  </div>
</template>

<script>
export default {
  inheritAttrs: false,
  props: {
    id: {
      type: String,
      default() {
        return `select-input-${this._uid}`;
      },
    },
    value: [String, Number, Boolean],
    label: String,
    error: {
      type: [String, Array],
      default: null
    },
  },
  data() {
    return {
      selected: this.value,
    };
  },
  watch: {
    selected(selected) {
      this.$emit("input", selected);
    },
  },
  computed: {
    hasMultipleErrors () {
      return this.error instanceof Array
    }
  },
  methods: {
    focus() {
      this.$refs.input.focus();
    },
    select() {
      this.$refs.input.select();
    },
  },
};
</script>
