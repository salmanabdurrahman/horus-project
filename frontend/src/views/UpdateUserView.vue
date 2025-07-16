<script setup>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import apiClient from '@/services/api';

const form = ref({
  name: '',
  username: '',
  email: '',
  password: '',
});
const isLoading = ref(false);
const router = useRouter();
const route = useRoute();
const toast = useToast();

const userId = route.params.id;

async function fetchUserData() {
  isLoading.value = true;

  try {
    const response = await apiClient.get(`/users/${userId}`);
    const userData = response?.data?.data;

    form.value.name = userData.name;
    form.value.username = userData.username;
    form.value.email = userData.email;
  } catch (error) {
    console.error('Error fetching user data:', error);
    toast.error(error.response?.data?.message || 'Terjadi kesalahan saat mengambil data pengguna.');
  } finally {
    isLoading.value = false;
  }
}

async function handleUpdate() {
  isLoading.value = true;

  try {
    const response = await apiClient.put(`/users/${userId}`, form.value);
    toast.success(response?.data?.message || 'Data pengguna berhasil diperbarui!');
    router.push({ name: 'dashboard' });
  } catch (error) {
    console.error('Update error:', error);
    toast.error(
      error.response?.data?.message || 'Terjadi kesalahan saat memperbarui data pengguna.'
    );
  } finally {
    isLoading.value = false;
  }
}

onMounted(() => {
  fetchUserData();
});
</script>

<template>
  <div class="flex min-h-screen flex-col bg-[#EFF3FA]">
    <div class="container mx-auto flex flex-1 items-center justify-center px-4 py-5 sm:px-0">
      <form
        v-if="!isLoading"
        @submit.prevent="handleUpdate"
        class="flex w-full max-w-[500px] flex-col gap-5 rounded-3xl border border-[#E5E5E5] bg-white p-6 sm:p-[50px_40px]"
      >
        <h1 class="text-2xl font-bold leading-[34px]">Mengubah Data Pengguna</h1>
        <p class="text-sm text-gray-500">
          Ubah data untuk pengguna: <span class="font-bold">{{ form.name }}</span>
        </p>
        <div class="flex flex-col gap-2">
          <label for="name" class="font-medium">Nama Lengkap</label>
          <div
            class="flex items-center gap-[10px] rounded-full border border-[#E5E5E5] p-[12px_20px] transition-all duration-300 focus-within:ring-2 focus-within:ring-[#FFC736]"
          >
            <div class="flex shrink-0">
              <i class="bx bxs-user text-2xl text-gray-500"></i>
            </div>
            <input
              type="text"
              id="name"
              v-model="form.name"
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none"
              required
              autofocus
            />
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <label for="username" class="font-medium">Username</label>
          <div
            class="flex items-center gap-[10px] rounded-full border border-[#E5E5E5] p-[12px_20px] transition-all duration-300 focus-within:ring-2 focus-within:ring-[#FFC736]"
          >
            <div class="flex shrink-0">
              <i class="bx bxs-user-circle text-2xl text-gray-500"></i>
            </div>
            <input
              type="text"
              id="username"
              v-model="form.username"
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none"
              required
            />
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <label for="email" class="font-medium">Alamat Email</label>
          <div
            class="flex items-center gap-[10px] rounded-full border border-[#E5E5E5] p-[12px_20px] transition-all duration-300 focus-within:ring-2 focus-within:ring-[#FFC736]"
          >
            <div class="flex shrink-0">
              <i class="bx bxs-envelope text-2xl text-gray-500"></i>
            </div>
            <input
              type="email"
              id="email"
              v-model="form.email"
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none"
              required
            />
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <label for="password" class="font-medium">Password Baru</label>
          <div
            class="flex items-center gap-[10px] rounded-full border border-[#E5E5E5] p-[12px_20px] transition-all duration-300 focus-within:ring-2 focus-within:ring-[#FFC736]"
          >
            <div class="flex shrink-0">
              <i class="bx bxs-lock-alt text-2xl text-gray-500"></i>
            </div>
            <input
              type="password"
              id="password"
              v-model="form.password"
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none placeholder:font-normal placeholder:text-[#616369]"
              placeholder="Kosongkan jika tidak ingin diubah"
            />
          </div>
        </div>
        <div class="mt-2 flex flex-col gap-3">
          <button
            type="submit"
            :disabled="isLoading"
            class="rounded-full bg-[#0D5CD7] p-[12px_24px] text-center font-semibold text-white transition-all duration-300 hover:bg-blue-800 disabled:bg-gray-400"
          >
            <span v-if="isLoading">Menyimpan...</span>
            <span v-else>Simpan Perubahan</span>
          </button>
          <router-link
            :to="{ name: 'dashboard' }"
            class="rounded-full border border-[#E5E5E5] bg-white p-[12px_24px] text-center font-semibold transition-all duration-300 hover:bg-gray-100"
          >
            Batal
          </router-link>
        </div>
      </form>
      <div v-else class="text-center">
        <i class="bx bx-loader-alt bx-spin text-4xl text-gray-400"></i>
        <p class="mt-2 text-gray-500">Memuat data pengguna...</p>
      </div>
    </div>
  </div>
</template>
