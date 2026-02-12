import type { Item } from "../../stores/items"
import { request } from "./base"

type UpdateItemPayload = {
  id: string
  text: string
}

export async function updateItem(payload: UpdateItemPayload): Promise<Item> {
  return request<Item>(`/api/items/${payload.id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: payload.text }),
  })
}
