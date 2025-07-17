<script setup>
import { getLoggedInUser } from '@/services/auth';

const isLoggedIn = !!getLoggedInUser();
const homeRoute = isLoggedIn ? { name: 'dashboard' } : { name: 'login' };
</script>

<template>
  <div class="flex min-h-screen flex-col items-center justify-center bg-[#EFF3FA] p-4">
    <div class="w-full max-w-md text-center">
      <h1 class="text-9xl font-extrabold tracking-widest text-[#0D5CD7]">404</h1>
      <div class="mt-4 rounded-xl bg-white p-6 shadow-md">
        <h2 class="text-2xl font-bold text-gray-800">Halaman Tidak Ditemukan</h2>
        <p class="mt-2 text-gray-500">
          Maaf, kami tidak dapat menemukan halaman yang Anda cari. Mungkin URL-nya salah ketik atau
          halamannya sudah dipindahkan.
        </p>
        <router-link
          :to="homeRoute"
          class="mt-6 inline-block rounded-full bg-[#0D5CD7] px-8 py-3 text-center font-semibold text-white transition-all duration-300 hover:bg-blue-800"
        >
          Kembali ke Halaman Utama
        </router-link>
      </div>
    </div>
  </div>
</template>
