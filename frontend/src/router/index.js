import { createRouter, createWebHistory } from 'vue-router';
import { getLoggedInUser } from '@/services/auth';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: { guestOnly: true },
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
      meta: { guestOnly: true },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/update/:id',
      name: 'update-user',
      component: () => import('../views/UpdateUserView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue'),
    },
  ],
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = !!getLoggedInUser();

  if (to.meta.guestOnly && isLoggedIn) {
    next({ name: 'dashboard' });
  }

  if (to.meta.requiresAuth && !isLoggedIn) {
    next({ name: 'login' });
  }

  next();
});

export default router;
