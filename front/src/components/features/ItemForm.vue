<template>
  <div>

    <q-form @submit.prevent="submit">
      <q-input
        v-model="text"
        dense
        label="Item text"
        placeholder="Enter item text"
        :error="Boolean(error)"
        style="height: 80px"
        :disable="submitting"
      />
      <div>
        <q-btn
          color="primary"
          type="submit"
          :loading="submitting"
          :disable="submitting"
        >
          Add item
        </q-btn>
      </div>

      <q-banner v-if="error"  dense>
        {{ error }}
      </q-banner>
    </q-form>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { useItemsStore } from "../../stores/items"

const store = useItemsStore()
const text = ref("")
const error = ref<string | null>(null)
const submitting = ref(false)

const submit = async () => {
  error.value = null

  if (text.value.trim().length < 5) {
    error.value = "Text must be at least 5 characters."
    return
  }

  try {
    submitting.value = true
    await store.createItem(text.value.trim())
    text.value = ""
  } catch (err) {
    error.value = err instanceof Error ? err.message : "Failed to create item."
  } finally {
    submitting.value = false
  }
}
</script>
