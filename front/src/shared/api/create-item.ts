import type { Item } from "../../stores/items"
import { request } from "./base"

type CreateItemPayload = {
  text: string
}

export async function createItem(payload: CreateItemPayload): Promise<Item> {
  return request<Item>("/api/items", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
}
