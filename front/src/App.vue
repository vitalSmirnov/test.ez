<template>
  <main class="app">
    <header class="header-item">
      <h1>Items</h1>
    </header>

    <section>
      <ItemForm />
      <ItemList />
    </section>
  </main>
</template>

<script setup lang="ts">
  import ItemList from "./components/entities/ItemList.vue"
  import ItemForm from "./components/features/ItemForm.vue";
</script>
