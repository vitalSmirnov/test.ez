<template>
  <div class="pagination">
    <q-btn
      flat
      size="sm"
      label="Prev"
      :disable="page <= 1 || fetching"
      @click="emit('prev')"
    />
    <span>{{ page }}</span>
    <q-btn
      flat
      size="sm"
      label="Next"
      :disable="!hasNext || fetching"
      @click="emit('next')"
    />
  </div>
</template>

<script setup lang="ts">
defineProps<{
  page: number
  hasNext: boolean
  fetching: boolean
}>()

const emit = defineEmits<{ (event: "prev"): void; (event: "next"): void }>()
</script>

<style scoped lang="scss">
.pagination {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 0.75rem;
  & span {
    font-weight: bold;
  }
}
</style>
