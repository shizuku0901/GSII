// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBX4lwh2pukmJYVVS2iwGmEhDIneGy1yOs",
  authDomain: "gsii-7b557.firebaseapp.com",
  projectId: "gsii-7b557",
  storageBucket: "gsii-7b557.firebasestorage.app",
  messagingSenderId: "653124992327",
  appId: "1:653124992327:web:de56415699ed6f6385e062",
  measurementId: "G-BEZV4Z6GW9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);