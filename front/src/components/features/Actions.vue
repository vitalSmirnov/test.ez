<template>
  <q-item-section side class="actions">
    <q-btn
      v-if="mode === 'edit'"
      color="primary"
      size="sm"
      :loading="saving"
      :disable="saving || deleting"
      @click="emit('save')"
    >
      Save
    </q-btn>
    <q-btn
      v-else
      color="primary"
      size="sm"
      :disable="saving || deleting"
      @click="emit('edit')"
    >
      Edit
    </q-btn>
    <q-btn
      v-if="mode === 'edit'"
      color="secondary"
      size="sm"
      :disable="saving || deleting"
      @click="emit('cancel')"
    >
      Cancel
    </q-btn>
    <q-btn
      v-else
      color="negative"
      size="sm"
      :loading="deleting"
      :disable="saving || deleting"
      @click="emit('delete')"
    >
      Delete
    </q-btn>
  </q-item-section>
</template>

<script setup lang="ts">
defineProps<{
  mode: "view" | "edit"
  saving: boolean
  deleting: boolean
}>()

const emit = defineEmits<{
  (event: "edit"): void
  (event: "save"): void
  (event: "cancel"): void
  (event: "delete"): void
}>()
</script>

<style scoped lang="scss">
.actions {
  display: flex;
  flex-direction: row;
  gap: 0.5rem;
}
</style>