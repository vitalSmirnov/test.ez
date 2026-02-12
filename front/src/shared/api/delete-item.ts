import type { Item } from "../../stores/items"
import { request } from "./base"

export async function deleteItem(id: string): Promise<Item> {
  return request<Item>(`/api/items/${id}`, {
    method: "DELETE",
  })
}
