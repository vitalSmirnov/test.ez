import { defineStore } from "pinia"
import { fetchItems } from "../shared/api/fetch-items"
import { createItem } from "../shared/api/create-item"
import { updateItem } from "../shared/api/update-item"
import { deleteItem } from "../shared/api/delete-item"


export type Item = {
  id: string
  text: string
  created_at: string
}

type ItemsState = {
  items: Item[]
  fetching: boolean
  error: string | null
  page: number
  limit: number
}

export const useItemsStore = defineStore("items", {
  state: (): ItemsState => ({
    items: [],
    fetching: false,
    error: null,
    page: 1,
    limit: 10,
  }),
  actions: {
    async fetchItems(page = 1, limit = 20) {
      this.fetching = true
      this.error = null
      this.page = page
      this.limit = limit
      
      try {
        const skip = (page - 1) * limit
        const data = await fetchItems({ skip, limit })
        this.items = data.items ?? []
        return this.items
      } catch (error) {
        this.error = error instanceof Error ? error.message : "Unknown error"
        throw new Error(this.error)
      } finally {
        this.fetching = false
      }

    },
    async createItem(text: string) {
      try {
        const created = await createItem({ text })
        this.items = [created, ...this.items]
        return created
      } catch (error) {
        throw error
      }
    },
    async updateItem(id: string, text: string) {
      try {
        const data = await updateItem({ id, text })
        this.items = this.items.map((item) => (item.id === id ? data : item))
        return data
      } catch (error) {
        throw error
      }
    },
    async deleteItem(id: string) {
      try {
        const deleted = await deleteItem(id)
        this.items = this.items.filter((item) => item.id !== id)
        return deleted
      } catch (error) {
        throw error
      }
    },
  },
})
