<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useToast } from 'vue-toastification';

const form = ref({
  name: '',
  username: '',
  email: '',
  password: '',
});
const isLoading = ref(false);
const router = useRouter();
const toast = useToast();

async function handleRegister() {
  isLoading.value = true;

  try {
    const response = await axios.post('http://127.0.0.1:5000/api/users', form.value);

    toast.success(response?.data?.message || 'Pendaftaran berhasil! Silakan masuk.');
    router.push('/');
  } catch (error) {
    console.error('Registration error:', error);
    toast.error(
      error.response?.data?.message || 'Terjadi kesalahan saat mendaftar. Silakan coba lagi.'
    );
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <div class="flex min-h-screen flex-col bg-[#EFF3FA]">
    <div
      class="container mx-auto flex max-w-[1130px] flex-1 items-center justify-center px-4 py-5 sm:px-0"
    >
      <form
        @submit.prevent="handleRegister"
        class="flex w-full max-w-[500px] flex-col gap-5 rounded-3xl border border-[#E5E5E5] bg-white p-6 sm:p-[50px_40px]"
      >
        <div class="flex justify-center">
          <h1 class="text-4xl font-extrabold tracking-wide text-[#0D5CD7] sm:text-5xl">Horus</h1>
        </div>
        <h1 class="text-2xl font-bold leading-[34px]">Daftar</h1>
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
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none placeholder:font-normal placeholder:text-[#616369]"
              placeholder="Tulis nama lengkapmu"
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
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none placeholder:font-normal placeholder:text-[#616369]"
              placeholder="Buat username unik"
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
              class="w-full appearance-none bg-transparent font-semibold text-black outline-none placeholder:font-normal placeholder:text-[#616369]"
              placeholder="Tulis alamat email kamu"
              required
            />
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <label for="password" class="font-medium">Password</label>
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
              placeholder="Buat password yang kuat"
              required
            />
          </div>
        </div>
        <div class="mt-2 flex flex-col gap-3">
          <button
            type="submit"
            :disabled="isLoading"
            class="rounded-full bg-[#0D5CD7] p-[12px_24px] text-center font-semibold text-white transition-all duration-300 hover:bg-blue-800 disabled:bg-gray-400"
          >
            <span v-if="isLoading">Memuat...</span>
            <span v-else>Daftar Akun Saya</span>
          </button>
          <router-link
            :to="{ name: 'login' }"
            class="rounded-full border border-[#E5E5E5] bg-white p-[12px_24px] text-center font-semibold transition-all duration-300 hover:bg-gray-100"
          >
            Masuk ke Akun Saya
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>
