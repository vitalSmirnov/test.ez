export async function request<T>(url: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch(url, init)

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`)
  }

  if (response.status === 204) {
    return undefined as T
  }

  return (await response.json()) as T
}
