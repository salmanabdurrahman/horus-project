<script setup>
import { computed, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import { getLoggedInUser, logout } from '@/services/auth';
import apiClient from '@/services/api';

const users = ref([]);
const isLoading = ref(true);
const loggedInUser = ref(null);
const searchQuery = ref('');
const sortKey = ref('name');
const sortOrder = ref('asc');

const router = useRouter();
const toast = useToast();

const filteredAndSortedUsers = computed(() => {
  let tempUsers = users.value;

  if (searchQuery.value) {
    tempUsers = tempUsers.filter(user => {
      const query = searchQuery.value.toLowerCase();
      return (
        user.name.toLowerCase().includes(query) ||
        user.username.toLowerCase().includes(query) ||
        user.email.toLowerCase().includes(query)
      );
    });
  }

  tempUsers.sort((a, b) => {
    let fa = a[sortKey.value].toLowerCase();
    let fb = b[sortKey.value].toLowerCase();
    if (fa < fb) return sortOrder.value === 'asc' ? -1 : 1;
    if (fa > fb) return sortOrder.value === 'asc' ? 1 : -1;
    return 0;
  });

  return tempUsers;
});

async function fetchUsers() {
  isLoading.value = true;

  try {
    const response = await apiClient.get('/users');
    users.value = response?.data?.data || [];
  } catch (error) {
    console.error('Error fetching users:', error);
    toast.error(error.response?.data?.message || 'Terjadi kesalahan saat mengambil data pengguna.');
  } finally {
    isLoading.value = false;
  }
}

function sortBy(key) {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc';
  } else {
    sortKey.value = key;
    sortOrder.value = 'asc';
  }
}

async function handleDelete(userId) {
  if (confirm('Apakah Anda yakin ingin menghapus pengguna ini?')) {
    try {
      const response = await apiClient.delete(`/users/${userId}`);
      toast.success(response?.data?.message || 'Pengguna berhasil dihapus!');
      await fetchUsers();
    } catch (error) {
      console.error('Error deleting user:', error);
      toast.error(error.response?.data?.message || 'Terjadi kesalahan saat menghapus pengguna.');
    }
  }
}

async function handleLogout() {
  logout();
  toast.success('Anda berhasil keluar!');
  router.push({ name: 'login' });
}

onMounted(() => {
  loggedInUser.value = getLoggedInUser();
  fetchUsers();
});
</script>

<template>
  <div class="flex min-h-screen flex-col bg-[#EFF3FA] p-4 sm:p-6 lg:p-12">
    <div class="container mx-auto max-w-7xl">
      <div class="mb-8 flex flex-col items-start justify-between gap-4 sm:flex-row sm:items-center">
        <div>
          <h1 class="text-3xl font-bold text-gray-800">Manajemen Pengguna</h1>
          <p class="mt-1 text-gray-500">
            Selamat datang kembali, {{ loggedInUser?.name || 'Pengguna' }}!
          </p>
        </div>
        <button
          @click="handleLogout"
          class="rounded-full border border-[#E5E5E5] bg-white p-[12px_24px] text-center font-semibold transition-all duration-300 hover:bg-red-500 hover:text-white"
        >
          Logout
        </button>
      </div>
      <div class="rounded-3xl border border-[#E5E5E5] bg-white p-6 sm:p-8">
        <div class="relative mb-6">
          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-4">
            <i class="bx bx-search text-xl text-gray-400"></i>
          </div>
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Cari berdasarkan nama, username, atau email..."
            class="block w-full rounded-full border border-[#E5E5E5] bg-white py-3 pl-12 pr-4 outline-none transition-all duration-300 focus:ring-2 focus:ring-[#FFC736] sm:text-sm"
          />
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full">
            <thead>
              <tr>
                <th
                  v-for="key in ['name', 'username', 'email']"
                  :key="key"
                  scope="col"
                  class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
                >
                  <button
                    @click="sortBy(key)"
                    class="flex items-center gap-2 uppercase hover:text-[#0D5CD7]"
                  >
                    {{ key }}
                    <span v-if="sortKey === key">
                      <i v-if="sortOrder === 'asc'" class="bx bxs-up-arrow text-xs"></i>
                      <i v-else class="bx bxs-down-arrow text-xs"></i>
                    </span>
                  </button>
                </th>
                <th
                  scope="col"
                  class="relative py-3.5 pl-3 pr-4 text-left text-sm font-semibold uppercase text-gray-900 sm:pr-6"
                >
                  Aksi
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr v-if="isLoading">
                <td colspan="4" class="py-16 text-center">
                  <i class="bx bx-loader-alt bx-spin text-4xl text-gray-400"></i>
                </td>
              </tr>
              <tr v-else-if="filteredAndSortedUsers.length === 0">
                <td colspan="4" class="py-16 text-center text-gray-500">
                  <i class="bx bx-search-alt-2 text-5xl"></i>
                  <p class="mt-2 font-semibold">Data Tidak Ditemukan</p>
                  <p class="text-sm">Tidak ada data yang cocok dengan pencarianmu.</p>
                </td>
              </tr>
              <tr
                v-else
                v-for="user in filteredAndSortedUsers"
                :key="user.id"
                class="hover:bg-gray-50"
              >
                <td
                  class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
                >
                  {{ user.name }}
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  {{ user.username }}
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{ user.email }}</td>
                <td
                  class="relative whitespace-nowrap py-4 pl-3 pr-4 text-left text-sm font-medium sm:pr-6"
                >
                  <div class="flex items-center gap-4">
                    <router-link
                      :to="{ name: 'update-user', params: { id: user.id } }"
                      class="text-[#0D5CD7] transition-colors hover:text-blue-800"
                      title="Update"
                    >
                      <i class="bx bxs-edit text-xl"></i>
                    </router-link>
                    <button
                      @click="handleDelete(user.id)"
                      class="text-red-600 transition-colors hover:text-red-900"
                      title="Delete"
                    >
                      <i class="bx bxs-trash text-xl"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
