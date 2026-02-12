<template>
  <q-card class="card">
    <q-card-section class="card-content">
      <div class="card-main">
        <p v-if="mode === 'view'">{{ item.text }}</p>
        <q-input
          v-else
          v-model="editText"
          dense
          filled
          autofocus
          :error="Boolean(localError)"
          :disable="saving || deleting"
          placeholder="Item text"
        />
        <div class="card-meta">{{ new Date(item.created_at).toLocaleString() }}</div>
        <q-banner v-if="localError" dense class="card-error">
          {{ localError }}
        </q-banner>
      </div>
    </q-card-section>
    <q-card-actions>
      <Actions
        :mode="mode"
        :saving="saving"
        :deleting="deleting"
        @edit="startEdit"
        @save="saveEdit"
        @cancel="cancelEdit"
        @delete="removeItem"
      />
    </q-card-actions>
  </q-card>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { useItemsStore, type Item } from "../../stores/items";
import Actions from "../features/Actions.vue";

const props = defineProps<{
  item: Item
}>()

const store = useItemsStore()
const editText = ref("")
const mode = ref<"view" | "edit">("view")
const localError = ref<string | null>(null)
const saving = ref(false)
const deleting = ref(false)

const startEdit = () => {
  mode.value = "edit"
  editText.value = props.item.text
  localError.value = null
}

const cancelEdit = () => {
  editText.value = ""
  localError.value = null
  mode.value = "view"
}

const saveEdit = async () => {
  localError.value = null

  if (editText.value.trim().length < 5) {
    localError.value = "Text must be at least 5 characters."
    return
  }

  try {
    saving.value = true
    await store.updateItem(props.item.id, editText.value.trim())
    cancelEdit()
  } catch (err) {
    localError.value = err instanceof Error ? err.message : "Failed to update item."
  } finally {
    saving.value = false
  }
}

const removeItem = async () => {
  localError.value = null

  try {
    deleting.value = true
    await store.deleteItem(props.item.id)
  } catch (err) {
    localError.value = err instanceof Error ? err.message : "Failed to delete item."
  } finally {
    deleting.value = false
  }
}
</script>

<style scoped lang="scss">
.card {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  box-sizing: border-box;
  padding: 1rem;
}

.card-content {
  flex: 1;
}

.card-main {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.card-meta {
  font-size: 0.85rem;
  opacity: 0.7;
}

.card-error {
  margin-top: 0.25rem;
}

p {
  text-overflow: ellipsis;
  white-space: normal;
}

@media (max-width: 720px) {
  .card {
    flex-direction: column;
  }
}
</style>