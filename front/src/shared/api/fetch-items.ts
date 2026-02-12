import type { Item } from "../../stores/items"
import { request } from "./base"

type ItemsResponse = {
  items: Item[]
}

export async function fetchItems(params?: {
  skip?: number
  limit?: number
}): Promise<ItemsResponse> {
  const query = new URLSearchParams()

  if (params?.skip !== undefined) {
    query.set("skip", String(params.skip))
  }

  if (params?.limit !== undefined) {
    query.set("limit", String(params.limit))
  }

  const suffix = query.toString()
  const url = suffix ? `/api/items?${suffix}` : "/api/items"

  return request<ItemsResponse>(url)
}
