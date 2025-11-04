// stores/user.ts
import { defineStore } from 'pinia'
import { jwtDecode } from 'jwt-decode'

interface UserState {
  id: number | null
  token: string
}

interface JwtPayload {
  id?: number
  user_id?: number
  [key: string]: any
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    id: null,
    token: ''
  }),
  actions: {
    setToken(token: string) {
      this.token = token

      // JWT 디코딩
      const decoded: JwtPayload = jwtDecode(token)

      // user_id 또는 id를 store에 저장
      this.id = decoded.user_id ?? decoded.id ?? null
    },
    logout() {
      this.id = null
      this.token = ''
    }
  }
})
