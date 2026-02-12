<template>
  <div>
    <q-card-section>
      <q-separator dark inset/>
      <div v-if="store.fetching">
        <q-spinner size="20px" />
        Loading items...
      </div>
      <q-banner v-else-if="store.error" dense class="item-list__error">
        {{ store.error }}
      </q-banner>
      <q-list v-else dense class="item-list">
        <q-item v-if="items.length === 0">
          <q-item-section>No items yet.</q-item-section>
        </q-item>
        <q-item v-for="item in items" :key="item.id" >
          <ItemCard :item="item" />
        </q-item>
      </q-list>
      <PaginationControls
        v-if="items.length > 0"
        :page="page"
        :has-next="hasNext"
        :fetching="store.fetching"
        @prev="goPrev"
        @next="goNext"
      />
    </q-card-section>
  </div>
</template>


<script setup lang="ts">
import { computed, onMounted, ref } from "vue"
import ItemCard from "./ItemCard.vue"
import { useItemsStore } from "../../stores/items"
import PaginationControls from "../features/PaginationControls.vue"

const store = useItemsStore()
const items = computed(() => store.items)
const page = ref(store.page)
const pageSize = ref(store.limit)
const hasNext = ref(false)

const loadPage = async (nextPage: number) => {
  const result = await store.fetchItems(nextPage, pageSize.value)
  page.value = nextPage
  hasNext.value = result.length === pageSize.value
}

const goPrev = () => {
  if (page.value > 1) {
    void loadPage(page.value - 1)
  }
}

const goNext = () => {
  if (hasNext.value) {
    void loadPage(page.value + 1)
  }
}

onMounted(() => {
  void loadPage(page.value)
})


</script>

<style scoped lang="scss">
.item-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>