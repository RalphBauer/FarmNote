import { createRouter, createWebHistory } from 'vue-router';
import StartPage from "@/views/StartPage.vue";
import LoadSessionPage from "@/views/LoadSessionPage.vue";
import MainPage from "@/views/MainPage.vue";
import CreateNote from "@/views/CreateNote.vue";
import NoteListPage from "@/views/NoteListPage.vue";
import EditNote from "@/views/EditNote.vue";

const routes = [
  {
    path: '/',
    name: 'start',
    component: StartPage
  },
  {
    path: '/load-session-page',
    name: 'load-session-page',
    component: LoadSessionPage
  },
  {
    path: '/main-page/:token',  // Füge den Token-Parameter hinzu
    name: 'main-page',
    component: MainPage,
    props: true  // Übergebe den Token als Prop an die MainPage-Komponente
  },
  {
    path: "/create-note",
    name: "create-note",
    component: CreateNote,
  },
  {
    path: '/note-list',
    name: 'note-list',
    component: NoteListPage,
  },
  {
    path: '/edit-note ',  // Route für das Bearbeiten der Notiz
    name: 'edit-note',
    component: EditNote,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
